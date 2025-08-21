# -*- coding: utf-8 -*-
"""
final_vid_edit.py
- BAT'ten gelen ortam değişkenleri ile video düzenleme
- Captions: start|end|text biçiminde CAP_FILE'dan okunur
- Hızlandırma, büyük font, merkez yerleşim, görünür stroke
- BGM: başlangıç/bitiş, loop, miks/tek-kanal opsiyonu
- Konsol ilerleme çubuğu (tqdm)
"""

import os, sys
from typing import List, Tuple, Optional
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from moviepy.editor import (
    VideoFileClip, CompositeVideoClip, ImageClip,
    AudioFileClip, CompositeAudioClip, vfx
)
from moviepy.audio.fx.all import audio_loop

# tqdm/proglog ilerleme çubuğu
try:
    from proglog import TqdmProgressBarLogger
    _LOGGER = TqdmProgressBarLogger()
except Exception:
    _LOGGER = None

# ---------- ENV / PATHS ----------
ROOT_DIR      = os.environ.get("ROOT_DIR", os.path.dirname(os.path.abspath(__file__)))
INPUT_VIDEO   = os.environ.get("INPUT_VIDEO", os.path.join(ROOT_DIR, "Binance_API.mp4"))
OUTPUT_VIDEO  = os.environ.get("OUTPUT_VIDEO", os.path.join(ROOT_DIR, "Binance_API_annotated.mp4"))
BGM_FILE      = os.environ.get("BGM_FILE", os.path.join(ROOT_DIR, "bgm.wav"))
CAP_FILE      = os.environ.get("CAP_FILE", os.path.join(ROOT_DIR, "_captions.tmp"))
SPEED_FACTOR  = float(os.environ.get("SPEED_FACTOR", "4"))
MUTE_ORIGINAL = os.environ.get("MUTE_ORIGINAL", "true").lower() in ("1","true","yes","y")
MUSIC_VOL     = float(os.environ.get("MUSIC_VOL", "0.14"))
BGM_START_S   = os.environ.get("BGM_START_S", "")
BGM_END_S     = os.environ.get("BGM_END_S", "")

def _to_float_or_none(x: str) -> Optional[float]:
    x = (x or "").strip()
    if x == "": return None
    try: return float(x)
    except: return None

BGM_START_S = _to_float_or_none(BGM_START_S)
BGM_END_S   = _to_float_or_none(BGM_END_S)

print("=== presentation_video.py ===")
print("Python      :", sys.version.split()[0])
print("SCRIPT_DIR  :", ROOT_DIR)
print("INPUT_VIDEO :", INPUT_VIDEO)
print("OUTPUT_VIDEO:", OUTPUT_VIDEO)
print("CAP_FILE    :", CAP_FILE)
print("BGM_FILE    :", BGM_FILE)
print("SPEED_FACTOR:", SPEED_FACTOR, "  MUTE_ORIGINAL:", MUTE_ORIGINAL)
print("BGM window  :", BGM_START_S, "->", BGM_END_S)

# ---------- Yazı parametreleri ----------
# İsterseniz burada sabit font yolu verebilirsiniz:
FONT_PATH      = None  # örn: r"C:\Windows\Fonts\arial.ttf"
FONT_SIZE_FR   = 0.10  # video yüksekliğinin %10'u
MAX_WIDTH_FR   = 0.96
POS_MODE       = "center"  # "center" | "top" | "bottom"
MARGIN_PX      = 60

TEXT_OPACITY   = 0.85
STROKE_OPACITY = 0.70
TEXT_COLOR     = (255,255,255, int(255*TEXT_OPACITY))
STROKE_COLOR   = (0,0,0, int(255*STROKE_OPACITY))

PADDING_X, PADDING_Y = 14, 12
ROUND_RADIUS   = 16
DRAW_BOX       = False
BG_COLOR       = (0,0,0,0)

# ---------- Yardımcılar ----------
def _win_fonts_dir() -> str:
    return os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

def get_font(size: int) -> ImageFont.FreeTypeFont:
    # Önce kullanıcı fontu
    if FONT_PATH and os.path.isfile(FONT_PATH):
        try: return ImageFont.truetype(FONT_PATH, size=size)
        except: pass
    # Yaygın Windows
    for name in ["arial.ttf", "arialbd.ttf", "segoeui.ttf", "calibri.ttf",
                 "tahoma.ttf", "verdana.ttf", "DejaVuSans.ttf"]:
        p = os.path.join(_win_fonts_dir(), name)
        if os.path.isfile(p):
            try: return ImageFont.truetype(p, size=size)
            except: pass
    # Pillow fallback
    try:
        from PIL import __file__ as PIL_FILE
        dejavu = os.path.join(os.path.dirname(PIL_FILE), "fonts", "DejaVuSans.ttf")
        if os.path.isfile(dejavu):
            return ImageFont.truetype(dejavu, size=size)
    except: pass
    return ImageFont.load_default()

def _text_size(font: ImageFont.FreeTypeFont, text: str) -> Tuple[int,int]:
    x0,y0,x1,y1 = font.getbbox(text)
    return (x1-x0, y1-y0)

def render_text_image(
    text: str, width_px: int, font_size: int,
    text_color=TEXT_COLOR, stroke_w: int = 0,
    padding_x=PADDING_X, padding_y=PADDING_Y,
    draw_box=DRAW_BOX, bg_color=BG_COLOR, round_radius=ROUND_RADIUS
):
    font = get_font(font_size)
    # kelime sarma
    lines = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append(""); continue
        cur = ""
        for word in paragraph.split():
            cand = (cur + " " + word).strip()
            w,_ = _text_size(font, cand)
            if w + 2*padding_x <= width_px: cur = cand
            else:
                if cur: lines.append(cur)
                cur = word
        if cur: lines.append(cur)

    line_gap  = max(6, int(font_size*0.16))
    line_sizes = [(_text_size(font, ln) if ln else (0,font_size)) for ln in lines]
    text_w = max((w for w,_ in line_sizes), default=0)
    text_h = sum(h for _,h in line_sizes) + max(0,len(lines)-1)*line_gap

    box_w = min(width_px, text_w + 2*padding_x)
    box_h = text_h + 2*padding_y

    img = Image.new("RGBA", (box_w, box_h), (0,0,0,0))
    draw = ImageDraw.Draw(img, "RGBA")
    if draw_box:
        try: draw.rounded_rectangle((0,0,box_w,box_h), radius=round_radius, fill=bg_color)
        except: draw.rectangle((0,0,box_w,box_h), fill=bg_color)

    y = padding_y
    for ln in lines:
        w,h = _text_size(font, ln) if ln else (0,font_size)
        x   = (box_w - w)//2
        if ln:
            draw.text((x,y), ln, font=font, fill=text_color,
                      stroke_width=stroke_w, stroke_fill=STROKE_COLOR)
        y += h + line_gap
    return img

def pil_to_imageclip(img: Image.Image, start: float, dur: float, W:int, H:int,
                     pos_mode:str, margin_px:int) -> ImageClip:
    arr = np.array(img)
    if pos_mode == "center":  y_pos = (H - img.height)//2
    elif pos_mode == "top":   y_pos = max(0, margin_px)
    else:                     y_pos = H - img.height - max(0, margin_px)
    x_pos = "center"

    if arr.ndim == 3 and arr.shape[2] == 4:
        rgb   = arr[..., :3]
        alpha = (arr[..., 3].astype("float32") / 255.0)
        clip  = ImageClip(rgb).set_start(start).set_duration(dur).set_position((x_pos, y_pos))
        mask  = ImageClip(alpha, ismask=True).set_start(start).set_duration(dur).set_position((x_pos, y_pos))
        clip  = clip.set_mask(mask)
    else:
        clip  = ImageClip(arr).set_start(start).set_duration(dur).set_position((x_pos, y_pos))
    return clip.fadein(0.12).fadeout(0.12)

def seconds_to_hhmmss(s: float) -> str:
    h = int(s//3600); s%=3600
    m = int(s//60);   s = s%60
    return f"{h:02d}:{m:02d}:{s:05.2f}"

# ---------- Captions loader ----------
def load_captions(path: str) -> List[Tuple[float,float,str]]:
    caps: List[Tuple[float,float,str]] = []
    if not os.path.isfile(path):
        print(f"[captions][WARN] CAP_FILE bulunamadı: {path}")
        return caps
    # UTF-8 (BOM dahil) → ANSI fallback
    for enc in ("utf-8-sig", "utf-8", "cp1254", "latin-1"):
        try:
            with open(path, "r", encoding=enc, errors="strict") as f:
                rows = f.read().splitlines()
            break
        except Exception:
            continue
    else:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            rows = f.read().splitlines()

    for ln in rows:
        ln = ln.strip()
        if not ln or ln.startswith("#"): continue
        parts = ln.split("|", 2)
        if len(parts) < 3: continue
        try:
            s = float(parts[0].strip())
            e = float(parts[1].strip())
        except:
            continue
        txt = parts[2].strip()
        if e > s: caps.append((s,e,txt))
    return caps

# ---------- Main ----------
def main():
    if not os.path.isfile(INPUT_VIDEO):
        print(f"[HATA] Video bulunamadı: {INPUT_VIDEO}")
        input("Devam etmek için Enter..."); return

    base = VideoFileClip(INPUT_VIDEO)
    print(f"Orijinal süre: {seconds_to_hhmmss(base.duration)} ({base.duration:.2f}s)")

    if SPEED_FACTOR and SPEED_FACTOR != 1.0:
        base = base.fx(vfx.speedx, SPEED_FACTOR)
        print(f"Hız x{SPEED_FACTOR} -> Yeni süre: {seconds_to_hhmmss(base.duration)}")

    W, H = base.w, base.h
    max_w     = int(W * MAX_WIDTH_FR)
    font_px   = max(36, int(H * FONT_SIZE_FR))
    stroke_px = max(2, int(font_px * 0.06))
    print(f"[font] size={font_px}px stroke={stroke_px}px max_w={max_w}px video={W}x{H}")

    # captions
    caps = load_captions(CAP_FILE)
    print(f"[captions] Yüklendi: {len(caps)} satır ({os.path.basename(CAP_FILE)})")
    if caps[:2]:
        for i,(s,e,t) in enumerate(caps[:2], 1):
            print(f"  {i}. {seconds_to_hhmmss(s)}–{seconds_to_hhmmss(e)}  {t[:60]}")

    # hızlandırmaya göre zamanları ölçekle
    scaled: List[Tuple[float,float,str]] = []
    for s,e,t in caps:
        s = s / SPEED_FACTOR if SPEED_FACTOR else s
        e = e / SPEED_FACTOR if SPEED_FACTOR else e
        s = max(0, min(s, base.duration))
        e = max(0, min(e, base.duration))
        if e > s: scaled.append((s,e,t))
    print(f"[captions] Uygulanacak: {len(scaled)}")

    # metin klipleri
    overlays = []
    for s,e,txt in scaled:
        dur = max(0.05, e - s)
        box = render_text_image(
            text=txt, width_px=max_w, font_size=font_px,
            text_color=TEXT_COLOR, stroke_w=stroke_px,
            draw_box=DRAW_BOX, bg_color=BG_COLOR
        )
        overlays.append(pil_to_imageclip(box, s, dur, W,H, POS_MODE, MARGIN_PX))

    # video kompozit
    final = CompositeVideoClip([base, *overlays], size=(W,H))

    # --- BGM ---
    try:
        if os.path.isfile(BGM_FILE):
            print(f"[audio] BGM bulundu: {BGM_FILE}")
            bgm = AudioFileClip(BGM_FILE)
            # pencere ayarla
            s0 = BGM_START_S or 0.0
            e0 = BGM_END_S   or bgm.duration
            s0 = max(0.0, min(float(s0), bgm.duration))
            e0 = max(0.0, min(float(e0), bgm.duration))
            if e0 <= s0: e0 = bgm.duration
            bgm = bgm.subclip(s0, e0)

            # final süreye göre loop/kısalt
            if bgm.duration < final.duration:
                bgm = audio_loop(bgm, duration=final.duration)
            else:
                bgm = bgm.subclip(0, final.duration)

            bgm = bgm.volumex(MUSIC_VOL)

            if MUTE_ORIGINAL or (final.audio is None):
                final = final.set_audio(bgm)
            else:
                final = final.set_audio(CompositeAudioClip([final.audio, bgm]))
        else:
            print(f"[audio][WARN] BGM yok: {BGM_FILE} (sadece orijinal ses)")
    except Exception as e:
        print(f"[audio][WARN] BGM uygulanamadı: {e}")

    # yaz
    fps_out = int(round(getattr(base, "fps", 30) or 30))
    print(f"[write] {OUTPUT_VIDEO}  (fps={fps_out})")
    final.write_videofile(
        OUTPUT_VIDEO,
        codec="libx264",
        audio=True,
        audio_codec="aac",
        fps=fps_out,
        threads=4,
        preset="medium",
        temp_audiofile=os.path.join(ROOT_DIR, "temp_audio.m4a"),
        remove_temp=True,
        logger=_LOGGER
    )
    print("✅ Bitti")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback; traceback.print_exc()
        input("\nERROR yakalandı. Enter...")




