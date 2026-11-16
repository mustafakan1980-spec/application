# Application — Ajan Kuralları

- Dil: Kod ve değişken adları İngilizce; kullanıcıya yazdığın açıklamalar ve rapor **Türkçe**.
- Bu bir PROTOTİP. En basit çalışan çözümü seç. Gereksiz kütüphane, katman, soyutlama ekleme.
- Teknoloji: Python, Django (son kararlı sürüm), Supabase (sadece PostgreSQL + Storage), Vercel (deployment).
- Front end: Ayrı framework YOK (React/Vue/Tailwind/Bootstrap yok). Django template + saf HTML, CSS, JavaScript. Hepsi aynı repoda.
- Django'nun yerleşik auth sistemini kullan (Supabase Auth KULLANMA). Supabase sadece veritabanı ve dosya depolama.
- Sadece istenen fazı uygula. Sonraki fazların işini önceden yapma.
- Her faz sonunda: çalıştır, hataları düzelt, kabul kriterlerini tek tek kontrol et, kısa Türkçe rapor yaz.
- Gizli anahtarları ASLA koda yazma; `.env` kullan, `.env.example` güncel tut, `.env` dosyasını `.gitignore`'a ekle.
- Supabase `service_role` anahtarı yalnızca sunucuda kullanılır; asla template/JS içine sızmaz.
- Büyük kararlar (yeni paket, model değişikliği) için önce kısa gerekçe yaz.
- Erişilebilirlik: anlamsal HTML, alt metinler, yeterli renk kontrastı, mobil uyumlu (mobile-first).
