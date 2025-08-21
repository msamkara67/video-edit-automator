video-edit-automator

Python + MoviePy ile zamana bağlı altyazılar ve arkaplan müziği ekleyen, Windows’ta .bat dosyasıyla ayarlanıp çalıştırılan küçük bir araç.

🔧 0) Gereksinimler (tek seferlik)

Windows + Python 3.9+ (kurulu olmalı)

Komut satırında pip çalışıyor olmalı

(İlk kurulum) Aşağıdaki komutla bağımlılıkları yükle:

pip install -r requirements.txt


MoviePy, gerekirse ffmpeg bileşenini otomatik indirir. Kurumsal ağda engel varsa ffmpeg.exe’yi PATH’e ekleyebilirsin.

⚡ 1) Hızlı Başlangıç (her video için)

Bu projeyi indirip çıkar ya da Git ile klonla.

Düzenlemek istediğin videoyu proje klasörüne kopyala (örn. MySource.mp4).

Kullanmak istiyorsan bir müzik dosyası koy (bgm.wav gibi).

video_edit.bat dosyasını Not Defteri ile aç ve üstteki değişkenleri ayarla:

set "ROOT_DIR=C:\...\video_editing"   :: proje klasörü
set "INPUT_VIDEO=MySource.mp4"        :: kaynak video
set "OUTPUT_VIDEO=MyResult.mp4"       :: çıkış video
set "BGM_FILE=bgm.wav"                :: müzik (opsiyonel)
set "SPEED_FACTOR=4"                  :: 1=normal, 4=4x hız
set "MUTE_ORIGINAL=true"              :: orijinal sesi kapat
set "BGM_START=0"                     :: müzik başlangıcı (sn)
set "BGM_END=0"                       :: 0 = videonun sonuna kadar


Aynı .bat dosyasının CAPTIONS bloğunda altyazılarını gir:

> "%ROOT_DIR%\_captions.tmp" (
  echo 0^|10^|User enters the date.
  echo 15^|88^|Fetch daily coin metrics from the Binance API -^> template workbook.
  echo 88^|110^|Transfer data -^> main workbook.
  echo 111^|128^|Convert to presentation workbook + add VBA to update charts.
  echo 129^|135^|Open the presentation workbook.
  echo 136^|166^|Dynamic indicator charts per coin (powered by Binance API).
  echo 167^|176^|Virtual investing simulation page.
  echo 177^|187^|Per-coin indicator table for filtering signals.
)


Sütun formatı: BAŞLANGIÇ|BİTİŞ|YAZI (saniye cinsinden)

Batch dosyasında | ve > karakterleri özel olduğu için ^ ile kaçırıyoruz: ^| ve ^>

Ok işareti → istiyorsan doğrudan yapıştırabilirsin; sorun çıkarsa -^> kullan.

.bat dosyasını çift tıkla çalıştır.
Çıktı dosyası: OUTPUT_VIDEO (örn. MyResult.mp4)

🧩 Altyazılar – ayrıntı

Zamanlar saniye cinsinden ondalıklı olabilir: 12.5^|18.2^|Text

Aynı anda birden fazla satır ekleyebilirsin; üst üste binerse sırayla gösterilir.

Yazı tipi boyutu video yüksekliğine göre otomatik ayarlanır (stroke/contour ile okunaklı).

🎵 Müzik penceresi

BGM_START ve BGM_END ile müziğin video içinde hangi aralıkta çalacağını belirleyebilirsin.

BGM_END=0 ⇒ videonun sonuna kadar

MUTE_ORIGINAL=true ⇒ orijinal video sesi kapatılır.

Ses seviyesi varsayılan ayarda; şiddet / fade sürelerini istersen koda parametre olarak ekleyebiliriz.

🐞 Sorun Giderme

BGM bulunamadı: BGM_FILE ismi/uzantısı doğru mu, aynı klasörde mi?

Türkçe karakterler bozuk: .bat içinde zaten chcp 65001 var; dosyayı UTF-8 olarak kaydettiğinden emin ol.

WinError 6 The handle is invalid: MoviePy/ffmpeg kapatma sırasında bazen görülür; çıktı video oluştuysa önemsemeyebilirsin.

Çok uzun metinler: Otomatik kaydırılır; yine de MAX_WIDTH_FR parametresiyle genişliği artırabiliriz.

📁 Dosya Yapısı
video-edit-automator/
├─ final_vid_edit.py      # asıl iş yapan Python betiği
├─ video_edit.bat         # hepsini düzenleyip çalıştırdığın Windows betiği
├─ requirements.txt       # tek seferlik bağımlılıklar
├─ LICENSE
└─ README.md

📜 Lisans

MIT

✅ Yol Haritası (isteğe bağlı)

Ses seviyesi / fade sürelerini .bat’tan ayarlanabilir yapmak

Yazı konumu (top/center/bottom) ve yazı kutusu stilleri

FFmpeg bulunamazsa otomatik uyarı
