# video-edit-automator

Python + MoviePy tabanlı küçük bir araç. Windows `.bat` dosyasıyla:
- videoya zamanlı altyazı (caption) ekler,
- arka plan müziği (BGM) karıştırır,
- hızlandırma ve başlangıç/bitiş ayarlarını tek yerden yönetir.

---

## Gereksinimler

- Windows + Python **3.9+**
- Komut satırında `pip` çalışıyor olmalı
- Kurulum (bir defa yeterli):
  ```bash
  pip install -r requirements.txt
Not: imageio-ffmpeg gerektiğinde FFmpeg’i otomatik indirir. Kurumsal ağ engellerse VPN ya da yönetici ile ilerleyin.

⚡ Hızlı Başlangıç
Depoyu indir (ZIP) ya da Git ile klonla.

Kaynak videonu klasöre koy (örn. MySource.mp4). İstersen bir bgm.wav dosyası ekle.

video_edit.bat dosyasını Not Defteri ile aç, üstteki değişkenleri düzenle.

.bat dosyasını çift tıkla çalıştır.

Çıkış dosyası (OUTPUT_VIDEO) klasöre yazılır.

.BAT Değişkenleri (tek yerden kontrol)
Değişken	Açıklama
ROOT_DIR	Proje klasörü (örn. C:\...\video_editing)
INPUT_VIDEO	Kaynak video adı (örn. MySource.mp4)
OUTPUT_VIDEO	Çıkış video adı (örn. MyResult.mp4)
BGM_FILE	Arka plan müziği (örn. bgm.wav) – boş bırakırsan müzik eklenmez
SPEED_FACTOR	Hız (1 = normal, 2 = 2x, 4 = 4x …)
MUTE_ORIGINAL	true ⇒ orijinal videonun sesi kapalı; false ⇒ açık
BGM_START_S	Müziğin karışmaya başlayacağı saniye (örn. 0.0)
BGM_END_S	Müziğin duracağı saniye. None yazarsan videonun sonuna kadar çalar

Altyazı (Captions) Formatı
.bat dosyasında CAPTIONS bloğuna her satır şu şekilde yazılır:

Copy
Edit
başlangıç|bitiş|metin
Örnek:

sql
Copy
Edit
0|10|User enters the date.
15|88|Fetch daily coin metrics from the Binance API → template workbook.
88|110|Transfer data → main workbook.
111|128|Convert to presentation workbook + add VBA to update charts.
129|135|Open the presentation workbook.
136|166|Dynamic indicator charts per coin (powered by Binance API).
167|176|Virtual investing simulation page.
177|187|Per-coin indicator table for filtering signals.
Süreler saniye cinsindedir (tam sayı veya ondalık olabilir).

İpuçları ve Sorun Giderme
“BGM bulunamadı” uyarısı: BGM_FILE adı/konumu yanlış olabilir.

“The handle is invalid”: MoviePy işi bitirince görülebilen zararsız bir mesajdır. Çıkış dosyanız varsa sorun yok.

Ses yok: MUTE_ORIGINAL=true iken BGM de yoksa sessiz çıkar; MUTE_ORIGINAL=false yap ya da bgm.wav ekle.

FFmpeg indirme engeli: pip install -U imageio-ffmpeg deneyin; kurumsal ağ indirimi engelleyebilir.

Yazı boyutu/konum: Kodda font otomatik büyük ayarlanır; istersen FONT_SIZE_FR, POS_MODE gibi sabitleri değiştirebilirsin.

Lisans
MIT

pgsql
Copy
Edit

bunu yap, commit’le. sonra istersen küçük bir görsel/gif (örnek çıktı) ekleme adımına geçebiliriz.
::contentReference[oaicite:0]{index=0}







Sources

Ask ChatGPT




