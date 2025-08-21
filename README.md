**Dosyalar:** [video_edit.bat](video_edit.bat) • [final_vid_edit.py](final_vid_edit.py) • [requirements.txt](requirements.txt)

## 🎬 Demo
[▶ Videoyu izle](https://github.com/msamkara67/video-edit-automator/releases/download/v0.1/MyResult.mp4)

## İndir

[![Release](https://img.shields.io/github/v/release/msamkara67/video-edit-automator?label=latest)](https://github.com/msamkara67/video-edit-automator/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/msamkara67/video-edit-automator/total.svg)](https://github.com/msamkara67/video-edit-automator/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![Download ZIP](https://img.shields.io/badge/Download-ZIP-blue?logo=github)](https://github.com/msamkara67/video-edit-automator/releases/latest/download/video-edit-automator.zip)


- **Son sürüm (önerilen)**:  
  [video-edit-automator.zip](https://github.com/msamkara67/video-edit-automator/releases/latest/download/video-edit-automator.zip)

- **Tüm sürümler**:  
  [Releases](https://github.com/msamkara67/video-edit-automator/releases)


Kurulum (bir defa yeterli):

```bash
pip install -r requirements.txt
```
---


## ⚡ Hızlı Başlangıç

1. Depoyu indir (ZIP) ya da Git ile klonla.
2. Kaynak videonu klasöre koy (örn. `MySource.mp4`). İstersen bir `bgm.wav` dosyası ekle.
3. `video_edit.bat` dosyasını **Not Defteri** ile aç; üstteki değişkenleri düzenle.
4. `.bat` dosyasını **çift tıkla** çalıştır.
5. Çıkış dosyası (`OUTPUT_VIDEO`) klasöre yazılır.
video_edit.bat

## .BAT Değişkenleri

| Değişken        | Açıklama                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `ROOT_DIR`      | Proje klasörü (örn. `C:\...\video_editing`)                               |
| `INPUT_VIDEO`   | Kaynak video adı (örn. `MySource.mp4`)                                    |
| `OUTPUT_VIDEO`  | Çıkış video adı (örn. `MyResult.mp4`)                                     |
| `BGM_FILE`      | Arka plan müziği (örn. `bgm.wav`) – boş bırakırsan müzik eklenmez         |
| `SPEED_FACTOR`  | Hız (1 = normal, 2 = 2x, 4 = 4x …)                                        |
| `MUTE_ORIGINAL` | `true` ⇒ orijinal videonun sesi kapalı; `false` ⇒ açık                   |
| `BGM_START_S`   | Müziğin karışmaya başlayacağı saniye (örn. `0.0`)                         |
| `BGM_END_S`     | Müziğin duracağı saniye. `None` yazarsan videonun sonuna kadar çalar      |



## Altyazı (Captions) Formatı

`.bat` dosyasında CAPTIONS bloğuna her satır şu şekilde yazılır:

0|10|User enters the date.
15|88|Fetch daily coin metrics from the Binance API → template workbook.
88|110|Transfer data → main workbook.
111|128|Convert to presentation workbook + add VBA to update charts.
129|135|Open the presentation workbook.
136|166|Dynamic indicator charts per coin (powered by Binance API).
167|176|Virtual investing simulation page.
177|187|Per-coin indicator table for filtering signals.

> Süreler **saniye** cinsindedir (tam sayı veya ondalık olabilir).

FFmpeg ile ilgili sorun yaşarsan:
```bash
pip install -U imageio-ffmpeg
```

### Ne yapman gerekiyor?
- README’deki başlıkların hizası bu yeni düzenle uyumlu kalsın.
- Kod bloklarının **üstünde** ve **sonunda** birer boş satır olsun.
- **Preview** ile kontrol et: tablo ve listeler düzgün hizalanıyor mu?


İstersen bir sonraki adımda “çıktı örneği” (küçük GIF veya ekran görüntüsü) ekleyip README’nin sonuna **Demo** bölümü de koyarız.
::contentReference[oaicite:0]{index=0}

**Lisans:** MIT — ayrıntılar için [LICENSE](LICENSE).


