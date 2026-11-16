# Application — Proje Planı ve Geliştirme Promptları

> Bu dosya Claude Code veya Antigravity içinde kullanılmak üzere hazırlandı.
> Projenin tamamını tek seferde yaptırma. **Fazları sırayla, her fazı ayrı bir görev olarak ver.**
> Her fazın sonunda "Kabul Kriterleri"ni kontrol et, sonra bir sonraki faza geç.

---

## 0. Bu Dosya Nasıl Kullanılır?

1. Boş bir klasör aç (`application/`), bu dosyayı `PLAN.md` adıyla köke koy.
2. **Bölüm 2 (Proje Kuralları)** kısmını Claude Code için `CLAUDE.md`, Antigravity için `AGENTS.md` (veya kural/rules dosyası) olarak kaydet. Böylece ajan her görevde kuralları hatırlar.
3. Her faz için ajana şunu söyle:
   > "PLAN.md dosyasını oku. Sadece **Faz X**'i uygula. Diğer fazlara dokunma. Bitince kabul kriterlerini tek tek kontrol edip rapor ver."
4. Faz bitince çalıştır, tarayıcıda dene, `git commit` at, sonra sonraki faza geç.

---

## 1. Proje Özeti

**Proje adı:** Application

**Amaç:** Dünya ülkelerindeki resmî kurumlara yapılan başvuruların (ehliyet, pasaport, iş izni, belge vb.) şartlarını, başvuru adımlarını, geçerlilik koşullarını, başvurulacak kurum ve iletişim bilgilerini ve **örnek belgeleri** tek bir sitede toplamak.

**Örnek sayfa:** "Senegal'de ehliyet almak için ne yapmalıyım?"
→ Kim başvurabilir, hangi şartlarda geçerli, hangi belgeler gerekli, ücret/süre, nereye başvurulur, kurum iletişim bilgileri, örnek belge (indirilebilir) — A'dan Z'ye tek sayfa.

**Dil:** Her ülkenin sayfaları, o ülkenin **kendi resmî dil(ler)inde** hazırlanır (Senegal → Fransızca, Türkiye → Türkçe vb.). Arayüz metinleri de çok dillidir.

**Önemli ilkeler:**
- **Takip mekanizması YOK.** Kullanıcı başvurusunu sitede takip etmez, "başvurularım" paneli yoktur.
- Her kullanıcı platformdaki tüm başvuru şartlarını ve örnek belgeleri görebilir (kullanıcıya özel içerik yok).
- Üye olmadan: içerik **özet düzeyinde** görüntülenir.
- Üye olunca: **tam detay** ve **belge indirme** açılır.
- İlk hedef **prototip**. Basit tut. Aşırı mühendislik yapma.

---

## 2. Proje Kuralları (CLAUDE.md / AGENTS.md olarak kaydet)

```markdown
# Application — Ajan Kuralları

- Dil: Kod ve değişken adları İngilizce; kullanıcıya yazdığın açıklamalar ve rapor **Türkçe**.
- Bu bir PROTOTİP. En basit çalışan çözümü seç. Gereksiz kütüphane, katman, soyutlama ekleme.
- Teknoloji: Python 3.12, Django (son kararlı sürüm), Supabase (sadece PostgreSQL + Storage), Vercel (deployment).
- Front end: Ayrı framework YOK (React/Vue/Tailwind/Bootstrap yok). Django template + saf HTML, CSS, JavaScript. Hepsi aynı repoda.
- Django'nun yerleşik auth sistemini kullan (Supabase Auth KULLANMA). Supabase sadece veritabanı ve dosya depolama.
- Sadece istenen fazı uygula. Sonraki fazların işini önceden yapma.
- Her faz sonunda: çalıştır, hataları düzelt, kabul kriterlerini tek tek kontrol et, kısa Türkçe rapor yaz.
- Gizli anahtarları ASLA koda yazma; `.env` kullan, `.env.example` güncel tut, `.env` dosyasını `.gitignore`'a ekle.
- Supabase `service_role` anahtarı yalnızca sunucu tarafında kullanılır; asla template/JS içine sızmaz.
- Büyük kararlar (yeni paket, model değişikliği) için önce kısa gerekçe yaz.
- Erişilebilirlik: anlamsal HTML, alt metinler, yeterli renk kontrastı, mobil uyumlu (mobile-first).
```

---

## 3. Teknoloji Yığını

| Katman | Seçim | Not |
|---|---|---|
| Backend | Python + Django | Server-side render (template) |
| Veritabanı | Supabase (PostgreSQL) | Django, Supabase Postgres'e doğrudan bağlanır |
| Dosya depolama | Supabase Storage (private bucket) | Örnek belgeler burada; indirme **signed URL** ile |
| Auth | Django auth | Özel User modeli: e-posta + kullanıcı adı + parola |
| Front end | HTML + CSS + vanilla JS | Django template içinde, ayrı framework yok |
| Statik dosyalar | WhiteNoise | Vercel'de statik servis için |
| Deployment | Vercel | Python/Django serverless |
| Çoklu dil | Django i18n (arayüz) + çeviri tabloları (içerik) | Bölüm 6 |

**Python paketleri (başlangıç):** `django`, `psycopg[binary]`, `dj-database-url`, `python-dotenv`, `whitenoise`, `supabase` (Storage için).
Başka paket gerekirse önce gerekçesini yaz.

**Ortam değişkenleri (`.env.example`):**

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=
DATABASE_URL=            # Supabase Postgres bağlantı adresi (Vercel için pooler adresi)
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
SUPABASE_STORAGE_BUCKET=sample-documents
```

---

## 4. Klasör Yapısı (hedef)

```
application/
├── PLAN.md
├── CLAUDE.md / AGENTS.md
├── manage.py
├── requirements.txt
├── vercel.json
├── .env.example
├── .gitignore
├── config/                  # Django proje ayarları (settings, urls, wsgi)
├── accounts/                # Kullanıcı modeli, kayıt/giriş/çıkış
├── catalog/                 # Ülke, kurum, başvuru, belge modelleri ve sayfaları
├── core/                    # Ana sayfa, ortak yardımcılar
├── templates/               # base.html + uygulama şablonları
├── static/
│   ├── css/                 # tokens.css, base.css, components.css
│   ├── js/                  # main.js (küçük etkileşimler)
│   └── img/
└── locale/                  # Arayüz çevirileri (tr, en, fr)
```

---

## 5. Veri Modeli

Mantık: **Ülke → Kurum → Başvuru (procedure)**. Başvurunun metinleri **çeviri tablosunda**, her dil için ayrı satır.

### 5.1 Tablolar

**Language**
- `code` (örn. `tr`, `fr`, `en`, `ar`), `name_native` (Türkçe, Français…), `is_rtl` (bool)

**Country**
- `iso2` (SN, TR…), `slug`, `flag_emoji`, `is_published`
- `official_languages` (ManyToMany → Language), `primary_language` (FK → Language)
- `CountryTranslation`: `country`, `language`, `name`

**Institution** (resmî kurum)
- `country` (FK), `website`, `phone`, `email`, `address`, `map_url` (opsiyonel)
- `InstitutionTranslation`: `institution`, `language`, `name`, `address_text`, `working_hours`

**Category** (ehliyet, pasaport, iş izni, vergi, eğitim…)
- `slug`, `icon` (emoji), `order`
- `CategoryTranslation`: `category`, `language`, `name`

**Procedure** (başvuru)
- `country` (FK), `institution` (FK), `category` (FK), `slug`, `is_published`, `updated_at`
- `last_verified_at` (içerik en son ne zaman doğrulandı), `official_source_url`
- `ProcedureTranslation`: `procedure`, `language`, `title`, `summary` (kısa, herkese açık),
  `eligibility` (kimler başvurabilir / geçerlilik şartları),
  `required_documents` (gerekli belgeler),
  `steps` (başvuru adımları),
  `fees_and_duration` (ücret ve süre),
  `validity` (geçerlilik süresi/koşulları),
  `notes` (ek notlar)
  *(Prototipte alanlar düz metin/markdown benzeri satır listesi olabilir; basit tut.)*

**SampleDocument** (örnek belge)
- `procedure` (FK), `storage_path` (Supabase Storage yolu), `file_type`, `order`
- `SampleDocumentTranslation`: `document`, `language`, `title`, `description`

**User** (accounts, `AbstractUser`'dan türet — **proje başında** `AUTH_USER_MODEL` olarak ayarla)
- `email` (unique, zorunlu), `username` (unique, zorunlu), `password`
- Giriş: **e-posta veya kullanıcı adı** + parola ile

### 5.2 Notlar
- Takip/başvuru geçmişi/favori tablosu **yapma**.
- Güvenlik için Supabase'de tüm tablolarda RLS'i **aç** (politika ekleme). Veriye yalnızca Django erişir; Supabase'in otomatik REST API'si tablolara açılmamalı.
- Tüm içerik yönetimi **Django Admin** üzerinden yapılır (prototipte ayrı yönetim paneli yok).

---

## 6. Çoklu Dil Stratejisi

- **Arayüz dili** (menüler, butonlar): Django i18n. Prototipte `tr`, `en`, `fr`.
- **URL yapısı:** `i18n_patterns` ile dil öneki → `/fr/countries/sn/`, `/tr/countries/tr/`
- **İçerik dili:** Bir başvuru sayfası açıldığında içerik, ülkenin **resmî dilinde** gösterilir. Kullanıcı arayüz dilini değiştirse bile, ülke içeriği için sayfada ayrı bir **"İçerik dili"** seçici bulunur (o ülkenin resmî dilleri + varsa İngilizce).
- **Fallback:** İstenen dilde çeviri yoksa ülkenin `primary_language` içeriği gösterilir ve üstte küçük bir bilgi etiketi çıkar ("Bu içerik şu dilde gösteriliyor: Français").
- RTL diller (Arapça) için `dir="rtl"` desteği veri modelinde hazır olsun (`is_rtl`); prototipte tam RTL tasarımı zorunlu değil.

---

## 7. Erişim Kuralları (Misafir vs Üye)

| İçerik | Misafir | Üye |
|---|---|---|
| Ana sayfa, ülke listesi, kategori listesi | ✅ | ✅ |
| Başvuru kartı: başlık, kurum adı, kısa özet (`summary`) | ✅ | ✅ |
| Başvuru **detayı** (şartlar, belgeler, adımlar, ücret, süre, geçerlilik, notlar, kurum iletişim bilgisi) | 🔒 kilitli | ✅ |
| Örnek belgelerin **listesi** (başlık görünür) | ✅ | ✅ |
| Örnek belge **indirme** | 🔒 | ✅ |

Misafir, kilitli bölümleri görmeye çalışınca: bulanık/kısaltılmış önizleme + **"Detayları görmek için ücretsiz üye ol"** çağrı kartı (kayıt ve giriş butonları, `?next=` ile geri dönüş).
Bu kuralları tek bir yerde (örn. şablon etiketi veya view dekoratörü) topla; her view'da tekrar yazma.

---

## 8. Arayüz / Tasarım Rehberi

**Genel his:** Gençlere hitap eden, ferah, neşeli, güven veren. Açık arka plan + canlı renklerin tonları. Sade, boşluklu, yuvarlak köşeli.

**Renk paleti (CSS değişkenleri olarak `tokens.css` içinde):**

| Rol | Renk | Ton |
|---|---|---|
| Arka plan | `#FAFAFF` | çok açık lavanta-beyaz |
| Yüzey (kart) | `#FFFFFF` | |
| Ana renk | `#6C5CE7` | canlı mor — tonları: `#EFEDFD`, `#CFC9F7`, `#4B3FC2` |
| İkincil | `#00C2A8` | canlı turkuaz — tonları: `#E0F8F4`, `#7FE3D3` |
| Vurgu 1 | `#FF6B6B` | mercan — tonları: `#FFEAEA` |
| Vurgu 2 | `#FFC857` | sarı — tonları: `#FFF5DB` |
| Metin | `#1F1B3A` | koyu lacivert-mor |
| Soluk metin | `#6B6889` | |

**Tipografi:** Google Fonts'tan `Plus Jakarta Sans` (başlıklar kalın, gövde normal). Fallback: `system-ui, sans-serif`.

**Bileşenler:** 20–24px yuvarlak kartlar, hafif renkli gölge, hap (pill) şeklinde butonlar, ülke bayrağı emojileri, kategori için emoji ikonlar, rozetler (ör. "🔒 Üyelere özel", "✅ Doğrulandı: 12.11.2026").

**Sayfa düzeni (mobile-first):**
- Üst menü: logo, arama kutusu, dil seçici, Giriş / Üye Ol.
- Ana sayfa: büyük başlık + arama + popüler ülkeler (bayraklı kartlar) + kategoriler.
- Ülke sayfası: o ülkenin kategorileri ve başvuruları.
- Başvuru sayfası: başlık, kurum, rozetler, kısa özet; altında bölümler (şartlar, belgeler, adımlar, ücret/süre, geçerlilik); yan/alt kartta kurum iletişim bilgileri; örnek belgeler kartı.
- Alt bilgi (footer): sorumluluk reddi (Bölüm 12).

**Etkileşimler (küçük JS):** mobil menü, dil seçici, adımlar için açılır/kapanır akordeon, basit arama filtresi, kilitli içerik kartı.

---

## 9. FAZLAR

> Her faz için: **Hedef → Prompt → Kabul Kriterleri**.
> Prompt kutusunu ajana olduğu gibi yapıştırabilirsin.

---

### FAZ 1 — İskelet ve Ortam

**Hedef:** Çalışan boş bir Django projesi, ayarlar, kullanıcı modeli, tasarım temeli.

**Prompt:**
```
PLAN.md ve CLAUDE.md/AGENTS.md dosyalarını oku. Sadece FAZ 1'i uygula.

1. Python sanal ortamı ve requirements.txt oluştur (django, psycopg[binary], dj-database-url, python-dotenv, whitenoise, supabase).
2. `config` adında Django projesi oluştur; `accounts`, `catalog`, `core` uygulamalarını ekle.
3. accounts içinde AbstractUser'dan türeyen özel User modeli yaz (e-posta unique ve zorunlu, username unique ve zorunlu). AUTH_USER_MODEL'i İLK migration'dan önce ayarla.
4. settings.py: .env'den oku (SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASE_URL), dj-database-url ile veritabanı, WhiteNoise, STATIC ayarları, i18n (LANGUAGES: tr, en, fr; LOCALE_PATHS), TEMPLATES içinde proje seviyesinde templates klasörü.
5. Geliştirme için SQLite fallback KOYMA; DATABASE_URL zorunlu olsun (Supabase Postgres'e bağlan). Bağlantı yoksa anlaşılır hata ver.
6. templates/base.html: Türkçe/çok dilli uyumlu iskelet (header, main, footer), static/css/tokens.css (PLAN.md Bölüm 8 renkleri ve fontu), base.css.
7. core: basit bir ana sayfa view'ı ve şablonu ("Application" başlığı, yer tutucu içerik).
8. .env.example, .gitignore, README.md (kurulum adımları, kısa) oluştur.
9. migrate çalıştır, superuser oluşturma talimatını README'ye yaz, runserver ile doğrula.
```

**Kabul Kriterleri:**
- [ ] `python manage.py runserver` ile ana sayfa açılıyor.
- [ ] Migration'lar Supabase Postgres'e uygulanmış, `accounts_user` tablosu orada görünüyor.
- [ ] `.env` git'e girmiyor, `.env.example` var.
- [ ] Renk/font değişkenleri `tokens.css`'te.

---

### FAZ 2 — Veri Modeli, Admin ve Örnek Veri

**Hedef:** Bölüm 5'teki modeller, Django Admin'den içerik girişi, test için örnek veri.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 2'yi uygula.

1. catalog uygulamasında PLAN.md Bölüm 5'teki modelleri yaz: Language, Country(+Translation), Institution(+Translation), Category(+Translation), Procedure(+Translation), SampleDocument(+Translation). Takip/favori/başvuru geçmişi modeli YAZMA.
2. Çeviri modelleri için (parent, language) çifti unique olsun.
3. Admin: her ana modelde çeviri satırlarını inline göster; list_display, search_fields, list_filter ekle. Procedure admin'inde ülke/kategori/yayın durumu filtreleri olsun.
4. Bir management command yaz: `python manage.py seed_demo` — tekrar çalıştırılabilir (idempotent) olsun. İçerik:
   - Diller: tr, en, fr
   - Ülkeler: Senegal (resmî dil: fr), Türkiye (tr), Birleşik Krallık (en)
   - Kategoriler: Ehliyet, Pasaport, Çalışma/İş İzni
   - Her ülke için en az 1 kurum ve 1–2 başvuru; her başvurunun KENDİ ülkesinin resmî dilinde çevirisi (Senegal ehliyeti Fransızca).
   - ÖNEMLİ: Bunlar TAMAMEN ÖRNEK/ŞABLON veridir. Gerçek ücret, adres, telefon gibi doğrulanmamış bilgileri uydurma; belirsiz alanları açıkça "[Örnek veri — doğrulanmadı]" diye işaretle. Kesin olmayan hiçbir bilgiyi gerçekmiş gibi yazma.
5. Migration'ları üret ve uygula; admin'e giriş yapıp verilerin göründüğünü doğrula.
```

**Kabul Kriterleri:**
- [ ] `seed_demo` iki kez çalıştırılınca çift kayıt oluşmuyor.
- [ ] Admin'den yeni ülke + başvuru + çeviri eklenebiliyor.
- [ ] Örnek veride "doğrulanmadı" etiketleri var, uydurma resmî bilgi yok.

---

### FAZ 3 — Herkese Açık Sayfalar (Misafir Görünümü)

**Hedef:** Ana sayfa, ülke listesi, ülke sayfası, kategori, başvuru sayfası (özet düzeyi), arama.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 3'ü uygula. Giriş/kayıt henüz yok; herkes misafir kabul edilir.

1. URL'ler (i18n_patterns ile dil önekli):
   - /            ana sayfa (arama, popüler ülkeler, kategoriler)
   - /countries/                 ülke listesi
   - /countries/<iso2>/          ülke sayfası (kategorilere göre başvurular)
   - /p/<slug>/                  başvuru sayfası
   - /search/?q=                 basit arama (başvuru başlığı, ülke adı, kategori adı üzerinde, istenen dilde)
2. İçerik dili mantığı: PLAN.md Bölüm 6. Başvuru/ülke içeriğini ülkenin resmî dilinde göster; içerik dili seçici ekle; çeviri yoksa primary_language'e düş ve bilgi etiketi göster. Bunu tek bir yardımcı fonksiyonda topla.
3. Başvuru sayfasında şimdilik: başlık, kurum adı, kategori rozeti, kısa özet (summary), "Son doğrulama" tarihi, örnek belgelerin başlık listesi. Detay bölümlerini (şartlar, belgeler, adımlar vb.) HENÜZ gösterme; yerine "🔒 Detaylar için üye ol" yer tutucu kartı koy (butonlar henüz çalışmasa da olur).
4. Tasarım: PLAN.md Bölüm 8'e uygun; mobile-first; kartlar, bayrak emojileri, kategori emojileri, hover efektleri; küçük JS ile mobil menü ve dil seçici.
5. Footer'a sorumluluk reddi metni ekle (PLAN.md Bölüm 12).
6. N+1 sorgu olmasın (select_related / prefetch_related kullan).
```

**Kabul Kriterleri:**
- [ ] Ana sayfadan ülkeye, ülkeden başvuruya gidilebiliyor.
- [ ] Senegal ehliyeti Fransızca gösteriliyor; dil seçiciyle çeviri olan dillere geçilebiliyor.
- [ ] Olmayan çeviri için fallback + bilgi etiketi çalışıyor.
- [ ] Arama sonuç döndürüyor. Mobilde düzgün görünüyor.

---

### FAZ 4 — Üyelik (Kayıt / Giriş / Çıkış)

**Hedef:** E-posta + kullanıcı adı + parola ile kayıt; giriş; çıkış.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 4'ü uygula.

1. accounts içinde:
   - Kayıt formu: e-posta, kullanıcı adı, parola, parola tekrar. E-posta ve kullanıcı adı benzersiz olmalı (e-posta küçük harfe normalize edilsin, kullanıcı adı büyük/küçük harf duyarsız benzersiz olsun). Django'nun parola doğrulayıcılarını kullan.
   - Giriş: "e-posta veya kullanıcı adı" + parola. Custom authentication backend yaz.
   - Çıkış: POST ile.
   - `?next=` parametresi ile geri dönüş (açık yönlendirme açığı olmasın: url_has_allowed_host_and_scheme kullan).
2. Sayfalar: /accounts/register/, /accounts/login/, /accounts/logout/. Tasarım PLAN.md Bölüm 8'e uygun, form hataları Türkçe/çok dilli ve anlaşılır, parola göster/gizle için küçük JS.
3. Header'da: misafire "Giriş" ve "Üye Ol"; üyeye kullanıcı adı ve "Çıkış".
4. E-posta doğrulama, parola sıfırlama, sosyal giriş bu fazda YOK (sonraki aşamaya notu README'ye yaz).
5. Basit testler: kayıt, tekrarlı e-posta/kullanıcı adı reddi, e-posta ile giriş, kullanıcı adı ile giriş.
```

**Kabul Kriterleri:**
- [ ] Kayıt olunup giriş yapılabiliyor (hem e-posta hem kullanıcı adıyla).
- [ ] Aynı e-posta/kullanıcı adı ikinci kez alınamıyor.
- [ ] Testler geçiyor.

---

### FAZ 5 — Erişim Kapısı ve Belge İndirme

**Hedef:** Misafir/üye ayrımı, tam detay, Supabase Storage'dan güvenli indirme.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 5'i uygula.

1. PLAN.md Bölüm 7'deki erişim kurallarını TEK bir yerde topla (örn. şablon bağlamında `can_view_details` değişkeni veya yardımcı fonksiyon). 
2. Başvuru sayfası:
   - Üye ise: tüm detay bölümleri (şartlar/geçerlilik, gerekli belgeler, adımlar, ücret ve süre, notlar, kurum iletişim kartı) görünür; adımlar akordeon olabilir.
   - Misafir ise: detay bölümlerinin İÇERİĞİ SUNUCUDAN HİÇ GÖNDERİLMESİN (sadece CSS ile gizleme/bulanıklaştırma yapma). Bunun yerine her bölüm için kilitli yer tutucu ve "Ücretsiz üye ol / Giriş yap" kartı göster (next ile dönüş).
3. Örnek belge indirme: /documents/<id>/download/ — sadece giriş yapmış kullanıcılar; misafir giriş sayfasına yönlendirilsin. View, Supabase Storage'daki private bucket'tan kısa ömürlü (örn. 60 sn) signed URL üretip yönlendirsin. service_role anahtarı yalnızca sunucuda.
4. Supabase tarafı: `sample-documents` adında PRIVATE bucket oluşturma adımlarını README'ye yaz. Admin'den dosya yükleme için en basit çözümü seç (örn. admin'de storage_path alanına elle yol girmek + README'de Supabase panelinden yükleme talimatı). İstersen admin'de yükleme alanı ekleyebilirsin ama basit tut.
5. Örnek belge dosyalarını depoya KOYMA; seed için 1–2 sahte örnek PDF'i Storage'a nasıl yükleyeceğimi README'de anlat.
6. Testler: misafir detay içeriğini HTML'de göremiyor; üye görüyor; misafir indirme linkinde yönlendiriliyor; üye indirmede signed URL'e yönlendiriliyor (Storage çağrısını mock'la).
```

**Kabul Kriterleri:**
- [ ] Misafir olarak sayfa kaynağında (View Source) detay metinleri YOK.
- [ ] Üye girişi sonrası tüm detaylar ve indirme çalışıyor.
- [ ] Dosyalar herkese açık bucket'ta DEĞİL; link kısa sürede geçersiz oluyor.

---

### FAZ 6 — Cilalama ve Kalite

**Hedef:** Tasarımı parlatmak, SEO ve erişilebilirlik temeli, boş durumlar, hata sayfaları.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 6'yı uygula.

1. Tasarım cilası: tutarlı boşluklar, hover/focus durumları, yükleme/boş durum ekranları ("Bu ülkede henüz başvuru yok"), animasyonlar çok hafif (CSS transition). Kontrastları kontrol et.
2. 404 ve 500 sayfaları (marka diliyle, ana sayfaya dönüş butonu).
3. SEO temeli: her sayfada anlamlı <title> ve meta description; Open Graph etiketleri; sitemap.xml (yayınlanmış ülkeler ve başvurular, dil alternatifleriyle) ve robots.txt; hreflang.
4. Erişilebilirlik: klavye ile gezilebilirlik, aria etiketleri, form label'ları, alt metinler.
5. Arayüz çevirilerini tamamla (tr, en, fr): makemessages / compilemessages. Hard-coded metin kalmasın.
6. Basit güvenlik gözden geçirmesi: DEBUG=False ayarında güvenli çerez bayrakları, CSRF, HSTS (üretimde), rate limit gerekmiyor ama README'ye "sonraki adım" olarak yaz.
7. Kod temizliği: kullanılmayan dosya/kod sil; README'yi güncelle.
```

**Kabul Kriterleri:**
- [ ] Lighthouse (mobil) erişilebilirlik ve SEO skorları makul (≥ 90 hedef).
- [ ] 404 sayfası marka diliyle çıkıyor.
- [ ] Hard-coded Türkçe/İngilizce/Fransızca metin kalmamış.

---

### FAZ 7 — Vercel'e Deploy

**Hedef:** Prototipi canlıya almak.

**Prompt:**
```
PLAN.md'yi oku. Sadece FAZ 7'yi uygula.

Önce Vercel'in GÜNCEL Django/Python dağıtım dokümantasyonunu kontrol et (yapılandırma biçimi değişmiş olabilir) ve ona göre ilerle. Hedefler:

1. Vercel'de çalışacak yapılandırmayı hazırla (vercel.json ve/veya gerekli giriş noktası; Django wsgi uygulaması `app` olarak dışa açılmalı). WhiteNoise ile statik dosyalar servis edilsin; collectstatic build adımında çalışsın.
2. Serverless kısıtlarını gözet:
   - Diske kalıcı yazma YOK (medya/yükleme yerel diske yazılmaz; dosyalar Supabase Storage'da).
   - Veritabanı bağlantısı: Supabase'in connection POOLER (transaction mode) adresini kullan; Django'da CONN_MAX_AGE=0 ve transaction pooling ile uyumlu ayarlar (gerekirse DISABLE_SERVER_SIDE_CURSORS=True).
   - Migration'ları Vercel build'inde ÇALIŞTIRMA; yerelden production veritabanına ayrıca uygulanacak şekilde README'ye yaz.
3. Ortam değişkenlerini (Bölüm 3) Vercel proje ayarlarına nasıl gireceğimi README'de adım adım anlat. DEBUG=False, ALLOWED_HOSTS ve CSRF_TRUSTED_ORIGINS'e Vercel alan adını ekle.
4. Canlıda kontrol listesi: ana sayfa, statik dosyalar (CSS/JS/font), kayıt/giriş, misafir kilidi, belge indirme (signed URL), admin paneli.
5. Bulduğun sorunları ve çözümlerini README'nin "Deploy notları" bölümüne yaz.
```

**Kabul Kriterleri:**
- [ ] Canlı adreste site açılıyor, CSS/JS yükleniyor.
- [ ] Kayıt, giriş, kilit mantığı ve indirme canlıda da çalışıyor.
- [ ] Gizli anahtarlar repoda yok, yalnızca Vercel ortam değişkenlerinde.

---

## 10. Prototip Sonrası (Şimdilik YAPMA)

Aşağıdakiler bilinçli olarak **kapsam dışı**; prototip çalışınca tek tek eklenebilir:

- E-posta doğrulama ve parola sıfırlama
- Sosyal giriş (Google vb.)
- Gelişmiş arama / filtreleme (Postgres full-text, trigram)
- Yüzlerce ülke için toplu içerik girişi (CSV içe aktarma, içerik editör rolü)
- İçeriklerin doğrulama/güncelleme iş akışı (kaynak linki, sürüm geçmişi)
- Kullanıcıların hata/güncelleme bildirmesi (geri bildirim butonu)
- Tam RTL arayüz desteği
- Rate limiting, bot koruması (captcha)
- Önbellekleme (cache) ve performans iyileştirmeleri
- Analitik

---

## 11. Genel Kabul Kriterleri (Prototip Bitti Sayılır)

- [ ] Misafir: ülke → başvuru özetini ve örnek belge başlıklarını görebiliyor; detay ve indirme kilitli.
- [ ] Üye (e-posta, kullanıcı adı, parola ile kayıtlı): tüm detayları görüyor, belgeleri indiriyor.
- [ ] Senegal örneği Fransızca, Türkiye örneği Türkçe sayfa olarak çalışıyor.
- [ ] Takip/başvuru geçmişi özelliği yok.
- [ ] Tasarım: açık arka plan, canlı renk tonları, mobilde sorunsuz.
- [ ] Vercel'de canlı, veriler Supabase'de.

---

## 12. Sorumluluk Reddi Metni (Footer için taslak)

> Bu sitedeki bilgiler genel bilgilendirme amaçlıdır ve resmî kurumları temsil etmez. Şartlar, ücretler ve belgeler zamanla değişebilir. Başvuru yapmadan önce mutlaka ilgili kurumun resmî kaynaklarından teyit edin.

Bu metin arayüz çevirileriyle (tr, en, fr) birlikte bulunmalı ve her sayfanın alt bilgisinde yer almalıdır.

---

## 13. İlk Mesaj Şablonu (Ajana)

Projeyi başlatırken ilk mesaj olarak şunu yapıştır:

```
Bu klasördeki PLAN.md ve CLAUDE.md (veya AGENTS.md) dosyalarını baştan sona oku.
Projeyi anladığını kısaca Türkçe özetle (5–6 cümle) ve varsa belirsiz noktaları sor.
Henüz kod yazma. Onayımdan sonra sadece FAZ 1'i uygulayacaksın.
```
