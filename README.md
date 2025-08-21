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



