# video-edit-automator

Python + MoviePy tabanlı küçük bir araç. Windows `.bat` dosyasıyla:
- videoya zamanlı altyazı (caption) ekler,
- arka plan müziği (BGM) karıştırır,
- hızlandırma ve başlangıç/bitiş ayarlarını tek yerden yönetir.

  ## Gereksinimler

- Windows + Python **3.9+**
- Komut satırında `pip` çalışıyor olmalı
- Kurulum (bir defa yeterli):
  ```bash
  pip install -r requirements.txt

**Commit message:** `README 2/6 – Gereksinimler`

---

## Adım 3 — Hızlı Başlangıç
**Nereye:** `README.md` (devamına ekle)

```markdown
## ⚡ Hızlı Başlangıç

1) Depoyu indir (ZIP) ya da Git ile klonla.  
2) Kaynak videonu klasöre koy (örn. `MySource.mp4`). İstersen bir `bgm.wav` dosyası ekle.  
3) `video_edit.bat` dosyasını Not Defteri ile aç, üstteki değişkenleri düzenle (aşağıda anlatılıyor).  
4) `.bat` dosyasını **çift tıkla** çalıştır.  
5) Çıkış dosyası (`OUTPUT_VIDEO`) klasöre yazılır.

## .BAT Değişkenleri

- `ROOT_DIR` : Proje klasörü (örn. `C:\...\video_editing`)
- `INPUT_VIDEO` : Kaynak video adı (örn. `MySource.mp4`)
- `OUTPUT_VIDEO`: Çıkış video adı (örn. `MyResult.mp4`)
- `BGM_FILE` : Arka plan müziği (örn. `bgm.wav`) – boş bırakırsan müzik eklenmez
- `SPEED_FACTOR` : Hız (1 = normal, 2 = 2x, 4 = 4x …)
- `MUTE_ORIGINAL` : `true` ⇒ orijinal videonun sesi kapalı; `false` ⇒ açık
- `BGM_START_S` / `BGM_END_S` : Müziğin videoya karışacağı saniye aralığı  
  (örn. `0.0` → `None` : baştan sona)

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





