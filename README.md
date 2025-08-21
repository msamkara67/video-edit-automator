Kurulum (bir defa yeterli):

```bash
pip install -r requirements.txt



---

### 2) Hızlı Başlangıç (numaralı liste)

```markdown
## ⚡ Hızlı Başlangıç

1. Depoyu indir (ZIP) ya da Git ile klonla.
2. Kaynak videonu klasöre koy (örn. `MySource.mp4`). İstersen bir `bgm.wav` dosyası ekle.
3. `video_edit.bat` dosyasını **Not Defteri** ile aç; üstteki değişkenleri düzenle.
4. `.bat` dosyasını **çift tıkla** çalıştır.
5. Çıkış dosyası (`OUTPUT_VIDEO`) klasöre yazılır.

## .BAT Değişkenleri

| Değişken        | Açıklama                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `ROOT_DIR`      | Proje klasörü (örn. `C:\...\video_editing`)                               |
| `INPUT_VIDEO`   | Kaynak video adı (örn. `MySource.mp4`)                                    |
| `OUTPUT_VIDEO`  | Çıkış video adı (örn. `MyResult.mp4`)                                     |
| `BGM_FILE`      | Arka plan müziği (örn. `bgm.wav`) – boş bırakırsan müzik eklenmez         |
| `SPEED_FACTOR`  | Hız (1 = normal, 2 = 2x, 4 = 4x …)                                        |
| `MUTE_ORIGINAL` | `true` ⇒ orijinal videonun sesi kapalı; `false` ⇒ açık                    |
| `BGM_START_S`   | Müziğin karışmaya başlayacağı saniye (örn. `0.0`)                         |
| `BGM_END_S`     | Müziğin duracağı saniye. `None` yazarsan videonun sonuna kadar çalar      |






