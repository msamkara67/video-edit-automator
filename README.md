# video-edit-automator

Python + MoviePy ile videolara zamanlı altyazı (captions) ve arka plan müziği ekleyen, Windows `.bat` dosyasıyla yönetilen küçük araç.

## ✨ Özellikler
- Zaman aralığına göre ekrana yerleşen büyük yazılar (center/top/bottom)
- Arka plan müziği: başlangıç/bitiş penceresi, fade-in/out
- Hızlandırma (speed factor)
- Tek noktadan yönetim: `video_edit.bat`

---

## ⚙️ Gereksinimler
- Windows + Python 3.9+ (pip çalışır halde)
- FFmpeg (MoviePy otomatik indirebilir; kurumsal ağlarda engel olabilir)
- Paketler:
  ```bash
  pip install -r requirements.txt

🚀 Hızlı Başlangıç

Bu projeyi indir ya da Git ile klonla.

Düzenlemek istediğin videoyu proje klasörüne kopyala (ör. MySource.mp4).

video_edit.bat dosyasını Not Defteri ile aç ve aşağıdaki değişkenleri ayarla:

set "ROOT_DIR=C:\...\video_editing"   :: proje klasörü
set "INPUT_VIDEO=MySource.mp4"        :: kaynak video
set "OUTPUT_VIDEO=MyResult.mp4"       :: çıktı video
set "BGM_FILE=bgm.wav"                :: arka plan müziği (isteğe bağlı)
set "SPEED_FACTOR=4"                  :: 1 = normal hız
set "MUTE_ORIGINAL=true"              :: videodaki orijinal sesi kapat

set "BGM_START=0.0"                   :: müzik başlangıcı (saniye)
set "BGM_END=0.0"                     :: 0 = videonun sonuna kadar

:: Başlıkların başlangıç/bitiş zamanı (saniye) ve yazısı: start|end|text
set "CAPTIONS=0|10|User enters the date.;15|88|Fetch daily coin metrics from the Binance API → template workbook.;88|110|Transfer data → main workbook.;111|128|Convert to presentation workbook + add VBA to update charts.;129|135|Open the presentation workbook.;136|166|Dynamic indicator charts per coin (powered by Binance API).;167|176|Virtual investing simulation page.;177|187|Per-coin indicator table for filtering signals."


video_edit.bat’e çift tıkla (veya cmd içinde çalıştır).

Not: Zamanlar orijinal videoya göredir; hızlandırma (örn. x4) uygulansa da içeride doğru ölçeklenir.

🧩 Parametre Özeti
Değişken	Açıklama
ROOT_DIR	Proje klasörü (tam yol)
INPUT_VIDEO	Kaynak video dosyası
OUTPUT_VIDEO	Çıkış video
BGM_FILE	Arka plan müziği (boş bırakılabilir)
SPEED_FACTOR	1, 2, 4…
MUTE_ORIGINAL	true/false – orijinal sesi kapat
BGM_START	Müziğin videoda başlayacağı zaman (sn)
BGM_END	Müziğin biteceği zaman (sn). 0 = videonun sonu
CAPTIONS	`start
🛠 Sorun Giderme

BGM bulunamadı: BGM_FILE yolunu ve dosya adını kontrol et.

Unicode/Türkçe karakter sorunu: Komut penceresi başına chcp 65001 kullanabilirsin.

“The handle is invalid”: Komut penceresini yönetici olmadan normal açıp çalıştırmayı dene.

FFmpeg bulunamıyor: imageio-ffmpeg indirilmesini engelleyen kurumsal proxy olabilir; FFmpeg’i PATH’e ekle.

📝 Lisans

MIT


### Küçük ek öneriler
- README’ye bir **ekran görüntüsü / GIF** ekle (çıktı örneği).
- Üst başa kısa **İngilizce özet** ekleyebilirsin (uluslararası görünürlük).
- Repo açıklamasına link: `pip install -r requirements.txt` ve `.bat` ile tek komutla çalışma vurgusu.

İstersen bu şablonu doğrudan README’ne yapıştırıp sadece kendi değerlerinle güncelle. Bu şekilde hem “preview” hem de “code” görünümünde okunması çok kolay olur.
::contentReference[oaicite:0]{index=0}

