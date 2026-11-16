# Application — Resmî Başvuru Rehberi

Dünya ülkelerindeki resmî kurumlara yapılan başvuruların (ehliyet, pasaport, iş izni vb.) şartlarını, adımlarını, geçerlilik koşullarını ve örnek belgelerini bir araya getiren prototip platform.

---

## 🛠️ Teknoloji Yığını

- **Backend:** Python 3.12+, Django 5.x
- **Veritabanı:** Supabase (PostgreSQL)
- **Depolama:** Supabase Storage (Private Bucket)
- **Ön Yüz:** Django Templates, saf HTML, CSS (Design Tokens), Vanilla JS
- **Statik Dosya Yönetimi:** WhiteNoise
- **Dağıtım (Deploy):** Vercel Serverless

---

## 🚀 Yerel Geliştirme Kurulumu

### 1. Sanal Ortamı Hazırlama
```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

### 2. Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

### 3. Ortam Değişkenleri (.env)
`.env.example` dosyasını `.env` olarak kopyalayın ve Supabase bilgilerinizi girin:
```bash
cp .env.example .env
```

`.env` içeriği:
```ini
SECRET_KEY=gizli-anahtariniz
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
DATABASE_URL=postgresql://postgres:[SIFRE]@db.[PROJE-REF].supabase.co:5432/postgres
SUPABASE_URL=https://[PROJE-REF].supabase.co
SUPABASE_SERVICE_ROLE_KEY=[SERVICE_ROLE_KEY]
SUPABASE_STORAGE_BUCKET=sample-documents
```

> **Önemli:** Proje doğrudan Supabase PostgreSQL veritabanına bağlanır; SQLite fallback bilerek kapalıdır.

### 4. Veritabanı Migration'larını Çalıştırma
```bash
python manage.py makemigrations accounts
python manage.py makemigrations
python manage.py migrate
```

### 5. Süper Kullanıcı (Admin) Oluşturma
```bash
python manage.py createsuperuser
```
E-posta, kullanıcı adı ve parola belirleyin.

### 6. Geliştirme Sunucusunu Başlatma
```bash
python manage.py runserver
```
Tarayıcınızda [http://localhost:8000/tr/](http://localhost:8000/tr/) adresine gidin.


---

## 👤 Kullanıcı & Üyelik Sistemi (Faz 4)

Kullanıcılar platforma e-posta, kullanıcı adı ve parola belirleyerek ücretsiz kayıt olabilirler.

- **Kayıt:** `/tr/accounts/register/` (E-posta küçük harfe normalize edilir; kullanıcı adı ve e-posta benzersizdir).
- **Giriş:** `/tr/accounts/login/` (Kullanıcı adı VEYA e-posta adresi + parola ile giriş yapılabilir).
- **Çıkış:** `/tr/accounts/logout/` (Güvenlik gereği yalnızca POST istekleri ile çalışır).
- **Açık Yönlendirme Koruması:** `?next=` parametresi yalnızca güvenli yerel adreslere yönlendirme yapar.

> **Gelecek Aşamalar İçin Not (Şimdilik Kapsam Dışı):**
> Prototip aşamasında basitliği korumak adına e-posta doğrulama (aktivasyon linki), parola sıfırlama (şifremi unuttum e-postası) ve sosyal medya ile giriş (Google OAuth vb.) bilinçli olarak kapsam dışı bırakılmıştır. Bu özellikler prototip sonrasında eklenecektir.

---

## 🔒 Erişim Kapısı ve Belge İndirme (Faz 5)

Platformda **Misafir** ve **Üye** kullanıcılar için içerik ayrımı sunucu tarafında (Server-side Access Gate) kesin çizgilerle uygulanır:

| İçerik / Özellik | Misafir | Üye |
|---|---|---|
| Başvuru başlığı, kurum adı, kısa özet (`summary`) | ✅ Açık | ✅ Açık |
| Detaylar (şartlar, belgeler, adımlar, harç/süre, notlar, kurum iletişim) | 🔒 Kilitli (HTML'e gönderilmez) | ✅ Tam Açık |
| Örnek belgelerin listesi ve başlığı | ✅ Açık | ✅ Açık |
| Örnek belge indirme | 🔒 Girişe Yönlendirilir | ✅ 60 sn İmzalı URL |

### 1. Sunucu Tarafı Güvenliği (Server-side Gate)
Misafir kullanıcılar başvuru detay sayfasını ziyaret ettiğinde, detay metinleri (`eligibility`, `required_documents`, `steps`, `fees_and_duration`, `validity`, `notes` ve kurum iletişim bilgileri) **HTML kaynağında (View Source) kesinlikle yer almaz**. Yalnızca kilitli çağrı kartı ve `?next=` parametresi ile dönüş bağlantıları oluşturulur.

### 2. Supabase Storage `sample-documents` Private Bucket Kurulumu
1. [Supabase Dashboard](https://supabase.com/dashboard)'a gidin ve projenizi seçin.
2. Sol menüden **Storage** sekmesine tıklayın.
3. **New Bucket** butonuna tıklayın:
   - **Name:** `sample-documents`
   - **Public Bucket:** **KAPALI (Unchecked)** tutun — bucket mutlaka **Private** olmalıdır.
4. **Save** butonuna basarak bucket'ı oluşturun.
5. `samples/` klasörü altına örnek dosyalarınızı yükleyin (örnek: `samples/tr_surucu_belgesi_dilekce_ornek.pdf`).
6. Django Admin panelinde (`/admin/catalog/sampledocument/`) `storage_path` alanına Supabase'e yüklediğiniz yolu girin (örnek: `samples/tr_surucu_belgesi_dilekce_ornek.pdf`).

### 3. Güvenli İmzalı URL (Signed URL) ile İndirme
- Belge indirme istekleri `/tr/documents/<id>/download/` uç noktasına yönlendirilir.
- Sadece oturum açmış kullanıcılar indirebilir (`@login_required`). Misafirler giriş sayfasına yönlendirilir (`/accounts/login/?next=...`).
- Sunucu tarafında `create_sample_document_signed_url` fonksiyonu çağrılarak Supabase Storage API üzerinden yalnızca **60 saniye** geçerli bir `signedURL` üretilir ve kullanıcı bu adrese HTTP 302 ile yönlendirilir.
- `service_role` anahtarı yalnızca sunucu tarafında (`.env`) saklanır, asla şablonlara veya JavaScript içerisine sızmaz.

---

## 🎨 Cilalama, SEO ve Erişilebilirlik (Faz 6)

Platform, kullanıcı deneyimi, arama motoru optimizasyonu ve web erişilebilirliği (a11y) standartlarına göre optimize edilmiştir:

### 1. SEO ve Arama Motoru Desteği
- **Dinamik Sitemap (`/sitemap.xml`):** Tüm yayınlanmış ülkeler, başvuru prosedürleri ve statik sayfalar, `tr`, `en`, `fr` dil varyasyonlarıyla otomatik listelenir.
- **Robots Kuralları (`/robots.txt`):** Arama motorlarına `/admin/`, `/accounts/` ve `/documents/` yollarını engeller; sitemap adresini bildirir.
- **Meta & Open Graph Etiketleri:** Her sayfada benzersiz `<title>`, `<meta name="description">`, `og:title`, `og:description`, `og:url` ve Twitter Card etiketleri yer alır.
- **Hreflang & Canonical:** Dil alternatifleri (`hreflang="tr"`, `"en"`, `"fr"`, `"x-default"`) ve `canonical` URL'ler otomatik üretilir.

### 2. Erişilebilirlik (a11y) ve Tasarım
- **Klavye ile Gezinme:** Ekran okuyucular ve klavye kullanıcıları için `Skip to Content` (İçeriğe Atla) linki mevcuttur. Odaklanan tüm öğelerde yüksek kontrastlı `focus-visible` çerçeveleri bulunur.
- **Anlamsal HTML & ARIA:** Form alanlarında `label` eşleşmeleri, accordion adımlarında `aria-expanded` nitelikleri ve semantik landmark (`role="main"`, `role="banner"`, `role="search"`) etiketleri kullanılmıştır.
- **Boş Durumlar (Empty States):** Henüz içeriği bulunmayan filtre veya aramalarda açıklayıcı ikon ve ana sayfaya dönüş yönlendirmesi içeren `.empty-state` bileşenleri gösterilir.
- **Hata Sayfaları (404 & 500):** Marka kimliğiyle uyumlu, arama çubuğu ve yönlendirme butonları içeren özel `404.html` ve `500.html` hata sayfaları mevcuttur.

### 3. Arayüz Çevirileri (i18n)
- Arayüz metinleri Türkçe (`tr`), İngilizce (`en`) ve Fransızca (`fr`) dillerinde GNU gettext standartlarına uygun olarak `.po` ve `.mo` dosyalarıyla yerelleştirilmiştir.
- Header'daki dil seçici üzerinden tek tıkla arayüz dili değiştirilebilir.
- Sayfa alt bilgisinde (footer) yasal sorumluluk reddi metni (`Disclaimer`) her dilde yer almaktadır.

### 4. Güvenlik ve Üretim Ayarları
- `DEBUG=False` modunda HTTPS yönlendirmesi (`SECURE_SSL_REDIRECT`), güvenli çerezler (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`), XSS ve Clickjacking koruması (`X_FRAME_OPTIONS = 'DENY'`) ve HSTS etkinleştirilir.
- **Sonraki Adım — Rate Limiting (Kapsam Dışı):** Prototip aşamasında harici redis veya ağır paketler eklenmemiştir. Üretim ortamında bot koruması ve brute-force saldırılarına karşı Cloudflare / Vercel Firewall kuralları veya `django-ratelimit` eklenmesi tavsiye edilir.

---

## 🚀 Vercel'e Dağıtım Rehberi (Faz 7)

Proje Vercel Serverless mimarisiyle ve WhiteNoise statik dosya yönetimiyle tam uyumlu olarak yapılandırılmıştır.

### 1. GitHub Bağlantısı ve Proje İçe Aktarma
1. [Vercel Dashboard](https://vercel.com/dashboard) adresine gidin ve oturum açın.
2. **Add New...** > **Project** butonuna tıklayın.
3. GitHub reponuzu bulun ve seçin: `mustafakan1980-spec/application` > **Import** butonuna tıklayın.

### 2. Ortam Değişkenlerini (Environment Variables) Tanımlama
Vercel proje oluşturma ekranında **Environment Variables** bölümünü açın ve aşağıdaki değişkenleri tek tek ekleyin:

| Değişken Adı | Örnek Değer / Açıklama |
|---|---|
| `SECRET_KEY` | Üretim için güçlü rastgele bir gizli anahtar |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.vercel.app` *(Otomatik eklenir, özel domain varsa virgülle ekleyin)* |
| `CSRF_TRUSTED_ORIGINS` | `https://*.vercel.app` *(Otomatik eklenir, özel domain varsa ekleyin)* |
| `DATABASE_URL` | Supabase Transaction Pooler URI: `postgresql://postgres.[REF]:[SIFRE]@aws-0-[REGION].pooler.supabase.com:6543/postgres` |
| `SUPABASE_URL` | `https://[REF].supabase.co` |
| `SUPABASE_ANON_KEY` | Supabase anon public key |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase service_role secret key *(Sunucuda imzalı indirme URL'i için)* |
| `SUPABASE_STORAGE_BUCKET` | `sample-documents` |

> ⚠️ **Önemli (Serverless Kuralı):** Veritabanı bağlantısı için doğrudan 5432 portu yerine Supabase Dashboard > **Project Settings** > **Database** > **Connection Pooling** altındaki **Transaction Pooler (Port 6543)** adresini kullanın. Django yapılandırmasında `conn_max_age=0` ve `disable_server_side_cursors=True` ayarlanmıştır.

### 3. Build & Dağıtım
- **Framework Preset:** `Other` (veya otomatik tespit edilen Django/Python)
- **Build Command:** Otomatik olarak `vercel.json` ve `build_files.sh` dosyaları çalışacaktır (`collectstatic` build sırasında yürütülür).
- **Deploy** butonuna tıklayın.

### 4. Canlıda Kontrol Listesi (Deployment Checklist)
Dağıtım tamamlandıktan sonra Vercel'in sağladığı canlı `.vercel.app` URL'inde şu adımları test edin:
- [ ] **Ana Sayfa:** Sayfa açılıyor mu, arama çubuğu ve ülke kartları yükleniyor mu?
- [ ] **Statik Dosyalar (CSS/JS/Font):** Tasarım ve renk paleti düzgün yükleniyor mu (`/static/css/tokens.css` ve `base.css`)?
- [ ] **Arayüz Dilleri:** Header'dan `TR`, `EN`, `FR` geçişleri sorunsuz çalışıyor mu?
- [ ] **Kayıt ve Giriş:** `/accounts/register/` ile yeni kullanıcı oluşturulabiliyor ve `/accounts/login/` ile giriş yapılabiliyor mu?
- [ ] **Misafir Kilit Mantığı:** Giriş yapılmadan bir başvuru detayına gidildiğinde kilitli kart çıkıyor mu; sayfa kaynağında (View Source) gizli detaylar görünmüyor mu?
- [ ] **Örnek Belge İndirme:** Üye girişi sonrası `/documents/<id>/download/` tıklandığında 60 saniyelik Supabase Signed URL'e yönlendirme yapılıyor mu?
- [ ] **Yönetim Paneli:** `/admin/` adresi açılıyor mu ve süper kullanıcı ile giriş yapılabiliyor mu?

---

## 📝 Deploy Notları & Çözülen Sorunlar

1. **Supabase Serverless Bağlantı Sayısı ve Pooler:**
   - Serverless lambda fonksiyonları eşzamanlı isteklerde hızla çoğalabildiğinden doğrudan 5432 portu yerine Supabase Transaction Mode Pooler (6543) tercih edilmiştir.
   - Transaction mode kullanırken Django'nun `disable_server_side_cursors=True` parametresi ayarlanarak olası "prepared statement does not exist" hataları engellenmiştir.

2. **Serverless Diske Kalıcı Yazma Kısıtı:**
   - Vercel Lambda ortamında yerel disk geçici (ephemeral) olduğundan, medya dosyaları ve kullanıcıya sunulan örnek başvuru belgeleri yerel disk yerine doğrudan **Supabase Storage** (Private bucket) üzerinden servis edilmiştir.

3. **Veritabanı Migration'ları:**
   - Migration komutları (`migrate`) Vercel build adımına bilinçli olarak **eklenmemiştir**; build adımlarının veritabanı kilitlerine yol açmaması için migration'lar yerel ortamdan canlı Supabase veritabanına uygulanmaktadır.

4. **WhiteNoise Statik Dosya Sıkıştırma:**
   - Vercel ortamında statik dosyaların eksiksiz ve en hızlı şekilde CDN üzerinden servis edilmesi için `whitenoise.storage.CompressedStaticFilesStorage` kullanılmıştır. Build esnasında `collectstatic --no-input --clear` çalıştırılmaktadır.

