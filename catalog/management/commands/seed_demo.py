from datetime import date
from django.core.management.base import BaseCommand
from catalog.models import (
    Language,
    Country, CountryTranslation,
    Institution, InstitutionTranslation,
    Category, CategoryTranslation,
    Procedure, ProcedureTranslation,
    SampleDocument, SampleDocumentTranslation,
)
from catalog.seed_data.languages_categories import LANGUAGES_DATA, CATEGORIES_DATA
from catalog.seed_data.countries_europe import EUROPE_COUNTRIES
from catalog.seed_data.countries_americas import AMERICAS_COUNTRIES
from catalog.seed_data.countries_asia_oceania import ASIA_OCEANIA_COUNTRIES
from catalog.seed_data.countries_mideast_africa import MIDEAST_AFRICA_COUNTRIES
from catalog.seed_data.importer import seed_country_dataset


class Command(BaseCommand):
    help = 'Tohum (seed) örnek demo verilerini yükler. Tekrar tekrar güvenle çalıştırılabilir (idempotent).'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Talep araştırmasına göre demo veriler yükleniyor..."))

        # ---------------------------------------------------------------------
        # 1. DİLLER
        # ---------------------------------------------------------------------
        langs = {}
        for l_data in LANGUAGES_DATA:
            lang_obj, _ = Language.objects.update_or_create(
                code=l_data['code'],
                defaults={'name_native': l_data['name_native'], 'is_rtl': l_data['is_rtl']}
            )
            langs[lang_obj.code] = lang_obj
            self.stdout.write(f"  [Dil] {lang_obj}")

        # ---------------------------------------------------------------------
        # 2. KATEGORİLER
        # ---------------------------------------------------------------------
        cats = {}
        for c_data in CATEGORIES_DATA:
            cat_obj, _ = Category.objects.update_or_create(
                slug=c_data['slug'],
                defaults={'icon': c_data['icon'], 'order': c_data['order']}
            )
            cats[cat_obj.slug] = cat_obj
            for code, name in c_data['translations'].items():
                if code in langs:
                    CategoryTranslation.objects.update_or_create(
                        category=cat_obj,
                        language=langs[code],
                        defaults={'name': name}
                    )
            self.stdout.write(f"  [Kategori] {cat_obj}")

        # ---------------------------------------------------------------------
        # 3. ÜLKELER
        # ---------------------------------------------------------------------
        countries_data = [
            {
                'iso2': 'TR',
                'slug': 'tr',
                'flag_emoji': '🇹🇷',
                'primary_language': 'tr',
                'official_languages': ['tr'],
                'translations': {
                    'tr': 'Türkiye',
                    'en': 'Turkey',
                    'fr': 'Turquie',
                    'de': 'Türkei',
                }
            },
            {
                'iso2': 'DE',
                'slug': 'de',
                'flag_emoji': '🇩🇪',
                'primary_language': 'de',
                'official_languages': ['de'],
                'translations': {
                    'de': 'Deutschland',
                    'tr': 'Almanya',
                    'en': 'Germany',
                    'fr': 'Allemagne',
                }
            },
            {
                'iso2': 'FR',
                'slug': 'fr',
                'flag_emoji': '🇫🇷',
                'primary_language': 'fr',
                'official_languages': ['fr'],
                'translations': {
                    'fr': 'France',
                    'tr': 'Fransa',
                    'en': 'France',
                    'de': 'Frankreich',
                }
            },
            {
                'iso2': 'GB',
                'slug': 'gb',
                'flag_emoji': '🇬🇧',
                'primary_language': 'en',
                'official_languages': ['en'],
                'translations': {
                    'en': 'United Kingdom',
                    'tr': 'Birleşik Krallık',
                    'fr': 'Royaume-Uni',
                    'de': 'Vereinigtes Königreich',
                }
            },
            {
                'iso2': 'CA',
                'slug': 'ca',
                'flag_emoji': '🇨🇦',
                'primary_language': 'en',
                'official_languages': ['en', 'fr'],
                'translations': {
                    'en': 'Canada',
                    'fr': 'Canada',
                    'tr': 'Kanada',
                    'de': 'Kanada',
                }
            },
            {
                'iso2': 'SN',
                'slug': 'sn',
                'flag_emoji': '🇸🇳',
                'primary_language': 'fr',
                'official_languages': ['fr'],
                'translations': {
                    'fr': 'Sénégal',
                    'tr': 'Senegal',
                    'en': 'Senegal',
                    'de': 'Senegal',
                }
            },
        ]
        countries = {}
        for c_data in countries_data:
            country_obj, _ = Country.objects.update_or_create(
                iso2=c_data['iso2'],
                defaults={
                    'slug': c_data['slug'],
                    'flag_emoji': c_data['flag_emoji'],
                    'primary_language': langs[c_data['primary_language']],
                    'is_published': True,
                }
            )
            for off_code in c_data['official_languages']:
                country_obj.official_languages.add(langs[off_code])

            countries[country_obj.iso2] = country_obj
            for code, name in c_data['translations'].items():
                if code in langs:
                    CountryTranslation.objects.update_or_create(
                        country=country_obj,
                        language=langs[code],
                        defaults={'name': name}
                    )
            self.stdout.write(f"  [Ülke] {country_obj}")

        # ---------------------------------------------------------------------
        # 4. KURUMLAR VE BAŞVURULAR
        # ---------------------------------------------------------------------

        # =====================================================================
        # 4.1 TÜRKİYE (TR)
        # =====================================================================
        # Kurum 1: NVİ
        nvi_tr, _ = Institution.objects.update_or_create(
            country=countries['TR'],
            slug='nvi-turkiye',
            defaults={
                'website': 'https://randevu.nvi.gov.tr',
                'phone': 'Alo 199 [Örnek veri — doğrulanmadı]',
                'email': 'bilgi@nvi.gov.tr [Örnek veri — doğrulanmadı]',
                'address': 'Çamlıca Mah. 408. Cad. No:136 Yenimahalle / Ankara',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=nvi_tr,
            language=langs['tr'],
            defaults={
                'name': 'Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü (NVİ)',
                'address_text': 'Yenimahalle / Ankara, Türkiye',
                'working_hours': 'Hafta içi: 08:30 - 17:30 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=nvi_tr,
            language=langs['en'],
            defaults={
                'name': 'General Directorate of Civil Registration and Citizenship',
                'address_text': 'Ankara, Turkey',
                'working_hours': 'Weekdays: 08:30 - 17:30 [Sample data — unverified]',
            }
        )

        # TR Başvuru 1: Ehliyet
        proc_tr_driver, _ = Procedure.objects.update_or_create(
            slug='tr-b-sinifi-surucu-belgesi',
            defaults={
                'country': countries['TR'],
                'institution': nvi_tr,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 12),
                'official_source_url': 'https://randevu.nvi.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_driver,
            language=langs['tr'],
            defaults={
                'title': 'B Sınıfı Sürücü Belgesi (Ehliyet) Başvurusu',
                'summary': "Türkiye'de otomobil kullanmak için ilk defa B sınıfı sürücü belgesi alma süreci ve gerekli belgeler.",
                'eligibility': "1. 18 yaşını doldurmuş olmak.\n2. En az ilkokul mezuniyeti.\n3. Sürücü olur sağlık raporuna sahip olmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• Sürücü Belgesi Dosyası ve Sertifikası (MEB)\n• T.C. Kimlik Kartı\n• Sürücü Sağlık Raporu (e-Rapor)\n• 1 adet biyometrik fotoğraf\n• Kan grubu belgesi\n• Harç ve değerli kâğıt bedeli makbuzu [Örnek veri — doğrulanmadı]",
                'steps': "1. MEB onaylı sürücü kursu teorik ve direksiyon eğitimlerini tamamlama.\n2. Sınavlardan başarıyla geçilmesi.\n3. Harç bedelinin vergi dairesi/banka aracılığıyla yatırılması.\n4. randevu.nvi.gov.tr üzerinden randevu alma.\n5. İlçe Nüfus Müdürlüğüne başvuru yapılması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Harç ücreti yıllık mevzuata göre güncellenir [Örnek veri — doğrulanmadı].\nBelge basımı sonrası PTT ile 3-7 iş gününde adrese teslim edilir.",
                'validity': "B sınıfı sürücü belgeleri 10 yıl geçerlidir [Örnek veri — doğrulanmadı].",
                'notes': "Resmî randevu işlemleri yalnızca randevu.nvi.gov.tr ve e-Devlet kapısı üzerinden yapılır.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_driver,
            language=langs['en'],
            defaults={
                'title': 'Class B Driving Licence Application',
                'summary': 'Application procedure and requirements for obtaining a first-time category B driving licence in Turkey.',
                'eligibility': '1. Minimum age 18.\n2. Primary school diploma.\n3. Valid driver medical report [Sample data — unverified].',
                'required_documents': 'National ID, Driver medical report, 1 biometric photo, Driving school certificate [Sample data — unverified].',
                'steps': 'Complete certified driving course, pass tests, pay tax duties, book appointment at randevu.nvi.gov.tr.',
                'fees_and_duration': 'Official government fees apply. Delivered by post within 3-7 business days.',
                'validity': 'Valid for 10 years.',
                'notes': 'Official appointments must be made through official NVİ portal.',
            }
        )

        doc_tr_driver, _ = SampleDocument.objects.update_or_create(
            procedure=proc_tr_driver,
            order=1,
            defaults={'storage_path': 'samples/tr_surucu_belgesi_dilekce_ornek.pdf', 'file_type': 'PDF'}
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_tr_driver,
            language=langs['tr'],
            defaults={
                'title': 'Sürücü Belgesi Başvuru ve Bilgi Formu [Örnek Belge — Doğrulanmadı]',
                'description': 'Nüfus müdürlüğüne ibraz edilen başvuru formu şablon örneği.',
            }
        )

        # TR Başvuru 2: Bordo Pasaport
        proc_tr_passport, _ = Procedure.objects.update_or_create(
            slug='tr-umuma-mahsus-bordo-pasaport',
            defaults={
                'country': countries['TR'],
                'institution': nvi_tr,
                'category': cats['passport'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 12),
                'official_source_url': 'https://randevu.nvi.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_passport,
            language=langs['tr'],
            defaults={
                'title': 'Umuma Mahsus (Bordo) Pasaport Başvurusu',
                'summary': "Türkiye Cumhuriyeti vatandaşlarının yurt dışına seyahat edebilmesi için düzenlenen bordo pasaport başvuru rehberi.",
                'eligibility': "T.C. vatandaşı olmak ve yurt dışına çıkış yasağı bulunmamak [Örnek veri — doğrulanmadı].",
                'required_documents': "• T.C. Kimlik Kartı\n• 1 adet biyometrik fotoğraf (son 6 ay içinde çekilmiş)\n• Harç ve defter bedeli ödeme dekontu (sistemden otomatik görünür)\n• Varsa eski pasaport\n• 18 yaş altı için muvafakatname [Örnek veri — doğrulanmadı]",
                'steps': "1. Pasaport defter ve harç bedelinin vergi dairesi veya bankalar aracılığıyla yatırılması.\n2. randevu.nvi.gov.tr veya Alo 199 üzerinden randevu oluşturulması.\n3. İlçe Nüfus Müdürlüğüne giderek parmak izi verilmesi ve başvurunun tamamlanması.\n4. PTT kurye ile adrese teslimat [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Defter bedeli ve harç süresine (6 ay, 1 yıl, 3 yıl, 10 yıl) göre değişir [Örnek veri — doğrulanmadı].\nTeslimat süresi il merkezlerine ortalama 2-4 iş günüdür.",
                'validity': "Seçilen harç süresine bağlı olarak 6 aydan 10 yıla kadar geçerlidir (25 yaş altı öğrencilere harçsız verilebilir).",
                'notes': "Harç ödemeleri NVİ sistemine elektronik olarak düşer, ıslak imzalı dekont zorunlu değildir ancak önerilir.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_passport,
            language=langs['en'],
            defaults={
                'title': 'Standard (Ordinary) Turkish Passport Application',
                'summary': 'Official application guide for Turkish standard burgundy passport issued to citizens.',
                'eligibility': 'Turkish citizenship without any judicial travel restriction [Sample data — unverified].',
                'required_documents': 'National ID card, 1 biometric photo, receipt of passport and booklet fee, previous passport if any.',
                'steps': 'Pay passport fees via bank/tax office, book NVİ appointment, provide fingerprints, delivered by PTT post.',
                'fees_and_duration': 'Varies based on validity period (6 months to 10 years). Delivery in 2-5 business days.',
                'validity': 'Up to 10 years for adults (up to 5 years for minors).',
                'notes': 'Students under 25 years old can obtain fee-exempt passports for educational purposes.',
            }
        )

        # Kurum 2: Göç İdaresi
        goc_tr, _ = Institution.objects.update_or_create(
            country=countries['TR'],
            slug='goc-idaresi-baskanligi',
            defaults={
                'website': 'https://e-ikamet.goc.gov.tr',
                'phone': 'YİMER 157 [Örnek veri — doğrulanmadı]',
                'email': 'gocidaresi@goc.gov.tr [Örnek veri — doğrulanmadı]',
                'address': 'Çamlıca Mah. 122. Sokak No:4 Yenimahalle / Ankara',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=goc_tr,
            language=langs['tr'],
            defaults={
                'name': 'T.C. İçişleri Bakanlığı Göç İdaresi Başkanlığı',
                'address_text': 'Yenimahalle / Ankara, Türkiye',
                'working_hours': 'Hafta içi: 09:00 - 18:00 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=goc_tr,
            language=langs['en'],
            defaults={
                'name': 'Presidency of Migration Management (PMM)',
                'address_text': 'Ankara, Turkey',
                'working_hours': 'Weekdays: 09:00 - 18:00 [Sample data — unverified]',
            }
        )

        # TR Başvuru 3: Kısa Dönem İkamet İzni (Oturum İzni)
        proc_tr_ikamet, _ = Procedure.objects.update_or_create(
            slug='tr-kisa-donem-ikamet-izni',
            defaults={
                'country': countries['TR'],
                'institution': goc_tr,
                'category': cats['residence-permit'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 10),
                'official_source_url': 'https://e-ikamet.goc.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_ikamet,
            language=langs['tr'],
            defaults={
                'title': 'Kısa Dönem İkamet İzni İlk Başvurusu',
                'summary': "Türkiye'de vize veya vize muafiyeti süresinden daha uzun süre kalmak isteyen yabancı ülke vatandaşlarının oturum izni başvurusu.",
                'eligibility': "Türkiye'ye yasal giriş yapmış olmak, geçerli sağlık sigortası ve ikamet amacını kanıtlayıcı belgelere sahip olmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• e-İkamet Başvuru Formu (imzalı)\n• Pasaport aslı ve fotokopisi\n• 4 adet biyometrik fotoğraf\n• Geçerli özel sağlık sigortası\n• Noter onaylı kira sözleşmesi veya tapu fotokopisi (UETS belgesi)\n• Yeterli maddi imkân beyanı\n• Harç ve ikamet kartı bedeli makbuzu [Örnek veri — doğrulanmadı]",
                'steps': "1. e-ikamet.goc.gov.tr adresinden 'İlk Kez İkamet İzni Başvurusu' yapılması.\n2. Sistemden randevu gün ve saatinin alınması.\n3. Başvuru dosyasının eksiksiz hazırlanması.\n4. Randevu günü İl Göç İdaresi Müdürlüğüne şahsen teslim ve parmak izi verilmesi.\n5. İkamet kartının PTT ile adrese teslimi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Kart bedeli + ülke karşılıklılık ilkesine göre harç bedeli [Örnek veri — doğrulanmadı].\nDeğerlendirme süresi azami 90 gündür.",
                'validity': "Genellikle en fazla 1 veya 2 yıl olarak düzenlenir.",
                'notes': "Resmî olmayan aracılara veya ücretli danışmanlık adı altındaki dolandırıcılık sitelerine karşı dikkatli olunmalıdır.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_ikamet,
            language=langs['en'],
            defaults={
                'title': 'Short-Term Residence Permit First Application',
                'summary': 'Application procedure for foreigners intending to stay in Turkey longer than their visa or visa exemption period.',
                'eligibility': 'Legal entry to Turkey, valid private health insurance, registered address, and valid purpose of stay [Sample data — unverified].',
                'required_documents': 'e-Ikamet application form, passport photocopy, 4 biometric photos, health insurance, notarized lease contract, receipt of residence fees.',
                'steps': 'Apply online via e-ikamet.goc.gov.tr, book appointment, submit documents to provincial immigration directorate in person, receive card via PTT.',
                'fees_and_duration': 'Permit fee + card fee depending on nationality. Processing time up to 90 days.',
                'validity': 'Typically issued for 1 or 2 years.',
                'notes': 'Always use the official e-ikamet portal. Official agencies do not work with unofficial fee-charging brokers.',
            }
        )

        # Kurum 3: MEB
        meb_tr, _ = Institution.objects.update_or_create(
            country=countries['TR'],
            slug='meb-turkiye',
            defaults={
                'website': 'https://e-okul.meb.gov.tr',
                'phone': 'MEBİM 444 0 632 [Örnek veri — doğrulanmadı]',
                'email': 'basin@meb.gov.tr [Örnek veri — doğrulanmadı]',
                'address': 'Atatürk Bulvarı No:98 Bakanlıklar / Ankara',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=meb_tr,
            language=langs['tr'],
            defaults={
                'name': 'T.C. Millî Eğitim Bakanlığı (MEB)',
                'address_text': 'Bakanlıklar / Ankara, Türkiye',
                'working_hours': 'Hafta içi: 08:30 - 17:30 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=meb_tr,
            language=langs['en'],
            defaults={
                'name': 'Ministry of National Education',
                'address_text': 'Ankara, Turkey',
                'working_hours': 'Weekdays: 08:30 - 17:30 [Sample data — unverified]',
            }
        )

        # TR Başvuru 4: İlkokul 1. Sınıf Başlama ve Kayıt
        proc_tr_school, _ = Procedure.objects.update_or_create(
            slug='tr-ilkokul-1-sinif-kayit',
            defaults={
                'country': countries['TR'],
                'institution': meb_tr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 10),
                'official_source_url': 'https://e-okul.meb.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_school,
            language=langs['tr'],
            defaults={
                'title': 'İlkokul 1. Sınıf E-Kayıt ve Okul Başlama Süreci',
                'summary': "Türkiye'de mecburi ilköğretim çağına gelen çocukların adrese dayalı nüfus kayıt sistemi (MERNİS) üzerinden ilkokul 1. sınıfa yerleştirilmesi ve kayıt tamamlama rehberi.",
                'eligibility': "Eylül ayı sonu itibarıyla 69 ayını dolduran çocuklar zorunlu kayıt kapsamındadır. 66-68 aylık çocuklar veli dilekçesiyle, 69-71 aylık çocuklar ise veli dilekçesiyle 1 yıl ertelenebilir [Örnek veri — doğrulanmadı].",
                'required_documents': "• Çocuğun T.C. Kimlik Kartı\n• İkametgâh Belgesi (MERNİS otomatik sorgulanır)\n• Kayıt Formu ve Acil Durum İletişim Bilgileri (Okul idaresinden alınır)\n• Aşı kartı fotokopisi [Örnek veri — doğrulanmadı]",
                'steps': "1. Temmuz ayında e-okul.meb.gov.tr veya e-Devlet üzerinden okul kaydı sorgulaması yapılması.\n2. Çocuğun ikamet adresine göre otomatik atandığı ilkokulun belirlenmesi.\n3. Ağustos-Eylül aylarında okul idaresine gidilerek şube ve kayıt işlemlerinin teyit edilmesi.\n4. Okul uyum haftası (Eylül başı) ile eğitime başlanması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet okullarında kayıt tamamen ücretsizdir; bağış veya zorunlu aidat yasal değildir [Örnek veri — doğrulanmadı].",
                'validity': "İlkokul 4 yıllık öğrenim süresince geçerlidir.",
                'notes': "Adres değişikliği durumunda NVİ üzerinden adres güncellemesi yapıldıktan sonra e-Okul nakil başvurusu yapılmalıdır.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_school,
            language=langs['en'],
            defaults={
                'title': 'Primary School 1st Grade e-Enrollment and Admission',
                'summary': 'Address-based official primary school enrollment process for 1st-grade children in Turkey.',
                'eligibility': 'Children reaching 69 months of age by the end of September are legally mandated to enroll [Sample data — unverified].',
                'required_documents': 'Child National ID card, proof of registered residence, emergency contact details form.',
                'steps': 'Check school placement on e-okul.meb.gov.tr in July, visit designated school administration in August-September to confirm.',
                'fees_and_duration': 'Free of charge in public schools.',
                'validity': 'Valid throughout the 4-year primary education period.',
                'notes': 'School placements are strictly based on the national population address registry system (MERNIS).',
            }
        )

        # TR Başvuru 5: Liseye Geçiş Sistemi (LGS) Merkezi Sınav ve Tercih Başvurusu
        proc_tr_lgs, _ = Procedure.objects.update_or_create(
            slug='tr-lgs-ortaogretime-gecis',
            defaults={
                'country': countries['TR'],
                'institution': meb_tr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://e-okul.meb.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_lgs,
            language=langs['tr'],
            defaults={
                'title': 'LGS (Liseye Geçiş Sistemi) Sınav ve Tercih Başvurusu',
                'summary': "8. sınıf öğrencilerinin fen liseleri, Anadolu liseleri ve proje okullarına yerleşebilmek için girdiği merkezi sınav ve okul tercih başvuru süreci.",
                'eligibility': "Resmî ve özel ortaokulların 8. sınıfında öğrenim görüyor olmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• T.C. Kimlik Kartı\n• e-Okul veli giriş bilgileri\n• Tercih Bildirim Formu (Okul müdürlüğünce onaylanan) [Örnek veri — doğrulanmadı]",
                'steps': "1. MEB kılavuzunun yayımlanması ile nisan ayında merkezi sınav başvurusunun yapılması.\n2. Haziran başında 2 oturumlu sınava girilmesi.\n3. Sınav sonuçlarının temmuzda açıklanması.\n4. e-okul.meb.gov.tr üzerinden yerel ve merkezi sınavlı lise tercihlerinin yapılması.\n5. Ortaokul müdürlüğüne gidilerek tercihlerin onaylatılması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet okullarında LGS sınavı ve tercih işlemleri tamamen ücretsizdir.",
                'validity': "Sınav ve yerleştirme ilgili eğitim-öğretim yılı için geçerlidir.",
                'notes': "Tercihlerin mutlaka kayıtlı bulunulan ortaokul müdürlüğü tarafından sistemden onaylanması şarttır.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_lgs,
            language=langs['en'],
            defaults={
                'title': 'High School Entrance Exam (LGS) & Secondary School Placement',
                'summary': 'Application and school choice procedure for 8th graders entering specialized high schools in Turkey.',
                'eligibility': 'Enrolled in 8th grade of accredited public or private middle schools [Sample data — unverified].',
                'required_documents': 'National ID card, e-Okul portal credentials, signed preference submission form.',
                'steps': 'Register online via e-Okul, sit for exam in June, submit high school preferences in July, get verified by middle school administration.',
                'fees_and_duration': 'Free of charge for public exams.',
                'validity': 'Valid for the specific school admission year.',
                'notes': 'Preferences must be approved by the student middle school administration.',
            }
        )

        # Kurum 4: ÖSYM
        osym_tr, _ = Institution.objects.update_or_create(
            country=countries['TR'],
            slug='osym-turkiye',
            defaults={
                'website': 'https://ais.osym.gov.tr',
                'phone': '444 6796 [Örnek veri — doğrulanmadı]',
                'email': 'basin@osym.gov.tr [Örnek veri — doğrulanmadı]',
                'address': 'Üniversiteler Mah. İhsan Doğramacı Bulvarı No:1 Çankaya / Ankara',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=osym_tr,
            language=langs['tr'],
            defaults={
                'name': 'Ölçme, Seçme ve Yerleştirme Merkezi Başkanlığı (ÖSYM)',
                'address_text': 'Çankaya / Ankara, Türkiye',
                'working_hours': 'Hafta içi: 08:30 - 17:30 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=osym_tr,
            language=langs['en'],
            defaults={
                'name': 'Assessment, Selection and Placement Centre (ÖSYM)',
                'address_text': 'Ankara, Turkey',
                'working_hours': 'Weekdays: 08:30 - 17:30 [Sample data — unverified]',
            }
        )

        # TR Başvuru 6: YKS Üniversite Sınavı ve Merkezi Yerleştirme Başvurusu
        proc_tr_yks, _ = Procedure.objects.update_or_create(
            slug='tr-yks-universite-basvurusu',
            defaults={
                'country': countries['TR'],
                'institution': osym_tr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://ais.osym.gov.tr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_yks,
            language=langs['tr'],
            defaults={
                'title': 'YKS Üniversite Giriş Sınavı ve Merkezi Tercih Başvurusu',
                'summary': "Türkiye'de üniversite lisans ve ön lisans programlarına yerleşmek isteyen lise mezunu adayların YKS (TYT, AYT, YDT) başvuru ve tercih süreci.",
                'eligibility': "Lise son sınıf öğrencisi olmak veya lise mezunu olmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• T.C. Kimlik Kartı\n• ÖSYM Aday İşlemleri Sistemi (AİS) şifresi veya e-Devlet girişi\n• Güncel biyometrik fotoğraf (AİS sisteminde geçerli olmalı) [Örnek veri — doğrulanmadı]",
                'steps': "1. Şubat-Mart aylarında ais.osym.gov.tr üzerinden oturum seçiminin yapılması.\n2. Sınav ücretinin banka kartı veya anlaşmalı bankalardan ödenmesi.\n3. Haziran ayında TYT, AYT ve YDT sınavlarına katılım.\n4. Temmuz sonunda sonuçların ilanı ve tercih listesinin hazırlanarak sisteme kaydedilmesi.\n5. Yerleştirme sonucuna göre üniversiteye e-Devlet üzerinden kayıt yapılması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Her oturum için kılavuzda belirlenen sınav ücreti yatırılır [Örnek veri — doğrulanmadı]. Tercih bildirimi ücretsizdir.",
                'validity': "TYT ve AYT puanları ilgili yerleştirme yılı için geçerlidir.",
                'notes': "Başvurular yalnızca resmi ais.osym.gov.tr adresi üzerinden kabul edilir.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_tr_yks,
            language=langs['en'],
            defaults={
                'title': 'Higher Education Institutions Examination (YKS) & University Admission',
                'summary': 'National university entrance examination (YKS) application and central university placement in Turkey.',
                'eligibility': 'High school seniors or high school graduates [Sample data — unverified].',
                'required_documents': 'Turkish ID card, ÖSYM Candidate Portal (AİS) credentials, valid digital photograph.',
                'steps': 'Register session on ais.osym.gov.tr in February/March, pay exam fees, sit for exams in June, submit university preferences in July/August.',
                'fees_and_duration': 'Per-session exam registration fees apply [Sample data — unverified].',
                'validity': 'Exam score valid for the central academic enrollment cycle.',
                'notes': 'Official registrations handled solely through ÖSYM AIS online portal.',
            }
        )

        # =====================================================================
        # 4.2 ALMANYA (DE)
        # =====================================================================
        # Kurum 1: BAMF
        bamf_de, _ = Institution.objects.update_or_create(
            country=countries['DE'],
            slug='bamf-germany',
            defaults={
                'website': 'https://www.bamf.de',
                'phone': '+49 911 943-0 [Örnek veri — doğrulanmadı]',
                'email': 'service@bamf.bund.de [Örnek veri — doğrulanmadı]',
                'address': 'Frankenstraße 210, 90461 Nürnberg, Deutschland',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=bamf_de,
            language=langs['de'],
            defaults={
                'name': 'Bundesamt für Migration und Flüchtlinge (BAMF)',
                'address_text': 'Nürnberg, Deutschland',
                'working_hours': 'Mo - Fr: 09:00 - 15:00 Uhr [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=bamf_de,
            language=langs['tr'],
            defaults={
                'name': 'Almanya Federal Göç ve Mülteciler Dairesi (BAMF)',
                'address_text': 'Nürnberg, Almanya',
                'working_hours': 'Hafta içi: 09:00 - 15:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # DE Başvuru 1: Fırsat Kartı (Chancenkarte 2026)
        proc_de_chancenkarte, _ = Procedure.objects.update_or_create(
            slug='de-chancenkarte-firsat-karti',
            defaults={
                'country': countries['DE'],
                'institution': bamf_de,
                'category': cats['work-permit'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://chancenkarte.com/de/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_chancenkarte,
            language=langs['de'],
            defaults={
                'title': 'Chancenkarte zur Arbeitsplatzsuche (§ 20a AufenthG)',
                'summary': "Die Chancenkarte ermöglicht qualifizierten Fachkräften aus Drittstaaten die Einreise nach Deutschland zur Arbeitsplatzsuche auf Basis eines transparenten Punktesystems.",
                'eligibility': "Vollwertig anerkannte ausländische Berufs- oder Hochschulausbildung ODER mindestens 6 Punkte im Punktesystem (Sprachkenntnisse A1 Deutsch oder B2 Englisch, Berufserfahrung, Alter, Deutschlandbezug) plus Nachweis des Lebensunterhalts [Örnek veri — doğrulanmadı].",
                'required_documents': "• Gültiger Reisepass\n• Nachweis über anerkannten Berufs- oder Hochschulabschluss (ZAB)\n• Sprachzertifikate (Goethe/Telc Deutsch oder IELTS/TOEFL Englisch)\n• Sperrkonto (Sperrbetrag ca. 1.027 EUR/Monat)\n• Krankenversicherungsnachweis (Incoming-Versicherung) [Örnek veri — doğrulanmadı]",
                'steps': "1. Prüfung der Voraussetzungen im Self-Check auf make-it-in-germany.com.\n2. Vorbereitung und Übersetzung aller Diplome und Nachweise.\n3. Eröffnung eines Sperrkontos zur Sicherung des Lebensunterhalts.\n4. Terminbuchung bei der deutschen Auslandsvertretung (Botschaft/Konsulat) oder Visametric.\n5. Visumantrag einreichen und biometrische Daten abgeben.\n6. Einreise und Anmeldung beim Einwohnermeldeamt [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Visumgebühr: 75 EUR [Örnek veri — doğrulanmadı]. Bearbeitungszeit: 4-12 Wochen.",
                'validity': "In der Regel für bis zu 1 Jahr zur Arbeitsplatzsuche erteilt; Verlängerung bei qualifiziertem Beschäftigungsangebot möglich.",
                'notes': "Erlaubt Probebeschäftigung bis zu 20 Stunden pro Woche sowie zweiwöchige Probearbeit bei einem potenziellen Arbeitgeber.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_chancenkarte,
            language=langs['tr'],
            defaults={
                'title': "Almanya Fırsat Kartı (Chancenkarte — 2026 İş Arama Vizesi)",
                'summary': "Nitelikli yabancı uzmanların Almanya'da iş aramak üzere puanlama sistemiyle 1 yıla kadar oturum ve çalışma izni almasını sağlayan yeni nesil vize.",
                'eligibility': "Tam denkliği olan diploma VEYA puan sisteminden en az 6 puan alma (A1 Almanca / B2 İngilizce, mesleki deneyim, yaş, Almanya bağlantısı) ve aylık bloke hesap güvencesi [Örnek veri — doğrulanmadı].",
                'required_documents': "• Geçerli Pasaport\n• ZAB onaylı üniversite/meslek diploması\n• Dil sertifikası (Goethe/Telc A1-B2 veya IELTS/TOEFL)\n• Bloke hesap belgesi (Aylık ~1.027 €)\n• Seyahat sağlık sigortası\n• Özgeçmiş ve motivasyon mektubu [Örnek veri — doğrulanmadı]",
                'steps': "1. Make-it-in-germany.com üzerinden puan uygunluk kontrolü yapılması.\n2. ZAB diploma denklik ve dil belgelerinin temini.\n3. Bloke hesap açılarak gereken meblağın yatırılması.\n4. Konsolosluk / VisaMetric üzerinden vize randevusu alınması.\n5. Başvuru evraklarının teslimi ve mülakat.\n6. Vize onayı sonrası Almanya'ya giriş ve ikamet kaydı [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Vize başvuru harcı: 75 € [Örnek veri — doğrulanmadı]. Ortalama sonuçlanma: 4-12 hafta.",
                'validity': "1 yıl süreli verilir; kalifiye iş bulunması halinde Mavi Kart'a veya çalışma iznine dönüştürülebilir.",
                'notes': "Haftalık 20 saate kadar yarı zamanlı yan işlerde çalışma ve deneme çalışması yapma hakkı tanır.",
            }
        )

        doc_de_chancen, _ = SampleDocument.objects.update_or_create(
            procedure=proc_de_chancenkarte,
            order=1,
            defaults={'storage_path': 'samples/de_chancenkarte_antrag_muster.pdf', 'file_type': 'PDF'}
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_de_chancen,
            language=langs['de'],
            defaults={
                'title': 'Chancenkarte Punkte-Berechnungsbogen [Musterdokument]',
                'description': 'Offizieller Prüfbogen zur Selbstberechnung der Mindestpunktzahl für den Antrag.',
            }
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_de_chancen,
            language=langs['tr'],
            defaults={
                'title': 'Fırsat Kartı Puan Hesaplama ve Başvuru Formu [Örnek Belge — Doğrulanmadı]',
                'description': '6 puan eşiğini hesaplamak için kullanılan örnek başvuru formu şablonu.',
            }
        )

        # DE Başvuru 2: Uni-Assist
        uniassist_de, _ = Institution.objects.update_or_create(
            country=countries['DE'],
            slug='uni-assist-germany',
            defaults={
                'website': 'https://www.uni-assist.de',
                'phone': '+49 30 201 646-001 [Örnek veri — doğrulanmadı]',
                'email': 'service@uni-assist.de [Örnek veri — doğrulanmadı]',
                'address': 'Geneststraße 5, 10829 Berlin, Deutschland',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=uniassist_de,
            language=langs['de'],
            defaults={
                'name': 'uni-assist e.V. (Arbeits- und Servicestelle für internationale Studienbewerbungen)',
                'address_text': 'Berlin, Deutschland',
                'working_hours': 'Mo - Fr: 10:00 - 15:00 Uhr [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=uniassist_de,
            language=langs['tr'],
            defaults={
                'name': 'Uni-Assist e.V. (Uluslararası Üniversite Başvuru Merkezi)',
                'address_text': 'Berlin, Almanya',
                'working_hours': 'Hafta içi: 10:00 - 15:00 [Örnek veri — doğrulanmadı]',
            }
        )

        proc_de_uni, _ = Procedure.objects.update_or_create(
            slug='de-uni-assist-universite-basvurusu',
            defaults={
                'country': countries['DE'],
                'institution': uniassist_de,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.uni-assist.de',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_uni,
            language=langs['de'],
            defaults={
                'title': 'Bewerbung um einen Studienplatz über uni-assist',
                'summary': "Zentrales Bewerbungsverfahren für internationale Studieninteressierte zur Prüfung von Hochschulzugangsberechtigungen an deutschen Hochschulen.",
                'eligibility': "Vorprüfung der Hochschulzugangsberechtigung (Abitur-Äquivalent / HZB) sowie ausreichende Sprachnachweise (Deutsch C1 / TestDaF / DSH oder Englisch TOEFL/IELTS) [Örnek veri — doğrulanmadı].",
                'required_documents': "• Beglaubigte Kopie des Schulabschlusszeugnisses\n• Fächer- und Notenübersichten (Transkripte)\n• Sprachnachweis (TestDaF, DSH, Goethe-Zertifikat)\n• Reisepasskopie\n• Tabellarischer Lebenslauf [Örnek veri — doğrulanmadı]",
                'steps': "1. Registrierung im MyAssist Online-Portal.\n2. Auswahl des gewünschten Studiengangs und der Hochschule.\n3. Hochladen aller Zeugnisse und Nachweise als PDF.\n4. Bezahlung des Bearbeitungsentgelts.\n5. Prüfung durch uni-assist und Weiterleitung an die Hochschule [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "75 EUR für die erste Wunschhochschule; 30 EUR für jede weitere Hochschule je Semester [Örnek veri — doğrulanmadı]. Dauer: 4-6 Wochen.",
                'validity': "Die Vorprüfungsdokumentation (VPD) ist meist 1 Jahr für die entsprechende Hochschule gültig.",
                'notes': "Bewerbungsfristen (15. Juli für das Wintersemester, 15. Januar für das Sommersemester) sind strikt einzuhalten.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_uni,
            language=langs['tr'],
            defaults={
                'title': 'Uni-Assist ile Almanya Üniversite Lisans / Yüksek Lisans Başvurusu',
                'summary': "Almanya'daki 180'den fazla üniversiteye lisans veya yüksek lisans başvurusu yapacak uluslararası öğrencilerin diploma denklik ön inceleme süreci.",
                'eligibility': "Almanya üniversite giriş yeterliliğine (HZB) sahip olmak ve programın dil şartını karşılamak (Almanca TestDaF/Goethe C1 veya İngilizce IELTS/TOEFL) [Örnek veri — doğrulanmadı].",
                'required_documents': "• Lise diploması ve transkript (noter onaylı Almanca/İngilizce çeviri)\n• YKS yerleştirme belgesi (Türkiye'den mezunlar için zorunlu)\n• Dil yeterlilik belgesi\n• Pasaport fotokopisi ve CV [Örnek veri — doğrulanmadı]",
                'steps': "1. uni-assist MyAssist portalında hesap açma.\n2. Üniversite ve bölüm seçimi.\n3. Evrakların dijital olarak yüklenmesi.\n4. Başvuru ücretinin ödenmesi.\n5. Ön İnceleme Belgesi (VPD) düzenlenmesi ve üniversiteye kabul bildirimi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "İlk üniversite başvurusu 75 €, sonraki her başvuru 30 € [Örnek veri — doğrulanmadı]. İnceleme süresi: 4-6 hafta.",
                'validity': "VPD belgesi genellikle düzenlendiği tarihten itibaren 1 yıl geçerlidir.",
                'notes': "Kış dönemi için son başvuru genellikle 15 Temmuz, yaz dönemi için 15 Ocak'tır.",
            }
        )

        # Kurum: LABO Berlin (Fahrerlaubnisbehörde)
        labo_de, _ = Institution.objects.update_or_create(
            country=countries['DE'],
            slug='labo-berlin-fahrerlaubnis',
            defaults={
                'website': 'https://service.berlin.de/standort/121593/',
                'phone': '+49 30 90269-2300 [Örnek veri — doğrulanmadı]',
                'email': 'post.fahrerlaubnis@labo.berlin.de [Örnek veri — doğrulanmadı]',
                'address': 'Puttkamerstraße 16-18, 10958 Berlin, Deutschland',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=labo_de,
            language=langs['de'],
            defaults={
                'name': 'Landesamt für Bürger- und Ordnungsangelegenheiten (Fahrerlaubnisbehörde)',
                'address_text': 'Berlin, Deutschland',
                'working_hours': 'Mo, Di, Do: 07:30 - 15:00 Uhr [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=labo_de,
            language=langs['tr'],
            defaults={
                'name': 'Berlin Sürücü Belgesi ve Trafik Dairesi (Fahrerlaubnisbehörde)',
                'address_text': 'Berlin, Almanya',
                'working_hours': 'Hafta içi mesai saatleri [Örnek veri — doğrulanmadı]',
            }
        )

        # DE Başvuru 3: Ehliyet (Führerschein Klasse B)
        proc_de_license, _ = Procedure.objects.update_or_create(
            slug='de-fuehrerschein-klasse-b',
            defaults={
                'country': countries['DE'],
                'institution': labo_de,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://service.berlin.de/dienstleistung/121593/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_license,
            language=langs['de'],
            defaults={
                'title': 'Führerschein der Klasse B — Ersterteilung',
                'summary': "Verfahren zur Beantragung der Ersterteilung einer Fahrerlaubnis der Klasse B für Kraftfahrzeuge bis 3,5 Tonnen in Deutschland.",
                'eligibility': "Mindestalter 18 Jahre (oder 17 Jahre beim begleiteten Fahren B17), Hauptwohnsitz in Deutschland [Örnek veri — doğrulanmadı].",
                'required_documents': "• Gültiger Personalausweis oder Reisepass mit Meldebescheinigung\n• Biometrisches Passfoto\n• Sehtestbescheinigung (nicht älter als 2 Jahre)\n• Nachweis über Teilnahme an einer Schulung in Erster Hilfe\n• Angabe der zuständigen Fahrschule [Örnek veri — doğrulanmadı]",
                'steps': "1. Anmeldung in einer lizenzierten Fahrschule.\n2. Erste-Hilfe-Kurs und Sehtest absolvieren.\n3. Antrag bei der Fahrerlaubnisbehörde oder im Bürgeramt einreichen.\n4. Theorieunterricht und theoretische Prüfung beim TÜV/DEKRA.\n5. Fahrstunden und praktische Prüfung.\n6. Aushändigung des EU-Kartenführerscheins [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Behördengebühr: ca. 45-50 EUR [Örnek veri — doğrulanmadı]. Gesamtkosten inkl. Fahrschule: ca. 2.500 - 3.500 EUR.",
                'validity': "Führerschein-Dokument ist 15 Jahre gültig; 2 Jahre Probezeit nach Ersterteilung.",
                'notes': "Der Antrag bei der Behörde sollte frühzeitig parallel zur Fahrschulausbildung gestellt werden.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_license,
            language=langs['tr'],
            defaults={
                'title': 'Almanya B Sınıfı Sürücü Belgesi (Ehliyet) İlk Başvurusu',
                'summary': "Almanya'da otomobil kullanabilmek için B sınıfı AB standart sürücü belgesi alma süreci ve yasal adımları.",
                'eligibility': "En az 18 yaşında olmak (veya refakatli sürüş için 17 yaş) ve Almanya'da ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "• Pasaport ve ikametgâh kaydı (Anmeldung)\n• 1 adet biyometrik fotoğraf\n• Göz testi belgesi (Sehtest)\n• İlk yardım kursu katılım belgesi (Erste Hilfe)\n• Kayıtlı bulunulan sürücü kursu bilgisi [Örnek veri — doğrulanmadı]",
                'steps': "1. Sürücü kursuna kayıt olma.\n2. İlk yardım kursu ve göz testini tamamlama.\n3. Bürgeramt veya Fahrerlaubnisbehörde'den randevu alarak ehliyet başvurusunu onaylatma.\n4. TÜV/DEKRA teorik ve direksiyon sınavlarını başarıyla tamamlama.\n5. Ehliyet kartını teslim alma [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Resmi başvuru harcı: ~48 € [Örnek veri — doğrulanmadı]. Kurs ve sınavlar dahil toplam masraf değişkenlik gösterir.",
                'validity': "Ehliyet kartı 15 yıl geçerlidir; ilk 2 yıl stajyerlik (Probezeit) uygulanır.",
                'notes': "Yetkili makama resmi başvuru yapılmadan teorik sınava girilemez.",
            }
        )

        # Kurum: Senatsverwaltung für Bildung, Jugend und Familie (Schulamt)
        senbjf_de, _ = Institution.objects.update_or_create(
            country=countries['DE'],
            slug='schulamt-senbjf-berlin',
            defaults={
                'website': 'https://service.berlin.de/dienstleistung/324903/',
                'phone': '+49 30 90227-5050 [Örnek veri — doğrulanmadı]',
                'email': 'poststelle@senbjf.berlin.de [Örnek veri — doğrulanmadı]',
                'address': 'Bernhard-Weiß-Straße 6, 10178 Berlin, Deutschland',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=senbjf_de,
            language=langs['de'],
            defaults={
                'name': 'Senatsverwaltung für Bildung, Jugend und Familie (Schulamt)',
                'address_text': 'Berlin, Deutschland',
                'working_hours': 'Mo - Fr: 09:00 - 15:00 Uhr [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=senbjf_de,
            language=langs['tr'],
            defaults={
                'name': 'Berlin Eğitim, Gençlik ve Aile Bakanlığı (Schulamt)',
                'address_text': 'Berlin, Almanya',
                'working_hours': 'Hafta içi: 09:00 - 15:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # DE Başvuru 4: Grundschule Einschulung (İlkokul Kaydı)
        proc_de_primary, _ = Procedure.objects.update_or_create(
            slug='de-grundschule-einschulung',
            defaults={
                'country': countries['DE'],
                'institution': senbjf_de,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://service.berlin.de/dienstleistung/324903/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_primary,
            language=langs['de'],
            defaults={
                'title': 'Anmeldung zur Grundschule (Einschulung)',
                'summary': "Verfahren zur regulären Schulanmeldung schulpflichtiger Kinder in die 1. Klasse der zuständigen Grundschule.",
                'eligibility': "Alle Kinder, die im Zeitraum vom 1. Oktober des Vorjahres bis zum 30. September des Einschulungsjahres das 6. Lebensjahr vollenden [Örnek veri — doğrulanmadı].",
                'required_documents': "• Geburtsurkunde des Kindes\n• Personalausweise / Pässe beider Sorgeberechtigter\n• Aktuelle Meldebescheinigung der Familie\n• Nachweis über Masernschutzimpfung\n• Anmeldeformular der zuständigen Einzugsschule [Örnek veri — doğrulanmadı]",
                'steps': "1. Erhalt der schriftlichen Benachrichtigung vom Schulamt.\n2. Persönliche Anmeldung in der zuständigen Einzugsgrundschule im Herbst.\n3. Schulärztliche Untersuchung durch das bezirkliche Gesundheitsamt.\n4. Einschulungsfeier und Beginn des Schuljahres nach den Sommerferien [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Die Schulanmeldung an öffentlichen Grundschulen ist kostenfrei.",
                'validity': "Gilt für den gesamten Zeitraum der Grundschulbildung (Klasse 1-4 bzw. in Berlin/Brandenburg Klasse 1-6).",
                'notes': "Ein Antrag auf Aufnahme in eine andere Wunschschule kann bei der Anmeldung begründet gestellt werden.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_primary,
            language=langs['tr'],
            defaults={
                'title': 'Almanya İlkokul 1. Sınıf Kayıt ve Başlama Süreci (Einschulung)',
                'summary': "Almanya'da 6 yaşını dolduran zorunlu eğitim çağındaki çocukların ikamet adresine bağlı temel ilkokula (Grundschule) kayıt süreci.",
                'eligibility': "Eylül sonu itibarıyla 6 yaşını dolduran tüm çocuklar zorunlu okul kaydı kapsamındadır [Örnek veri — doğrulanmadı].",
                'required_documents': "• Çocuğun doğum belgesi (Geburtsurkunde)\n• Ebeveynlerin pasaportları ve ikametgâh belgesi (Meldebescheinigung)\n• Kızamık aşı belgesi (Masernschutz)\n• Okul kayıt formu [Örnek veri — doğrulanmadı]",
                'steps': "1. Schulamt'tan gelen kayıt çağrı mektubu ile adrese bağlı ilkokula başvuru.\n2. Okul doktoru muayenesi (Schulärztliche Untersuchung).\n3. Sınıf ve şube kesinleşmesi, okul açılışı ve Schultüte geleneği ile başlangıç [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet okullarında kayıt tamamen ücretsizdir.",
                'validity': "Grundschule süresi boyunca (eyalete göre 4 veya 6 yıl) geçerlidir.",
                'notes': "Farklı bir okula gitmek istenirse gerekçeli dilekçe ile nakil talebi sunulabilir.",
            }
        )

        # DE Başvuru 5: Lise Kaydı (Gymnasium / Sekundarstufe Übergang)
        proc_de_secondary, _ = Procedure.objects.update_or_create(
            slug='de-gymnasium-sekundarstufe-anmeldung',
            defaults={
                'country': countries['DE'],
                'institution': senbjf_de,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://service.berlin.de/dienstleistung/324904/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_secondary,
            language=langs['de'],
            defaults={
                'title': 'Übergang in die weiterführende Schule (Gymnasium / ISS)',
                'summary': "Verfahren zur Anmeldung und Zuweisung an eine weiterführende Schule (Gymnasium oder Integrierte Sekundarschule) nach Abschluss der Grundschulzeit.",
                'eligibility': "Erfolgreicher Abschluss der 4. Klasse (bzw. 6. Klasse in Berlin/Brandenburg) und Vorliegen der Förderprognose der Grundschule [Örnek veri — doğrulanmadı].",
                'required_documents': "• Anmeldebogen für weiterführende Schulen mit Erst-, Zweit- und Drittwunsch\n• Förderprognose der Grundschule (Notenübersicht und Gutachten)\n• Halbjahreszeugnis\n• Ausweise der Sorgeberechtigten [Örnek veri — doğrulanmadı]",
                'steps': "1. Erhalt der Förderprognose und Beratungsgespräch an der Grundschule.\n2. Abgabe des Anmeldebogens an der Erstwunschschule im Februar.\n3. Prüfung der Kapazitäten und Eignungskriterien.\n4. Versand der Aufnahmebescheide im Mai/Juni [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Kostenfrei an allen staatlichen Regelschulen.",
                'validity': "Gilt bis zum Erwerb des mittleren Schulabschlusses (MSA) bzw. des Abiturs.",
                'notes': "Bei Übernachfrage an beliebten Gymnasien entscheidet meist die Durchschnittsnote der Förderprognose.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_secondary,
            language=langs['tr'],
            defaults={
                'title': 'Almanya Lise Geçişi ve Gymnasium Kayıt Başvurusu',
                'summary': "Grundschule sonrası öğrencilerin akademik başarı veya öğretmen tavsiyesine göre Gymnasium veya ortaöğretim okullarına kayıt olma süreci.",
                'eligibility': "İlkokulu başarıyla bitirmek ve okuldan alınan öğretmen değerlendirme/tavsiye raporu (Förderprognose) [Örnek veri — doğrulanmadı].",
                'required_documents': "• 3 tercihli okul başvuru formu\n• İlkokul başarı tavsiye belgesi ve dönem karnesi\n• Veli kimlik ve ikamet belgeleri [Örnek veri — doğrulanmadı]",
                'steps': "1. Grundschule'den tavsiye raporunun alınması.\n2. Şubat ayında 1. tercih okuluna şahsen başvuru.\n3. Okul kontenjan değerlendirmesi ve kabul mektubunun tebliği [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet liselerinde başvuru ve eğitim ücretsizdir.",
                'validity': "Abitur (lise diploması) mezuniyetine kadar geçerlidir.",
                'notes': "Kontenjan aşımı olan okullarda öğrencinin karne not ortalaması öncelik sebebidir.",
            }
        )

        # DE Başvuru 6: AB Mavi Kart (Blaue Karte EU)
        proc_de_bluecard, _ = Procedure.objects.update_or_create(
            slug='de-blaue-karte-eu',
            defaults={
                'country': countries['DE'],
                'institution': bamf_de,
                'category': cats['residence-permit'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.bamf.de/DE/Themen/MigrationAufenthalt/ZuwandererDrittstaaten/Migrathek/BlaueKarteEU/blauekarteeu-node.html',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_bluecard,
            language=langs['de'],
            defaults={
                'title': 'Blaue Karte EU (§ 18g AufenthG) für Fachkräfte',
                'summary': "Aufenthaltstitel für Hochschulabsolventen und IT-Spezialisten aus Nicht-EU-Staaten mit einem konkreten Arbeitsplatzangebot in Deutschland.",
                'eligibility': "Anerkannter deutscher oder ausländischer Hochschulabschluss sowie Nachweis eines Mindestbruttogehalts gemäß den aktuellen gesetzlichen Schwellenwerten (Regelberufe oder Engpassberufe) [Örnek veri — doğrulanmadı].",
                'required_documents': "• Arbeitsvertrag oder verbindliches Stellenangebot\n• Erklärung zum Beschäftigungsverhältnis\n• Anerkannter Hochschulabschluss (Anabin-Auszug oder ZAB)\n• Gültiger Reisepass und biometrisches Foto\n• Mietvertrag und Nachweis der Krankenversicherung [Örnek veri — doğrulanmadı]",
                'steps': "1. Abschluss eines Arbeitsvertrags mit deutschem Arbeitgeber.\n2. Visumantrag bei der Botschaft oder Direktantrag bei der Ausländerbehörde vor Ort.\n3. Prüfung durch die Bundesagentur für Arbeit (falls erforderlich).\n4. Ausstellung der Blauen Karte EU als elektronischer Aufenthaltstitel [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Erteilungsgebühr: 100 EUR [Örnek veri — doğrulanmadı]. Bearbeitung: 4-8 Wochen.",
                'validity': "Dauer des Arbeitsvertrags plus 3 Monate, maximal 4 Jahre; nach 21-27 Monaten Niederlassungserlaubnis (Daueraufenthalt) möglich.",
                'notes': "Erleichterter Familiennachzug ohne vorherigen Deutschnachweis der Ehepartner.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_de_bluecard,
            language=langs['tr'],
            defaults={
                'title': 'Almanya AB Mavi Kart (Blaue Karte EU) Çalışma ve Oturum İzni',
                'summary': "Almanya'da nitelikli bir iş teklifi alan üniversite mezunları ve kıdemli BT uzmanları için hızlı kalıcı oturum imkânı sunan oturum izni.",
                'eligibility': "Denkliği bulunan üniversite diploması ve yasal olarak belirlenen asgari yıllık brüt maaş eşiğini karşılayan iş sözleşmesi [Örnek veri — doğrulanmadı].",
                'required_documents': "• İş sözleşmesi ve iş tanımı formu (Erklärung zum Beschäftigungsverhältnis)\n• Anabin/ZAB onaylı diploma\n• Pasaport ve biyometrik fotoğraf\n• Almanya'da konut kira sözleşmesi ve sağlık sigortası [Örnek veri — doğrulanmadı]",
                'steps': "1. Konsolosluktan D tipi çalışma vizesi alma veya Almanya'da Ausländerbehörde'ye başvuru.\n2. Belgelerin teslimi ve biyometri kaydı.\n3. eAT (elektronik oturum kartı) teslimi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Kart bedeli: ~100 € [Örnek veri — doğrulanmadı]. İşlem süresi: 4-8 hafta.",
                'validity': "İş sözleşmesi süresi + 3 ay (en fazla 4 yıl); B1 Almanca ile 21 ayda, A1 ile 27 ayda süresiz yerleşim iznine geçiş sağlar.",
                'notes': "Eşler için dil şartı aranmaksızın aile birleşimi ve sınırsız çalışma hakkı tanır.",
            }
        )

        # =====================================================================
        # 4.3 FRANSA (FR)
        # =====================================================================
        # Kurum 1: Ministère de l'Intérieur
        minint_fr, _ = Institution.objects.update_or_create(
            country=countries['FR'],
            slug='ministere-interieur-france',
            defaults={
                'website': 'https://administration-etrangers-en-france.interieur.gouv.fr',
                'phone': '3939 [Örnek veri — doğrulanmadı]',
                'email': 'contact-anef@interieur.gouv.fr [Örnek veri — doğrulanmadı]',
                'address': 'Place Beauvau, 75800 Paris Cedex 08, France',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=minint_fr,
            language=langs['fr'],
            defaults={
                'name': "Ministère de l'Intérieur (ANEF - Séjour des étrangers)",
                'address_text': 'Paris, France',
                'working_hours': 'Lundi au Vendredi: 08h30 - 17h00 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=minint_fr,
            language=langs['tr'],
            defaults={
                'name': "Fransa İçişleri Bakanlığı (ANEF Dijital Göçmenlik Portalı)",
                'address_text': 'Paris, Fransa',
                'working_hours': 'Hafta içi: 08:30 - 17:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # FR Başvuru 1: VLS-TS Étudiant
        campus_fr, _ = Institution.objects.update_or_create(
            country=countries['FR'],
            slug='campus-france-visas',
            defaults={
                'website': 'https://france-visas.gouv.fr',
                'phone': '+33 1 40 40 58 58 [Örnek veri — doğrulanmadı]',
                'email': 'information@campusfrance.org [Örnek veri — doğrulanmadı]',
                'address': '28 rue de la Grange aux Belles, 75010 Paris, France',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=campus_fr,
            language=langs['fr'],
            defaults={
                'name': 'Campus France & France-Visas',
                'address_text': 'Paris, France',
                'working_hours': 'Lundi au vendredi : 09h00 - 17h00 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=campus_fr,
            language=langs['tr'],
            defaults={
                'name': 'Campus France & France-Visas Vize İdaresi',
                'address_text': 'Paris, Fransa',
                'working_hours': 'Hafta içi: 09:00 - 17:00 [Örnek veri — doğrulanmadı]',
            }
        )

        proc_fr_student, _ = Procedure.objects.update_or_create(
            slug='fr-visa-long-sejour-etudiant',
            defaults={
                'country': countries['FR'],
                'institution': campus_fr,
                'category': cats['visa'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://france-visas.gouv.fr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_student,
            language=langs['fr'],
            defaults={
                'title': "Visa de long séjour valant titre de séjour (VLS-TS) — Étudiant",
                'summary': "Procédure officielle permettant aux étudiants étrangers de s'installer en France pour suivre des études supérieures pour une durée supérieure à 3 mois.",
                'eligibility': "Admission dans un établissement d'enseignement supérieur français et justification de ressources mensuelles d'au moins 615 EUR [Örnek veri — doğrulanmadı].",
                'required_documents': "• Attestation d'accord préalable d'inscription (Campus France)\n• Justificatifs de ressources financières (attestation bancaire, bourse)\n• Justificatif d'hébergement pour les 3 premiers mois\n• Passeport valide et photos d'identité conformes [Örnek veri — doğrulanmadı]",
                'steps': "1. Procédure 'Études en France' sur Campus France.\n2. Création de la demande sur france-visas.gouv.fr.\n3. Rendez-vous de dépôt de dossier chez le prestataire officiel (TLScontact / VFS Global).\n4. Arrivée en France et validation obligatoire en ligne sur l'ANEF dans les 3 mois [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Frais de visa : 50 EUR (ou 99 EUR selon convention) + taxe de validation OFII de 50 EUR [Örnek veri — doğrulanmadı]. Délai : 2-4 semaines.",
                'validity': "Valable entre 4 et 12 mois, renouvelable en titre de séjour pluriannuel.",
                'notes': "Autorise le travail à titre accessoire à concurrence de 60 % de la durée annuelle du travail (964 heures par an).",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_student,
            language=langs['tr'],
            defaults={
                'title': 'Fransa Uzun Dönem Öğrenci Vizesi (VLS-TS Étudiant)',
                'summary': "Fransa'da üniversite veya yükseköğrenim kurumlarında 3 aydan uzun süre öğrenim görecek öğrencilerin vize ve ilk oturum izni süreci.",
                'eligibility': "Fransa'daki akredite bir üniversiteden kabul belgesi ve aylık en az 615 € finansal kaynak teminatı [Örnek veri — doğrulanmadı].",
                'required_documents': "• Campus France kabul ve onay sertifikası\n• Banka bloke hesap veya sponsorluk teminat yazısı\n• İlk 3 aylık konaklama belgesi\n• Pasaport ve biyometrik fotoğraflar [Örnek veri — doğrulanmadı]",
                'steps': "1. Campus France 'Etudes en France' dosyasının onaylanması.\n2. France-Visas portalından başvuru formunun doldurulması.\n3. VFS Global / TLScontact merkezine evrak teslimi ve biyometri.\n4. Fransa'ya varışta 3 ay içinde ANEF portalından vizenin online onaylatılması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Vize harcı: 50 € + OFII onay pulu: 50 € [Örnek veri — doğrulanmadı]. Ortalama süre: 2-4 hafta.",
                'validity': "Genellikle 1 yıllık düzenlenir; eğitim süresince Fransa içinden çok yıllık karta uzatılabilir.",
                'notes': "Öğrencilere yılda 964 saate kadar yasal yarı zamanlı çalışma hakkı tanır.",
            }
        )

        # FR Başvuru 2: Titre de séjour
        proc_fr_titre, _ = Procedure.objects.update_or_create(
            slug='fr-titre-de-sejour-vie-privee',
            defaults={
                'country': countries['FR'],
                'institution': minint_fr,
                'category': cats['residence-permit'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://administration-etrangers-en-france.interieur.gouv.fr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_titre,
            language=langs['fr'],
            defaults={
                'title': "Première demande de titre de séjour temporaire en Préfecture",
                'summary': "Démarche dématérialisée ou en préfecture pour l'obtention d'un titre de séjour régulier en France.",
                'eligibility': "Résider sur le territoire français sous couvert d'un visa de long séjour en cours de validité [Örnek veri — doğrulanmadı].",
                'required_documents': "• Copie intégrale du passeport\n• Justificatif de domicile de moins de 6 mois\n• 3 photographies d'identité récentes ou e-photo\n• Justificatifs d'état civil et de situation professionnelle [Örnek veri — doğrulanmadı]",
                'steps': "1. Connexion au portail ANEF du Ministère de l'Intérieur.\n2. Sélection du motif de séjour et saisie du dossier en ligne.\n3. Téléchargement de l'attestation de dépôt sécurisée.\n4. Convocation en préfecture pour la prise d'empreintes digitales.\n5. Retrait de la carte plastifiée de séjour [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Taxe de séjour et droit de timbre : 225 EUR [Örnek veri — doğrulanmadı]. Délai de délivrance : 2 à 4 mois.",
                'validity': "Délivré pour 1 an en titre temporaire, puis jusqu'à 4 ans en carte pluriannuelle.",
                'notes': "Depuis la généralisation de l'ANEF, la majorité des démarches s'effectuent sans déplacement préalable au guichet.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_titre,
            language=langs['tr'],
            defaults={
                'title': 'Fransa Valilik Oturum İzni (Titre de Séjour) İlk Başvurusu',
                'summary': "Fransa'da uzun dönem vize sonrasında yasal olarak ikamet etmeye devam etmek için valilik (Préfecture) oturum kartı alma süreci.",
                'eligibility': "Geçerli bir uzun dönem vizeye sahip olmak ve Fransa'da yerleşik adreste ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "• Pasaport fotokopisi\n• Son 6 aya ait ikametgâh belgesi (fatura, kira kontratı)\n• e-Photo biyometrik kod\n• Gelir veya çalışma durumunu gösterir resmî belgeler [Örnek veri — doğrulanmadı]",
                'steps': "1. administration-etrangers-en-france.interieur.gouv.fr adresinden online başvuru.\n2. Dosya teslim belgesinin (attestation de dépôt) indirilmesi.\n3. Valiliğe parmak izi vermeye gidilmesi.\n4. SMS bildirimi ile oturum kartının valilikten teslim alınması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Vergi ve harç pulu: ~225 € [Örnek veri — doğrulanmadı]. İşlem süresi: 2-4 ay.",
                'validity': "İlk yıl 1 yıllık verilir; yenilemede 4 yıllık çok yıllık karta geçilebilir.",
                'notes': "Başvurular artık ANEF dijital platformu üzerinden çevrim içi yapılmaktadır.",
            }
        )

        # Kurum: France Titres / ANTS
        ants_fr, _ = Institution.objects.update_or_create(
            country=countries['FR'],
            slug='ants-france-titres',
            defaults={
                'website': 'https://permisdeconduire.ants.gouv.fr',
                'phone': '34 00 [Örnek veri — doğrulanmadı]',
                'email': 'contact@ants.gouv.fr [Örnek veri — doğrulanmadı]',
                'address': '18 rue Irénée Carré, 08000 Charleville-Mézières, France',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ants_fr,
            language=langs['fr'],
            defaults={
                'name': 'France Titres (Agence Nationale des Titres Sécurisés - ANTS)',
                'address_text': 'Charleville-Mézières, France',
                'working_hours': 'Lundi au Vendredi: 07h45 - 19h00 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ants_fr,
            language=langs['tr'],
            defaults={
                'name': 'Fransa Güvenli Kimlik ve Sürücü Belgeleri İdaresi (France Titres - ANTS)',
                'address_text': 'Fransa',
                'working_hours': 'Hafta içi: 08:00 - 18:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # FR Başvuru 3: Ehliyet (Permis de conduire B)
        proc_fr_driving, _ = Procedure.objects.update_or_create(
            slug='fr-permis-de-conduire-b',
            defaults={
                'country': countries['FR'],
                'institution': ants_fr,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://permisdeconduire.ants.gouv.fr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_driving,
            language=langs['fr'],
            defaults={
                'title': 'Demande de permis de conduire — Catégorie B',
                'summary': "Procédure d'inscription aux examens et d'obtention du premier permis de conduire sécurisé format carte bancaire en France.",
                'eligibility': "Être âgé d'au moins 17 ans (réforme du permis dès 17 ans) et résider régulièrement en France [Örnek veri — doğrulanmadı].",
                'required_documents': "• Pièce d'identité en cours de validité\n• Justificatif de domicile de moins de 6 mois\n• Code photo numérique et signature d'identité (e-photo)\n• Certificat d'examen du permis de conduire (CEPC) avec mention favorable [Örnek veri — doğrulanmadı]",
                'steps': "1. Création d'un compte sur permisdeconduire.ants.gouv.fr pour obtenir le numéro NEPH.\n2. Réussite à l'épreuve théorique générale (Code de la route).\n3. Formation pratique en auto-école et réussite à l'examen de conduite.\n4. Téléchargement du certificat provisoire CEPC.\n5. Demande de fabrication du permis définitif en ligne et réception par voie postale [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Frais de fabrication gratuits; taxe régionale éventuelle selon le département [Örnek veri — doğrulanmadı]. Délai de fabrication : 2-3 semaines.",
                'validity': "Le titre au format carte plastifiée est valable 15 ans.",
                'notes': "Le certificat provisoire CEPC permet de conduire légalement sur le territoire français pendant 4 mois en attendant la carte.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_driving,
            language=langs['tr'],
            defaults={
                'title': 'Fransa B Sınıfı Sürücü Belgesi (Ehliyet) Başvurusu',
                'summary': "Fransa'da B sınıfı otomobil ehliyeti alma, sınav kayıt süreci (NEPH) ve kart basım adımları.",
                'eligibility': "En az 17 yaşında olmak ve Fransa'da yasal olarak ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "• Kimlik belgesi veya oturum kartı\n• 6 aydan yeni adres belgesi\n• Dijital e-Photo kodu\n• Başarılı direksiyon sınav sonuç belgesi (CEPC) [Örnek veri — doğrulanmadı]",
                'steps': "1. ANTS üzerinden kayıt olup NEPH dosya numarası alma.\n2. Trafik teorik sınavını (Code) geçme.\n3. Sürücü kursu direksiyon sınavını tamamlama.\n4. CEPC geçici sürüş belgesini indirme.\n5. ANTS'den asıl kart basım talebi oluşturma ve posta ile teslim alma [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet kart basım harcı ücretsizdir (bölgeye göre küçük damga vergisi olabilir). Basım süresi 2-3 hafta.",
                'validity': "Kart 15 yıl geçerlidir; ilk 3 yıl stajyer (permis probatoire) statüsündedir.",
                'notes': "Sınavı geçtikten sonra indirilen CEPC belgesi 4 ay boyunca geçici ehliyet olarak kullanılır.",
            }
        )

        # Kurum: Ministère de l'Éducation nationale
        menj_fr, _ = Institution.objects.update_or_create(
            country=countries['FR'],
            slug='menj-france',
            defaults={
                'website': 'https://www.service-public.fr/particuliers/vosdroits/F1864',
                'phone': '3939 [Örnek veri — doğrulanmadı]',
                'email': 'contact@education.gouv.fr [Örnek veri — doğrulanmadı]',
                'address': '110 rue de Grenelle, 75007 Paris, France',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=menj_fr,
            language=langs['fr'],
            defaults={
                'name': "Ministère de l'Éducation nationale et Mairies de France",
                'address_text': 'Paris, France',
                'working_hours': 'Lundi au Vendredi: 08h30 - 17h00 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=menj_fr,
            language=langs['tr'],
            defaults={
                'name': "Fransa Millî Eğitim Bakanlığı ve İlçe Belediyeleri (Mairie)",
                'address_text': 'Paris, Fransa',
                'working_hours': 'Hafta içi mesai saatleri [Örnek veri — doğrulanmadı]',
            }
        )

        # FR Başvuru 4: İlkokul Kaydı (École élémentaire)
        proc_fr_elem, _ = Procedure.objects.update_or_create(
            slug='fr-inscription-ecole-elementaire',
            defaults={
                'country': countries['FR'],
                'institution': menj_fr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.service-public.fr/particuliers/vosdroits/F1864',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_elem,
            language=langs['fr'],
            defaults={
                'title': "Inscription de votre enfant à l'école élémentaire (CP)",
                'summary': "Démarche d'inscription obligatoire en mairie et à l'école de secteur pour les enfants entrant en cours préparatoire (CP).",
                'eligibility': "Enfants ayant atteint l'âge de 6 ans au cours de l'année civile de la rentrée scolaire [Örnek veri — doğrulanmadı].",
                'required_documents': "• Livret de famille ou extrait d'acte de naissance de l'enfant\n• Justificatif de domicile récent\n• Document attestant de la vaccination obligatoire (DTP)\n• Certificat d'inscription délivré par la mairie [Örnek veri — doğrulanmadı]",
                'steps': "1. Démarche auprès de la mairie du domicile au printemps pour obtenir le certificat d'inscription.\n2. Prise de rendez-vous avec la direction de l'école primaire du secteur.\n3. Présentation des pièces justificatives et admission définitive de l'enfant [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "L'inscription dans les écoles publiques est gratuite et obligatoire.",
                'validity': "Valable pour toute la scolarité élémentaire (du CP au CM2).",
                'notes': "L'instruction est obligatoire dès l'âge de 3 ans en France depuis la rentrée 2019.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_elem,
            language=langs['tr'],
            defaults={
                'title': 'Fransa İlkokul (CP) Kayıt Başvurusu',
                'summary': "Fransa'da 6 yaşını dolduran çocukların belediye (Mairie) ve mahalle okuluna resmi kayıt adımları.",
                'eligibility': "Eğitim yılının sona erdiği takvim yılında 6 yaşını dolduran tüm çocuklar zorunlu kayıt kapsamındadır [Örnek veri — doğrulanmadı].",
                'required_documents': "• Aile cüzdanı veya çocuğun doğum kayıt örneği\n• İkametgâh belgesi (son 3 aya ait elektrik/gaz faturası)\n• DTP zorunlu aşı karnesi\n• Belediye kayıt belgesi [Örnek veri — doğrulanmadı]",
                'steps': "1. İlkbahar aylarında bağlı bulunulan belediyeye (Mairie) giderek kayıt belgesi alma.\n2. Mahalle okulunun müdürlüğü ile randevulaşma.\n3. Evrakları teslim ederek kesin kaydı tamamlama [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Fransız devlet okullarında kayıt tamamen ücretsizdir.",
                'validity': "İlkokul (CP - CM2) dönemi boyunca geçerlidir.",
                'notes': "Fransa'da anaokulundan itibaren (3 yaş) eğitim zorunludur.",
            }
        )

        # FR Başvuru 5: Lise Kaydı (Affelnet-Lycée)
        proc_fr_lycee, _ = Procedure.objects.update_or_create(
            slug='fr-affectation-lycee-affelnet',
            defaults={
                'country': countries['FR'],
                'institution': menj_fr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.education.gouv.fr/l-orientation-en-3e-et-l-affectation-en-lycee-324424',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_lycee,
            language=langs['fr'],
            defaults={
                'title': "Affectation et inscription au lycée via Affelnet-Lycée",
                'summary': "Procédure d'orientation en fin de classe de 3e et d'affectation des élèves vers la classe de seconde générale, technologique ou professionnelle.",
                'eligibility': "Élèves scolarisés en classe de 3e de collège en France ou équivalence de niveau académique [Örnek veri — doğrulanmadı].",
                'required_documents': "• Fiche de vœux d'orientation et d'affectation dûment signée\n• Bulletins scolaires de l'année de 3e\n• Justificatif de domicile\n• Dossier d'inscription du lycée d'affectation [Örnek veri — doğrulanmadı]",
                'steps': "1. Formulation des intentions d'orientation au 2e trimestre de 3e.\n2. Saisie des vœux d'établissements et de filières sur le portail EduConnect / Affelnet en mai.\n3. Publication des résultats d'affectation fin juin.\n4. Inscription administrative directe auprès du lycée attribué début juillet [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Procédure entièrement gratuite dans l'enseignement public.",
                'validity': "Valable pour le cycle secondaire menant au Baccalauréat (3 ans).",
                'notes': "Les vœux sont traités automatiquement par l'algorithme Affelnet en fonction du secteur géographique et du dossier scolaire.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_lycee,
            language=langs['tr'],
            defaults={
                'title': 'Fransa Lise Yerleştirme ve Kayıt Süreci (Affelnet-Lycée)',
                'summary': "Fransa'da ortaokul (3e) son sınıf öğrencilerinin genel, teknolojik veya meslek liselerine merkezi yerleştirme sistemi.",
                'eligibility': "Ortaokulu başarıyla tamamlamak ve akademik kuruldan lise geçiş onayı almak [Örnek veri — doğrulanmadı].",
                'required_documents': "• İmzalı tercih bildirim formu\n• 3e sınıfı karne ve not çizelgeleri\n• İkametgâh belgesi [Örnek veri — doğrulanmadı]",
                'steps': "1. Mayıs ayında EduConnect / Affelnet portalında okul ve alan tercihlerinin yapılması.\n2. Haziran sonunda yerleştirme sonuçlarının açıklanması.\n3. Temmuz başında atanan liseye bizzat gidilerek kaydın tamamlanması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet liselerinde başvuru ve kayıt ücretsizdir.",
                'validity': "Lise eğitimi (Baccalauréat) süresince geçerlidir.",
                'notes': "Yerleştirmede öğrencinin coğrafi ikamet sektörü ve karne notları esas alınır.",
            }
        )

        # Kurum: Parcoursup
        mesr_fr, _ = Institution.objects.update_or_create(
            country=countries['FR'],
            slug='parcoursup-france',
            defaults={
                'website': 'https://www.parcoursup.gouv.fr',
                'phone': '0800 400 070 [Örnek veri — doğrulanmadı]',
                'email': 'contact@parcoursup.fr [Örnek veri — doğrulanmadı]',
                'address': '1 rue Descartes, 75231 Paris Cedex 05, France',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=mesr_fr,
            language=langs['fr'],
            defaults={
                'name': "Parcoursup (Ministère de l'Enseignement supérieur et de la Recherche)",
                'address_text': 'Paris, France',
                'working_hours': "Assistance en ligne 7j/7 pendant la campagne d'inscription [Örnek veri — doğrulanmadı]",
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=mesr_fr,
            language=langs['tr'],
            defaults={
                'name': "Parcoursup Fransa Yükseköğretim ve Üniversite Başvuru Portalı",
                'address_text': 'Paris, Fransa',
                'working_hours': 'Online başvuru sistemi [Örnek veri — doğrulanmadı]',
            }
        )

        # FR Başvuru 6: Parcoursup Üniversite
        proc_fr_parcoursup, _ = Procedure.objects.update_or_create(
            slug='fr-parcoursup-universite',
            defaults={
                'country': countries['FR'],
                'institution': mesr_fr,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.parcoursup.gouv.fr',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_parcoursup,
            language=langs['fr'],
            defaults={
                'title': "Parcoursup — Inscription en première année de l'enseignement supérieur",
                'summary': "Plateforme nationale de préinscription en 1ère année d'études supérieures (Licence, BTS, BUT, CPGE, écoles d'ingénieurs) en France.",
                'eligibility': "Élèves de terminale préparant le Baccalauréat ou étudiants déjà titulaires du baccalauréat ou d'un diplôme étranger équivalent [Örnek veri — doğrulanmadı].",
                'required_documents': "• Numéro INE (Identifiant National Étudiant) ou identifiant étranger\n• Bulletins scolaires de 1ère et de Terminale\n• Projet de formation motivé rédigé pour chaque vœu\n• Fiche Avenir remplie par l'équipe pédagogique [Örnek veri — doğrulanmadı]",
                'steps': "1. Ouverture de compte et formulation de 10 vœux maximum entre janvier et mars.\n2. Confirmation des vœux et finalisation des dossiers début avril.\n3. Réception des propositions d'admission à partir de fin mai.\n4. Réponse obligatoire aux propositions dans les délais impartis.\n5. Inscription administrative dans l'université choisie [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "L'inscription sur Parcoursup est gratuite (certaines filières sélectives privées appliquent des frais de concours).",
                'validity': "Valable pour l'admission à la rentrée universitaire de septembre.",
                'notes': "Une phase complémentaire s'ouvre à la mi-juin pour les candidats n'ayant pas reçu de proposition.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_fr_parcoursup,
            language=langs['tr'],
            defaults={
                'title': 'Parcoursup — Fransa Üniversite ve Yükseköğretim İlk Yıl Başvurusu',
                'summary': "Fransa'daki üniversite lisans programlarına (Licence, BUT, BTS) merkezi sistemle başvuru ve kabul süreci rehberi.",
                'eligibility': "Lise son sınıf öğrencisi olmak veya lise mezuniyeti/Fransız bakalorya denkliği bulunmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• INE öğrenci numarası veya geçerli pasaport\n• Lise karne ve transkript belgeleri\n• Her tercih için yazılmış gerekçeli motivasyon mektubu (Projet de formation motivé) [Örnek veri — doğrulanmadı]",
                'steps': "1. Ocak-Mart aylarında en fazla 10 tercih seçilmesi.\n2. Nisan başında dosyaların tamamlanıp onaylanması.\n3. Mayıs sonunda kabul yanıtlarının (oui / attente) başlaması.\n4. Süre dolmadan kabulün onaylanması ve üniversite kaydı [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Parcoursup platformunda başvuru tamamen ücretsizdir.",
                'validity': "İlgili akademik yıl kayıt dönemi için geçerlidir.",
                'notes': "Açıkta kalan veya yeni tercih yapmak isteyenler için haziranda ek yerleştirme (Phase complémentaire) açılır.",
            }
        )

        # =====================================================================
        # 4.4 BİRLEŞİK KRALLIK (GB)
        # =====================================================================
        # Kurum 1: Home Office / UKVI
        home_office_uk, _ = Institution.objects.update_or_create(
            country=countries['GB'],
            slug='home-office-uk',
            defaults={
                'website': 'https://www.gov.uk/government/organisations/uk-visas-and-immigration',
                'phone': '+44 300 790 6268 [Sample data — unverified]',
                'email': 'public.enquiries@homeoffice.gov.uk [Sample data — unverified]',
                'address': '2 Marsham Street, London, SW1P 4DF, United Kingdom',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=home_office_uk,
            language=langs['en'],
            defaults={
                'name': 'UK Visas and Immigration (UKVI) & Home Office',
                'address_text': 'London, United Kingdom',
                'working_hours': 'Monday to Friday: 09:00 - 17:00 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=home_office_uk,
            language=langs['tr'],
            defaults={
                'name': 'Birleşik Krallık Vize ve Göçmenlik İdaresi (UKVI)',
                'address_text': 'Londra, Birleşik Krallık',
                'working_hours': 'Hafta içi: 09:00 - 17:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # GB Başvuru 1: Skilled Worker Visa
        proc_gb_skilled, _ = Procedure.objects.update_or_create(
            slug='gb-skilled-worker-visa',
            defaults={
                'country': countries['GB'],
                'institution': home_office_uk,
                'category': cats['work-permit'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.gov.uk/skilled-worker-visa',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_skilled,
            language=langs['en'],
            defaults={
                'title': 'Skilled Worker Visa Application',
                'summary': 'Application route for eligible skilled workers from outside the UK with an approved job offer from a licensed Home Office sponsor.',
                'eligibility': '1. Valid Certificate of Sponsorship (CoS) reference number.\n2. Job on the eligible occupations list.\n3. Minimum salary requirement (salary threshold rules apply).\n4. English language proficiency at CEFR B1 level [Sample data — unverified].',
                'required_documents': '• Certificate of Sponsorship (CoS)\n• Current passport\n• Proof of English language proficiency (SELT)\n• Tuberculosis test results (if applying from listed countries)\n• Criminal record certificate (for specific occupations) [Sample data — unverified]',
                'steps': '1. Secure job offer and CoS from licensed employer.\n2. Complete online application on GOV.UK.\n3. Pay visa fee and Immigration Health Surcharge (IHS).\n4. Verify identity via UK Immigration: ID Check app or biometric appointment at TLScontact/VFS.\n5. Receive eVisa status notification [Sample data — unverified].',
                'fees_and_duration': "Fee: £719 to £1,500 depending on duration + £1,035/year IHS surcharge [Sample data — unverified]. Decision: 3-8 weeks.",
                'validity': "Up to 5 years before eligibility for Indefinite Leave to Remain (ILR).",
                'notes': "The UK transition to digital eVisa is active. Biometric Residence Permits (BRP) are replaced by digital status.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_skilled,
            language=langs['tr'],
            defaults={
                'title': 'Birleşik Krallık Nitelikli Çalışan Vizesi (Skilled Worker Visa)',
                'summary': "İngiltere'de onaylı bir işverenden iş teklifi ve sponsorluk belgesi (CoS) alan profesyonellerin çalışma ve oturum vizesi.",
                'eligibility': "Onaylı bir UK sponsorundan iş teklifi, asgari maaş eşiği ve B1 düzeyinde İngilizce yeterliliği [Örnek veri — doğrulanmadı].",
                'required_documents': "CoS numarası, geçerli pasaport, SELT İngilizce sınav sonucu, TB sağlık testi ve birikim kanıtı [Örnek veri — doğrulanmadı].",
                'steps': "İşverenden CoS alma, GOV.UK online başvuru, sağlık katkı payı (IHS) ödeme ve biyometri randevusu.",
                'fees_and_duration': "Vize harcı: £719 - £1.500 + yıllık £1.035 sağlık primi [Örnek veri — doğrulanmadı]. Süre: 3-8 hafta.",
                'validity': "5 yıla kadar verilir; 5 yıl sonunda süresiz oturum (ILR) hakkı doğar.",
                'notes': "Birleşik Krallık'ta artık dijital eVisa sistemine geçilmiştir.",
            }
        )

        # GB Başvuru 2: Standard Visitor Visa (Turist Vizesi)
        proc_gb_visitor, _ = Procedure.objects.update_or_create(
            slug='gb-standard-visitor-visa',
            defaults={
                'country': countries['GB'],
                'institution': home_office_uk,
                'category': cats['visa'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.gov.uk/standard-visitor',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_visitor,
            language=langs['en'],
            defaults={
                'title': 'Standard Visitor Visa (Tourism, Business & Visiting Family)',
                'summary': 'Application to visit the UK for tourism, holidays, visiting family or friends, business meetings, or short courses of study up to 6 months.',
                'eligibility': 'Intend to leave the UK at the end of the visit, show sufficient funds to cover all expenses without public funds, and not intend to work illegally [Sample data — unverified].',
                'required_documents': '• Valid passport with at least 1 blank page\n• Evidence of financial funds (bank statements for last 6 months)\n• Proof of accommodation and travel plans\n• Employment confirmation letter or student certificate [Sample data — unverified]',
                'steps': '1. Complete online visa application on GOV.UK.\n2. Pay visa fee.\n3. Book appointment at local visa application centre (TLScontact / VFS Global).\n4. Attend appointment to submit passport and fingerprints.\n5. Track application and retrieve passport [Sample data — unverified].',
                'fees_and_duration': "Fee: £115 for up to 6 months [Sample data — unverified]. Processing time: 3 weeks.",
                'validity': "Usually valid for 6 months (multiple entry); long-term 2, 5 or 10-year visas available.",
                'notes': "You cannot take paid work or live in the UK through frequent successive visits.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_visitor,
            language=langs['tr'],
            defaults={
                'title': 'Birleşik Krallık Standart Ziyaretçi ve Turist Vizesi (Visitor Visa)',
                'summary': "İngiltere'ye turistik gezi, aile ziyareti veya iş toplantıları amacıyla 6 aya kadar seyahat etmek isteyenlerin başvuru rehberi.",
                'eligibility': "Ziyaret sonunda ülkeden ayrılma niyeti, konaklama ve masrafları karşılayacak yeterli banka birikimi [Örnek veri — doğrulanmadı].",
                'required_documents': "• Geçerli pasaport\n• Son 6 aylık banka hesap dökümü\n• Çalışma ve maaş belgeleri (veya şirket evrakları)\n• Seyahat ve konaklama planı [Örnek veri — doğrulanmadı]",
                'steps': "1. gov.uk/standard-visitor üzerinden form doldurma.\n2. Vize harcının online ödenmesi.\n3. TLScontact / VFS merkezine parmak izi randevusu alınması.\n4. Randevuda evrakların teslimi ve pasaportun onay sonrası teslim alınması [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "6 aylık vize harcı: £115 [Örnek veri — doğrulanmadı]. İşlem süresi: ortalama 3 hafta.",
                'validity': "Genellikle 6 ay çok girişli olarak düzenlenir (2, 5 veya 10 yıllık seçenekler mevcuttur).",
                'notes': "Turist vizesi ile Birleşik Krallık'ta herhangi bir ücretli işte çalışılamaz.",
            }
        )

        # Kurum 2: DVLA
        dvla_uk, _ = Institution.objects.update_or_create(
            country=countries['GB'],
            slug='dvla-uk',
            defaults={
                'website': 'https://www.gov.uk/apply-first-provisional-driving-licence',
                'phone': '+44 300 790 6801 [Sample data — unverified]',
                'email': 'enquiries@dvla.gov.uk [Sample data — unverified]',
                'address': 'Longview Road, Morriston, Swansea, SA6 7JL, United Kingdom',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dvla_uk,
            language=langs['en'],
            defaults={
                'name': 'Driver and Vehicle Licensing Agency (DVLA)',
                'address_text': 'Swansea, United Kingdom',
                'working_hours': 'Monday to Friday: 08:00 - 19:00 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dvla_uk,
            language=langs['tr'],
            defaults={
                'name': 'Birleşik Krallık Sürücü ve Araç Ruhsatlandırma Kurumu (DVLA)',
                'address_text': 'Swansea, Birleşik Krallık',
                'working_hours': 'Hafta içi: 08:00 - 19:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # GB Başvuru 3: Provisional Driving Licence
        proc_gb_driving, _ = Procedure.objects.update_or_create(
            slug='gb-provisional-driving-licence',
            defaults={
                'country': countries['GB'],
                'institution': dvla_uk,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.gov.uk/apply-first-provisional-driving-licence',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_driving,
            language=langs['en'],
            defaults={
                'title': 'Apply for your first provisional driving licence',
                'summary': 'Official process to obtain a Great Britain provisional driving licence to start learning to drive a car or ride a motorcycle.',
                'eligibility': 'At least 15 years and 9 months old, resident in Great Britain, can read a number plate from 20 metres away [Sample data — unverified].',
                'required_documents': '• Identity document (UK biometric passport or share code)\n• National Insurance number (if known)\n• Addresses where you have lived for the last 3 years [Sample data — unverified]',
                'steps': '1. Apply online via GOV.UK using your Government Gateway account.\n2. Pay the application fee securely online.\n3. Provide identity details digitally or send required documents by post.\n4. Receive green provisional photocard licence by post [Sample data — unverified].',
                'fees_and_duration': "Online fee: £34 (or £43 by post) [Sample data — unverified]. Delivery within 1-2 weeks.",
                'validity': "Valid until you reach the age of 70 (photocard renewed every 10 years).",
                'notes': "With a provisional licence, you must display 'L' plates and be accompanied by a qualified driver at all times until passing the practical driving test.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_driving,
            language=langs['tr'],
            defaults={
                'title': 'İngiltere İlk Sürücü Öğrenci Belgesi (Provisional Driving Licence)',
                'summary': "Birleşik Krallık'ta araç sürmeyi öğrenmek ve sürücü sınavlarına girebilmek için alınan yeşil renkli ön ehliyet başvuru süreci.",
                'eligibility': "En az 15 yıl 9 aylık olmak ve Birleşik Krallık'ta yerleşik ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "• Kimlik belgesi (Biyometrik pasaport veya dijital share code)\n• Son 3 yıllık Birleşik Krallık adres geçmişi\n• Varsa National Insurance (NI) numarası [Örnek veri — doğrulanmadı]",
                'steps': "1. gov.uk/apply-first-provisional-driving-licence üzerinden online form doldurma.\n2. Kart ile harç ödemesi yapma.\n3. Kimlik doğrulama adımını tamamlama.\n4. 1-2 hafta içinde ehliyetin posta kutusuna gelmesi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Online başvuru ücreti: £34 [Örnek veri — doğrulanmadı]. Teslimat süresi: 1-2 hafta.",
                'validity': "70 yaşına kadar geçerlidir (kart üzerindeki fotoğraf 10 yılda bir yenilenir).",
                'notes': "Asıl ehliyet sınavını geçene kadar araca 'L' levhası takılması ve yanınızda tecrübeli sürücü bulunması zorunludur.",
            }
        )

        # Kurum 3: Department for Education & Local Authorities
        dfe_uk, _ = Institution.objects.update_or_create(
            country=countries['GB'],
            slug='dfe-local-authorities-uk',
            defaults={
                'website': 'https://www.gov.uk/schools-admissions',
                'phone': '+44 370 000 2288 [Sample data — unverified]',
                'email': 'contact@education.gov.uk [Sample data — unverified]',
                'address': 'Sanctuary Buildings, Great Smith Street, London, SW1P 3BT, United Kingdom',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dfe_uk,
            language=langs['en'],
            defaults={
                'name': 'Department for Education & Local Councils (School Admissions)',
                'address_text': 'London, United Kingdom',
                'working_hours': 'Monday to Friday: 08:30 - 17:00 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dfe_uk,
            language=langs['tr'],
            defaults={
                'name': 'Birleşik Krallık Eğitim Bakanlığı ve Yerel Belediyeler (Local Council)',
                'address_text': 'Londra, Birleşik Krallık',
                'working_hours': 'Hafta içi: 08:30 - 17:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # GB Başvuru 4: Primary School Admission
        proc_gb_primary, _ = Procedure.objects.update_or_create(
            slug='gb-primary-school-admission',
            defaults={
                'country': countries['GB'],
                'institution': dfe_uk,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.gov.uk/schools-admissions',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_primary,
            language=langs['en'],
            defaults={
                'title': 'Apply for a primary school place (Reception Class)',
                'summary': 'Application to your local council for a primary school reception class place for children turning 4 before 1 September.',
                'eligibility': 'Children resident in the council borough reaching compulsory school age [Sample data — unverified].',
                'required_documents': '• Child birth certificate or passport\n• Council Tax bill as proof of address\n• Recent utility bills\n• Completed eAdmissions application form [Sample data — unverified]',
                'steps': '1. Research primary schools in your local borough.\n2. Apply online through your council eAdmissions portal by 15 January.\n3. List up to 3 to 6 preferred schools in priority order.\n4. Receive national offer day results on 16 April.\n5. Accept offer online within the designated timeframe [Sample data — unverified].',
                'fees_and_duration': 'State school admission is free of charge.',
                'validity': 'Valid for the full 7-year primary phase (Reception through Year 6).',
                'notes': 'Catchment area and siblings attending the school are critical criteria for oversubscribed primary schools.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_primary,
            language=langs['tr'],
            defaults={
                'title': 'İngiltere İlkokul (Reception) Kayıt ve Yerleştirme Başvurusu',
                'summary': "Birleşik Krallık'ta 4 yaşını dolduran çocukların yerel belediye (Council / eAdmissions) aracılığıyla ilkokul hazırlık sınıfına kayıt süreci.",
                'eligibility': "İlgili belediye sınırlarında ikamet etmek ve çocuğun 1 Eylül'den önce 4 yaşına basmış olması [Örnek veri — doğrulanmadı].",
                'required_documents': "• Çocuğun doğum belgesi veya pasaportu\n• Council Tax belediye vergi dökümü (adres kanıtı)\n• Son 3 aya ait fatura [Örnek veri — doğrulanmadı]",
                'steps': "1. 15 Ocak tarihine kadar bağlı olunan belediyenin eAdmissions portalından başvuru yapılması.\n2. Öncelik sırasına göre okul tercihlerinin sıralanması.\n3. 16 Nisan Ulusal Teklif Günü'nde (National Offer Day) sonucun açıklanması.\n4. Teklifin sistemden kabul edilmesi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet okullarında kayıt tamamen ücretsizdir.",
                'validity': "Reception sınıfından 6. sınıfa kadar geçerlidir.",
                'notes': "Talep gören okullarda evin okula olan yürüme mesafesi (catchment area) belirleyici rol oynar.",
            }
        )

        # GB Başvuru 5: Secondary School Admission (Lise Geçişi / Year 7)
        proc_gb_secondary, _ = Procedure.objects.update_or_create(
            slug='gb-secondary-school-admission',
            defaults={
                'country': countries['GB'],
                'institution': dfe_uk,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.gov.uk/schools-admissions',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_secondary,
            language=langs['en'],
            defaults={
                'title': 'Apply for a secondary school place (Year 7 Transfer)',
                'summary': 'Application process for children in Year 6 transferring to secondary school (comprehensive schools or grammar schools via 11-plus test).',
                'eligibility': 'Children resident in the UK completing Year 6 of primary education [Sample data — unverified].',
                'required_documents': '• Council Tax statement\n• Proof of child address\n• 11-Plus examination score certificate (if applying to selective grammar schools) [Sample data — unverified]',
                'steps': '1. Sit for the 11-Plus test in September (if grammar schools are targeted).\n2. Submit secondary school preferences via local council portal by 31 October deadline.\n3. Allocation processing by local authority admissions teams.\n4. National Offer Day on 1 March.\n5. Confirm placement acceptance [Sample data — unverified].',
                'fees_and_duration': 'Free of charge in state-funded schools.',
                'validity': 'Valid for secondary education through GCSEs (Years 7 to 11) and Sixth Form.',
                'notes': 'The 31 October deadline is strictly enforced nationwide.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_secondary,
            language=langs['tr'],
            defaults={
                'title': 'İngiltere Ortaokul ve Lise Geçiş Başvurusu (Secondary School - Year 7)',
                'summary': "İlkokul 6. sınıf öğrencilerinin Secondary School ve Grammar School'lara yerleştirilmesi için yapılan resmi başvuru süreci.",
                'eligibility': "İlkokul 6. sınıfta öğrenci olmak ve İngiltere'de ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "• İkametgâh kanıtı (Council tax faturası)\n• Varsa 11-Plus sınav sonuç belgesi (Grammar okul adayları için) [Örnek veri — doğrulanmadı]",
                'steps': "1. Grammar school hedefleniyorsa eylül ayında 11-Plus sınavına girilmesi.\n2. 31 Ekim'e kadar yerel belediye portalından okul tercihlerinin yapılması.\n3. 1 Mart Ulusal Teklif Günü'nde sonucun öğrenilmesi ve kabul edilmesi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Devlet okullarında yerleştirme ve eğitim ücretsizdir.",
                'validity': "GCSE sınavlarına kadar 5 yıllık lise dönemi boyunca geçerlidir.",
                'notes': "31 Ekim son başvuru tarihi ülke genelinde kesinlikle esnetilmez.",
            }
        )

        # Kurum 4: UCAS
        ucas_uk, _ = Institution.objects.update_or_create(
            country=countries['GB'],
            slug='ucas-uk',
            defaults={
                'website': 'https://www.ucas.com',
                'phone': '+44 330 3330 230 [Sample data — unverified]',
                'email': 'enquiries@ucas.ac.uk [Sample data — unverified]',
                'address': 'Rosehill, New Court Road, Cheltenham, GL52 3LZ, United Kingdom',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ucas_uk,
            language=langs['en'],
            defaults={
                'name': 'Universities and Colleges Admissions Service (UCAS)',
                'address_text': 'Cheltenham, United Kingdom',
                'working_hours': 'Monday to Friday: 08:30 - 18:00 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ucas_uk,
            language=langs['tr'],
            defaults={
                'name': 'UCAS — Birleşik Krallık Üniversiteler Merkezi Başvuru Servisi',
                'address_text': 'Birleşik Krallık',
                'working_hours': 'Hafta içi: 08:30 - 18:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # GB Başvuru 6: UCAS Lisans Başvurusu
        proc_gb_ucas, _ = Procedure.objects.update_or_create(
            slug='gb-ucas-undergraduate-application',
            defaults={
                'country': countries['GB'],
                'institution': ucas_uk,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.ucas.com/undergraduate',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_ucas,
            language=langs['en'],
            defaults={
                'title': 'UCAS Undergraduate University Application',
                'summary': 'Centralized application process for domestic and international students applying to undergraduate degree courses at UK universities.',
                'eligibility': 'Completion of A-levels, International Baccalaureate (IB), or equivalent international high school diplomas with required grades [Sample data — unverified].',
                'required_documents': '• Academic qualifications and predicted grades\n• Personal Statement\n• Academic reference letter\n• English language test results (IELTS Academic / TOEFL) [Sample data — unverified]',
                'steps': '1. Register on UCAS Hub and choose up to 5 course choices.\n2. Write your personal statement explaining course motivation.\n3. Add academic referee and get predicted grades submitted.\n4. Submit before the January equal consideration deadline (October for Oxford, Cambridge, and medicine courses).\n5. Review university offers (conditional/unconditional) and select firm and insurance choices [Sample data — unverified].',
                'fees_and_duration': "Application fee: £28.50 for up to 5 choices [Sample data — unverified].",
                'validity': "Valid for the academic intake year beginning September/October.",
                'notes': 'Unplaced applicants can enter UCAS Extra from February or UCAS Clearing from July.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_gb_ucas,
            language=langs['tr'],
            defaults={
                'title': 'UCAS ile İngiltere Üniversite Lisans Başvurusu',
                'summary': "Birleşik Krallık üniversitelerinde (Oxford, Cambridge, Russell Group dahil) lisans eğitimi almak isteyen tüm adayların merkezi başvuru süreci.",
                'eligibility': "Lise diploması veya uluslararası bakalorya (IB, A-Level) ve ilgili üniversitenin aradığı not ortalaması ile IELTS dil puanı [Örnek veri — doğrulanmadı].",
                'required_documents': "• Lise transkripti ve beklenen notlar (predicted grades)\n• Niyet mektubu (Personal Statement)\n• Akademik referans mektubu\n• IELTS sınav sonucu [Örnek veri — doğrulanmadı]",
                'steps': "1. UCAS Hub üzerinde hesap açıp en fazla 5 bölüm tercihi seçme.\n2. Personal Statement niyet mektubunu sisteme girme.\n3. Referans mektubunu ekleyip son başvuru tarihinden önce (Ocak sonu) gönderme.\n4. Üniversitelerden gelen şartlı/şartsız kabul tekliflerini inceleyip asıl (Firm) ve yedek (Insurance) seçme [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Başvuru ücreti: £28,50 (5 tercih için) [Örnek veri — doğrulanmadı].",
                'validity': "İlgili öğretim yılı sonbahar dönemi için geçerlidir.",
                'notes': "Doğrudan kabul alamayan adaylar temmuz ayında UCAS Clearing sistemini kullanabilir.",
            }
        )

        # =====================================================================
        # 4.5 KANADA (CA)
        # =====================================================================
        # Kurum 1: IRCC
        ircc_ca, _ = Institution.objects.update_or_create(
            country=countries['CA'],
            slug='ircc-canada',
            defaults={
                'website': 'https://www.canada.ca/en/immigration-refugees-citizenship.html',
                'phone': '+1 888 242 2100 [Sample data — unverified]',
                'email': 'question@cic.gc.ca [Sample data — unverified]',
                'address': '365 Laurier Avenue West, Ottawa, Ontario, K1A 1L1, Canada',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ircc_ca,
            language=langs['en'],
            defaults={
                'name': 'Immigration, Refugees and Citizenship Canada (IRCC)',
                'address_text': 'Ottawa, Ontario, Canada',
                'working_hours': 'Monday to Friday: 8am to 4pm EST [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ircc_ca,
            language=langs['fr'],
            defaults={
                'name': 'Immigration, Réfugiés et Citoyenneté Canada (IRCC)',
                'address_text': 'Ottawa, Ontario, Canada',
                'working_hours': 'Lundi au vendredi : 8h à 16h HNE [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ircc_ca,
            language=langs['tr'],
            defaults={
                'name': 'Kanada Göçmenlik, Mültecilik ve Vatandaşlık Bakanlığı (IRCC)',
                'address_text': 'Ottawa, Kanada',
                'working_hours': 'Hafta içi: 08:00 - 16:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # CA Başvuru 1: Study Permit
        proc_ca_study, _ = Procedure.objects.update_or_create(
            slug='ca-study-permit-ogrenci-izni',
            defaults={
                'country': countries['CA'],
                'institution': ircc_ca,
                'category': cats['visa'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit.html',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_study,
            language=langs['en'],
            defaults={
                'title': 'Study Permit Application (IMM 1294)',
                'summary': 'Document issued by IRCC that allows foreign nationals to study at designated learning institutions (DLI) in Canada.',
                'eligibility': 'Acceptance letter from a DLI, provincial attestation letter (PAL), and proof of minimum living funds (20,635 CAD/year) [Sample data — unverified].',
                'required_documents': '• Letter of Acceptance (LOA)\n• Provincial Attestation Letter (PAL)\n• Proof of financial support (GIC or bank statements)\n• Valid passport\n• Statement of purpose [Sample data — unverified]',
                'steps': '1. Get accepted by a DLI and secure PAL.\n2. Apply online through the IRCC secure portal.\n3. Pay processing and biometrics fees.\n4. Give fingerprints and photo at a VAC.\n5. Receive letter of introduction and travel to Canada [Sample data — unverified].',
                'fees_and_duration': "Processing fee: 150 CAD + 85 CAD biometrics [Sample data — unverified]. Processing time: 6-12 weeks.",
                'validity': "Valid for the duration of the study program plus 90 extra days.",
                'notes': "Eligible students can work off-campus up to 24 hours per week during regular academic sessions.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_study,
            language=langs['tr'],
            defaults={
                'title': 'Kanada Öğrenci Vizesi ve İzni (Study Permit)',
                'summary': "Kanada'daki yetkili eğitim kurumlarında (DLI) 6 aydan uzun süre öğrenim görmek isteyen uluslararası öğrencilerin resmi başvuru süreci.",
                'eligibility': "Kanada DLI kurumundan kabul mektubu (LOA), eyalet onay mektubu (PAL) ve yıllık en az 20.635 CAD yaşam masrafı kanıtı [Örnek veri — doğrulanmadı].",
                'required_documents': "Kabul mektubu, PAL mektubu, pasaport, banka teminatı/GIC belgesi, niyet mektubu ve biyometri belgesi [Örnek veri — doğrulanmadı].",
                'steps': "1. Okuldan kabul ve PAL alın.\n2. canada.ca üzerinden IRCC portalında başvuru oluşturun.\n3. Harçları ödeyip VFS Global'de parmak izi verin.\n4. Onay mektubuyla Kanada'ya seyahat edin [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Harç: 150 CAD + 85 CAD biyometri [Örnek veri — doğrulanmadı]. Süre: 6-12 hafta.",
                'validity': "Eğitim süresi artı 90 gün geçerlidir.",
                'notes': "Dönem içinde haftalık 24 saate kadar yasal kampüs dışı çalışma izni verir.",
            }
        )

        doc_ca_study, _ = SampleDocument.objects.update_or_create(
            procedure=proc_ca_study,
            order=1,
            defaults={'storage_path': 'samples/ca_imm1294_study_permit.pdf', 'file_type': 'PDF'}
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_ca_study,
            language=langs['en'],
            defaults={
                'title': 'IMM 1294 Application for a Study Permit Made Outside of Canada [Sample]',
                'description': 'Official IRCC standard application document template.',
            }
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_ca_study,
            language=langs['tr'],
            defaults={
                'title': 'Kanada Öğrenci İzni Başvuru Formu (IMM 1294) [Örnek Belge — Doğrulanmadı]',
                'description': 'Kanada dışından yapılan başvurularda doldurulan resmi form örneği.',
            }
        )

        # CA Başvuru 2: Visitor Visa (TRV - Turist Vizesi)
        proc_ca_visitor, _ = Procedure.objects.update_or_create(
            slug='ca-visitor-visa-trv',
            defaults={
                'country': countries['CA'],
                'institution': ircc_ca,
                'category': cats['visa'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/apply-visitor-visa.html',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_visitor,
            language=langs['en'],
            defaults={
                'title': 'Visitor Visa (Temporary Resident Visa - TRV)',
                'summary': 'Official document placed in your passport to show that you meet the requirements to enter Canada as a temporary resident (tourist, visiting family or business).',
                'eligibility': 'Valid travel document, good health, no criminal record, ties to home country (job, home, financial assets), and sufficient funds for visit [Sample data — unverified].',
                'required_documents': '• Valid passport\n• Proof of financial support (bank statements)\n• Purpose of travel itinerary\n• Letter of invitation (if visiting family/friends)\n• Ties to home country documents [Sample data — unverified]',
                'steps': '1. Create an account on the IRCC secure portal.\n2. Fill out form IMM 5257 and upload supporting files.\n3. Pay application and biometrics fees.\n4. Book and attend biometrics appointment at local Visa Application Centre (VAC).\n5. Submit passport upon approval letter [Sample data — unverified].',
                'fees_and_duration': "Fee: 100 CAD per person + 85 CAD biometrics [Sample data — unverified]. Processing time: 3-8 weeks.",
                'validity': "Multiple entry visa usually valid for up to 10 years or until passport expiry date; maximum stay 6 months per visit.",
                'notes': 'Visitors are not allowed to work in Canada without a separate work permit.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_visitor,
            language=langs['tr'],
            defaults={
                'title': 'Kanada Ziyaretçi ve Turist Vizesi (Temporary Resident Visa - TRV)',
                'summary': "Kanada'ya turistik seyahat, aile ziyareti veya ticari görüşmeler amacıyla gitmek isteyenlerin resmi vize başvuru süreci.",
                'eligibility': "Temiz adli sicil kaydı, geçerli pasaport, seyahat masraflarını karşılayacak finansal güç ve menşe ülkeye dönüş bağları [Örnek veri — doğrulanmadı].",
                'required_documents': "• Pasaport\n• Son 4 aylık banka hesap dökümü\n• İşyeri çalışma belgesi ve maaş bordrosu\n• Seyahat planı veya davetiye mektubu [Örnek veri — doğrulanmadı]",
                'steps': "1. canada.ca üzerinden IRCC portalında hesap açma.\n2. IMM 5257 başvuru formunu doldurup evrakları yükleme.\n3. Harç ve biyometri ücretini kartla ödeme.\n4. VFS Global merkezinde parmak izi verme.\n5. Onay mektubu sonrası pasaportu vize basımı için gönderme [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Vize harcı: 100 CAD + biyometri: 85 CAD [Örnek veri — doğrulanmadı]. Süre: 3-8 hafta.",
                'validity': "Pasaport süresine bağlı olarak 10 yıla kadar çok girişli verilir; her girişte en fazla 6 ay kalınabilir.",
                'notes': "Ziyaretçi vizesi Kanada'da çalışma veya sosyal yardım hakkı tanımaz.",
            }
        )

        # Kurum 2: Ontario Ministry of Transportation / DriveTest
        mto_ca, _ = Institution.objects.update_or_create(
            country=countries['CA'],
            slug='mto-drivetest-ontario',
            defaults={
                'website': 'https://drivetest.ca',
                'phone': '+1 888 570 6110 [Sample data — unverified]',
                'email': 'customercomments@drivetest.ca [Sample data — unverified]',
                'address': '777 Bay Street, Toronto, Ontario, M7A 2J8, Canada',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=mto_ca,
            language=langs['en'],
            defaults={
                'name': 'Ministry of Transportation Ontario (MTO) & DriveTest',
                'address_text': 'Toronto, Ontario, Canada',
                'working_hours': 'Monday to Friday: 08:30 - 17:00 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=mto_ca,
            language=langs['tr'],
            defaults={
                'name': 'Kanada Ontario Ulaştırma Bakanlığı & DriveTest Sınav Merkezleri',
                'address_text': 'Ontario, Kanada',
                'working_hours': 'Hafta içi: 08:30 - 17:00 [Örnek veri — doğrulanmadı]',
            }
        )

        # CA Başvuru 3: Ehliyet (Ontario G1 Driver's Licence)
        proc_ca_driver, _ = Procedure.objects.update_or_create(
            slug='ca-ontario-g1-driving-licence',
            defaults={
                'country': countries['CA'],
                'institution': mto_ca,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://drivetest.ca/licences/licence-types/g-licence/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_driver,
            language=langs['en'],
            defaults={
                'title': "Ontario G1 Driving Licence — Knowledge Test",
                'summary': "First step in Ontario's graduated licensing system for passenger cars, entitling the holder to practice driving with a fully licensed driver.",
                'eligibility': 'At least 16 years old, pass an eye test, and pass the written knowledge test about rules of the road and traffic signs [Sample data — unverified].',
                'required_documents': '• Proof of legal identity (passport, Canadian citizenship card, or PR card)\n• Secondary identity document\n• Eye test results (conducted on-site) [Sample data — unverified]',
                'steps': '1. Study the Official MTO Driver Handbook.\n2. Visit a DriveTest centre in person with valid identification.\n3. Take vision screening and pay the Class G1 licensing fee package.\n4. Pass the multiple-choice knowledge test.\n5. Receive temporary paper G1 licence and photocard by mail [Sample data — unverified].',
                'fees_and_duration': "G1 Licence package fee: 159.75 CAD (includes knowledge test and subsequent G2 road test) [Sample data — unverified].",
                'validity': "Valid for up to 5 years under the graduated licensing framework.",
                'notes': 'G1 drivers must maintain a zero blood alcohol level and drive accompanied by a fully licensed driver with at least 4 years driving experience.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_driver,
            language=langs['tr'],
            defaults={
                'title': 'Kanada Ontario G1 Sürücü Belgesi (Ehliyet) Başvurusu',
                'summary': "Kanada Ontario eyaletinde kademeli ehliyet sisteminin ilk adımı olan G1 teorik sınav ve öğrenci sürücü belgesi süreci.",
                'eligibility': "En az 16 yaşında olmak, göz taramasından geçmek ve trafik kuralları teorik sınavını başarmak [Örnek veri — doğrulanmadı].",
                'required_documents': "• Geçerli pasaport veya PR kartı\n• Varsa Türkiye ehliyeti ve konsolosluktan alınmış ehliyet sicil belgesi (deneyim saydırmak için) [Örnek veri — doğrulanmadı]",
                'steps': "1. Resmi Ontario sürücü el kitabına çalışma.\n2. Randevusuz olarak en yakın DriveTest merkezine gitme.\n3. Göz testi ve teorik sınav harcını ödeme.\n4. 40 soruluk çoktan seçmeli teorik sınavı (G1 Knowledge test) tamamlama.\n5. Geçici G1 belgesini alma ve kartın posta ile gelmesi [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "G1 Başvuru ve paket harcı: 159,75 CAD [Örnek veri — doğrulanmadı].",
                'validity': "5 yıl geçerlidir; bu süre zarfında G2 ve tam G sınavlarının tamamlanması gerekir.",
                'notes': "Türkiye'den 2 yıl ve üzeri ehliyeti olanlar deneyim mektubu ile doğrudan G2 veya tam G yol sınavına girebilir.",
            }
        )

        # Kurum 3: TDSB (Toronto District School Board)
        tdsb_ca, _ = Institution.objects.update_or_create(
            country=countries['CA'],
            slug='tdsb-school-board-canada',
            defaults={
                'website': 'https://www.tdsb.on.ca/Find-your/School/Registration',
                'phone': '+1 416 397 3000 [Sample data — unverified]',
                'email': 'registration@tdsb.on.ca [Sample data — unverified]',
                'address': '5050 Yonge Street, Toronto, Ontario, M2N 5N8, Canada',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=tdsb_ca,
            language=langs['en'],
            defaults={
                'name': 'Toronto District School Board (TDSB) — International & Newcomer Admissions',
                'address_text': 'Toronto, Ontario, Canada',
                'working_hours': 'Monday to Friday: 08:30 - 16:30 [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=tdsb_ca,
            language=langs['tr'],
            defaults={
                'name': 'Kanada Toronto Bölge Eğitim Kurulu (TDSB) — Yeni Gelen Öğrenci Kayıt İdaresi',
                'address_text': 'Toronto, Ontario, Kanada',
                'working_hours': 'Hafta içi: 08:30 - 16:30 [Örnek veri — doğrulanmadı]',
            }
        )

        # CA Başvuru 4: İlkokul ve Lise Kaydı (Elementary & High School Registration)
        proc_ca_school, _ = Procedure.objects.update_or_create(
            slug='ca-school-registration-elementary-highschool',
            defaults={
                'country': countries['CA'],
                'institution': tdsb_ca,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.tdsb.on.ca/Find-your/School/Registration',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_school,
            language=langs['en'],
            defaults={
                'title': 'Elementary & High School Registration for Newcomer Families',
                'summary': 'Process for registering children in Canadian publicly funded elementary (Kindergarten to Grade 8) or secondary (Grades 9-12) schools based on residential address.',
                'eligibility': 'Children residing in Ontario with parents holding Canadian citizenship, PR, work permit, or study permit status [Sample data — unverified].',
                'required_documents': '• Proof of child age (birth certificate or passport)\n• Proof of address (lease agreement or utility bill)\n• Immunization record (yellow card)\n• Parent immigration documents (work permit / study permit / PR card)\n• Academic transcripts from previous school [Sample data — unverified]',
                'steps': '1. Locate your home school using the school board address locator.\n2. Complete online student registration form.\n3. Book an appointment at the Newcomer Reception Centre for language and math assessment (for high school students).\n4. Visit the designated school to finalize enrollment [Sample data — unverified].',
                'fees_and_duration': 'Public school education is free for dependents of Canadian citizens, permanent residents, and valid work/study permit holders.',
                'validity': 'Valid for the duration of the student schooling in the designated district.',
                'notes': 'International fee-paying students must apply through the International Students Office prior to school placement.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_school,
            language=langs['tr'],
            defaults={
                'title': 'Kanada İlkokul ve Lise Kayıt Başvurusu (Newcomer Kaydı)',
                'summary': "Kanada'ya yeni taşınan ailelerin çocuklarını adrese dayalı devlet ilk ve ortaöğretim okullarına (Kindergarten - 12. Sınıf) kaydettirme süreci.",
                'eligibility': "Kanada'da ikamet eden vatandaş, daimi ikamet (PR), çalışma izni veya öğrenci izni sahibi ailelerin çocukları [Örnek veri — doğrulanmadı].",
                'required_documents': "• Çocuğun doğum belgesi veya pasaportu\n• İkametgâh kanıtı (kira sözleşmesi, elektrik/gaz faturası)\n• Aşı kartı dökümü (İngilizce)\n• Anne-babanın Kanada yasal statü belgeleri (çalışma izni, vize vb.)\n• Önceki okul karneleri ve transkript [Örnek veri — doğrulanmadı]",
                'steps': "1. Okul kurulu (School Board) web sitesinden adrese bağlı okulu bulma.\n2. Online ön kayıt formunu doldurma.\n3. Lise öğrencileri için Yeni Gelen Kabul Merkezinde (Reception Centre) İngilizce ve matematik seviye tespitine katılma.\n4. Okul idaresine evrakları sunarak ders kaydını tamamlama [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Yasal ikameti olan aileler için devlet okullarında eğitim tamamen ücretsizdir.",
                'validity': "Kayıtlı olunan eğitim bölgesi boyunca geçerlidir.",
                'notes': "Okul yerleşimleri kesinlikle ikamet edilen sokak ve adrese göre belirlenir.",
            }
        )

        # Kurum 4: OUAC
        ouac_ca, _ = Institution.objects.update_or_create(
            country=countries['CA'],
            slug='ouac-universities-canada',
            defaults={
                'website': 'https://www.ouac.on.ca',
                'phone': '+1 519 823 1063 [Sample data — unverified]',
                'email': 'undergrad-support@ouac.on.ca [Sample data — unverified]',
                'address': '170 Stone Road West, Guelph, Ontario, N1G 5L3, Canada',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ouac_ca,
            language=langs['en'],
            defaults={
                'name': "Ontario Universities' Application Centre (OUAC)",
                'address_text': 'Guelph, Ontario, Canada',
                'working_hours': 'Monday to Friday: 08:30 - 16:30 EST [Sample data — unverified]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=ouac_ca,
            language=langs['tr'],
            defaults={
                'name': 'OUAC — Kanada Ontario Üniversiteleri Merkezi Başvuru Servisi',
                'address_text': 'Ontario, Kanada',
                'working_hours': 'Hafta içi: 08:30 - 16:30 [Örnek veri — doğrulanmadı]',
            }
        )

        # CA Başvuru 5: OUAC Üniversite Başvurusu
        proc_ca_ouac, _ = Procedure.objects.update_or_create(
            slug='ca-ouac-university-undergraduate-application',
            defaults={
                'country': countries['CA'],
                'institution': ouac_ca,
                'category': cats['education'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 14),
                'official_source_url': 'https://www.ouac.on.ca/apply/undergrad/',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_ouac,
            language=langs['en'],
            defaults={
                'title': 'Undergraduate University Application via OUAC',
                'summary': 'Centralized application service for applying to undergraduate degree programs at Ontario universities (such as University of Toronto, Waterloo, McMaster).',
                'eligibility': 'Ontario high school graduates, Canadian out-of-province applicants, and international high school graduates meeting university admission grade averages [Sample data — unverified].',
                'required_documents': '• Official high school transcripts\n• English language test score (IELTS Academic / TOEFL iBT / Duolingo)\n• Supplementary application essays or portfolios (for selective engineering or business programs) [Sample data — unverified]',
                'steps': '1. Create an OUAC Undergraduate Application account.\n2. Select university programs of interest (minimum 3 selections included in base fee).\n3. Enter academic history and personal details.\n4. Pay application fees online.\n5. Access individual university applicant portals to submit supplementary documents and track admission offers [Sample data — unverified].',
                'fees_and_duration': "Base application fee: 156 CAD (covers initial 3 program choices) + 50 CAD for each additional choice [Sample data — unverified].",
                'validity': "Valid for the Fall academic intake cycle.",
                'notes': 'Equal consideration deadline for Ontario high school students is typically mid-January.',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_ca_ouac,
            language=langs['tr'],
            defaults={
                'title': 'OUAC ile Kanada Üniversite Lisans Başvurusu (Toronto, Waterloo vb.)',
                'summary': "Kanada Ontario eyaletindeki üniversitelere (University of Toronto, Waterloo, McMaster vb.) lisans başvurularının yapıldığı merkezi sistem.",
                'eligibility': "Lise mezuniyeti veya son sınıf öğrencisi olmak, program bazında aranan not ortalamasını ve IELTS/TOEFL dil koşulunu sağlamak [Örnek veri — doğrulanmadı].",
                'required_documents': "• Lise transkripti\n• İngilizce yeterlilik sınav sonucu (IELTS 6.5+ / TOEFL 90+)\n• Varsa bölüm ek formları ve niyet yazıları [Örnek veri — doğrulanmadı]",
                'steps': "1. ouac.on.ca üzerinde lisans başvuru hesabı oluşturma.\n2. İstenen üniversite ve bölümleri seçme (taban ücret 3 tercihi kapsar).\n3. Başvuru harcını kredi kartıyla ödeme.\n4. Üniversitelerin öğrenci portallarına erişip transkript ve ek evrakları yükleme.\n5. Kabul tekliflerini (Offer of Admission) inceleyip kesin onay verme [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Taban başvuru ücreti: 156 CAD (ilk 3 tercih için) + ek tercih başına 50 CAD [Örnek veri — doğrulanmadı].",
                'validity': "Eylül başlangıçlı sonbahar akademik dönemi için geçerlidir.",
                'notes': "Mühendislik ve işletme gibi seçici bölümler için ayrıca video mülakat veya portfolyo istenebilir.",
            }
        )

        # =====================================================================
        # 4.6 SENEGAL (SN) - Pasaport ve Ehliyet
        # =====================================================================
        dtr_sn, _ = Institution.objects.update_or_create(
            country=countries['SN'],
            slug='dtr-senegal',
            defaults={
                'website': 'https://transports.gouv.sn',
                'phone': '+221 33 800 00 00 [Örnek veri — doğrulanmadı]',
                'email': 'contact@dtr.gouv.sn [Örnek veri — doğrulanmadı]',
                'address': 'Dakar, Sénégal [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dtr_sn,
            language=langs['fr'],
            defaults={
                'name': 'Direction des Transports Routiers (DTR)',
                'address_text': 'Avenue Malick Sy, Dakar, Sénégal',
                'working_hours': 'Lundi - Vendredi: 08h00 - 16h30 [Örnek veri — doğrulanmadı]',
            }
        )
        InstitutionTranslation.objects.update_or_create(
            institution=dtr_sn,
            language=langs['tr'],
            defaults={
                'name': 'Senegal Karayolu Taşımacılığı Genel Müdürlüğü (DTR)',
                'address_text': 'Dakar, Senegal',
                'working_hours': 'Hafta içi: 08:00 - 16:30 [Örnek veri — doğrulanmadı]',
            }
        )

        # SN Başvuru 1: Ehliyet
        proc_sn_driver, _ = Procedure.objects.update_or_create(
            slug='sn-permis-de-conduire-b',
            defaults={
                'country': countries['SN'],
                'institution': dtr_sn,
                'category': cats['driving-license'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 10),
                'official_source_url': 'https://transports.gouv.sn/permis',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_sn_driver,
            language=langs['fr'],
            defaults={
                'title': 'Obtention du permis de conduire (Catégorie B)',
                'summary': "Procédure officielle pour l'obtention du premier permis de conduire de catégorie B au Sénégal.",
                'eligibility': "1. Être âgé d'au moins 18 ans révolus.\n2. Résider régulièrement au Sénégal.\n3. Être reconnu médicalement apte [Örnek veri — doğrulanmadı].",
                'required_documents': "• Certificat médical d'aptitude visuelle et physique\n• Copie légalisée de la Carte Nationale d'Identité (CNI)\n• 4 photos d'identité récentes en couleur\n• Certificat de résidence [Örnek veri — doğrulanmadı]",
                'steps': "1. Inscription dans une auto-école agréée.\n2. Examen théorique du code de la route.\n3. Examen pratique de conduite.\n4. Dépôt du dossier au bureau des examens de la DTR.\n5. Retrait du permis probatoire [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Frais officiels : 15 000 - 25 000 FCFA [Örnek veri — doğrulanmadı]. Durée : 1 à 3 mois.",
                'validity': "Permis initial probatoire valable 2 ans, suivi de la validation définitive.",
                'notes': "Les démarches doivent être effectuées auprès des centres agréés de la DTR.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_sn_driver,
            language=langs['tr'],
            defaults={
                'title': 'Senegal B Sınıfı Sürücü Belgesi Başvurusu',
                'summary': "Senegal'de B sınıfı hafif araç sürücü belgesi alma süreci ve resmî koşulları.",
                'eligibility': "18 yaşını doldurmuş olmak ve Senegal'de ikamet etmek [Örnek veri — doğrulanmadı].",
                'required_documents': "Kimlik belgesi, sağlık raporu, 4 adet fotoğraf [Örnek veri — doğrulanmadı].",
                'steps': "Sürücü kursuna kayıt, teorik ve pratik sınavlar, DTR onay süreci.",
                'fees_and_duration': "Yaklaşık 15.000 - 25.000 FCFA. Süre: 1-3 ay [Örnek veri — doğrulanmadı].",
                'validity': "2 yıllık stajyerlik sonrası kalıcı ehliyet.",
                'notes': "Bilgiler Senegal resmî DTR kaynaklarına dayanır.",
            }
        )

        doc_sn, _ = SampleDocument.objects.update_or_create(
            procedure=proc_sn_driver,
            order=1,
            defaults={'storage_path': 'samples/sn_formulaire_demande_permis.pdf', 'file_type': 'PDF'}
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_sn,
            language=langs['fr'],
            defaults={
                'title': 'Formulaire de demande de permis de conduire [Örnek belge — doğrulanmadı]',
                'description': 'Exemple officiel de formulaire à remplir pour le dépôt de dossier.',
            }
        )

        # SN Başvuru 2: Senegal Biyometrik Pasaport
        proc_sn_passport, _ = Procedure.objects.update_or_create(
            slug='sn-passeport-biometrique-ordinaire',
            defaults={
                'country': countries['SN'],
                'institution': dtr_sn,
                'category': cats['passport'],
                'is_published': True,
                'last_verified_at': date(2026, 11, 8),
                'official_source_url': 'https://police.secu.gouv.sn',
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_sn_passport,
            language=langs['fr'],
            defaults={
                'title': 'Demande de passeport biométrique ordinaire de la CEDEAO',
                'summary': "Délivrance du passeport biométrique pour les citoyens sénégalais auprès de la Direction de la Police des Étrangers et des Titres de Voyage (DPETV).",
                'eligibility': "Être de nationalité sénégalaise et titulaire d'une Carte Nationale d'Identité biométrique CEDEAO [Örnek veri — doğrulanmadı].",
                'required_documents': "• Carte Nationale d'Identité biométrique CEDEAO originale et photocopie\n• Reçu de paiement de la quittance fiscale\n• Ancien passeport (en cas de renouvellement)\n• Déclaration de perte légalisée (en cas de perte) [Örnek veri — doğrulanmadı]",
                'steps': "1. Paiement de la quittance du timbre fiscal au Trésor ou en ligne.\n2. Prise de rendez-vous ou dépôt au centre d'enrôlement (Dieuppeul ou commissariats agréés).\n3. Prise de photo et empreintes biométriques.\n4. Retrait du passeport sous 5 à 10 jours ouvrés [Örnek veri — doğrulanmadı].",
                'fees_and_duration': "Quittance fiscale : 20 500 FCFA [Örnek veri — doğrulanmadı]. Délai : 1 à 2 semaines.",
                'validity': "Valable 5 ans pour les adultes et les mineurs.",
                'notes': "Le passeport sénégalais permet de voyager sans visa dans tout l'espace CEDEAO.",
            }
        )
        ProcedureTranslation.objects.update_or_create(
            procedure=proc_sn_passport,
            language=langs['tr'],
            defaults={
                'title': 'Senegal Biyometrik Pasaport (CEDEAO) Başvurusu',
                'summary': "Senegal vatandaşlarının uluslararası seyahatleri için biyometrik pasaport başvuru ve yenileme süreci.",
                'eligibility': "Senegal vatandaşı olmak ve biyometrik kimlik kartına sahip olmak [Örnek veri — doğrulanmadı].",
                'required_documents': "Biyometrik kimlik kartı, vergi makbuzu ve varsa eski pasaport [Örnek veri — doğrulanmadı].",
                'steps': "Vergi makbuzunun ödenmesi, parmak izi verilmesi ve teslimat.",
                'fees_and_duration': "20.500 FCFA. Süre: 1-2 hafta [Örnek veri — doğrulanmadı].",
                'validity': "5 yıl geçerlidir.",
                'notes': "ECOWAS/CEDEAO bölgesinde serbest dolaşım sağlar.",
            }
        )

        doc_sn_passport, _ = SampleDocument.objects.update_or_create(
            procedure=proc_sn_passport,
            order=1,
            defaults={'storage_path': 'samples/sn_recu_quittance_passeport.pdf', 'file_type': 'PDF'}
        )
        SampleDocumentTranslation.objects.update_or_create(
            document=doc_sn_passport,
            language=langs['fr'],
            defaults={
                'title': 'Récépissé de dépôt de passeport biométrique [Exemple de document]',
                'description': 'Exemple de récépissé délivré pour le retrait du titre.',
            }
        )

        # =====================================================================
        # 5. KÜRESEL ÜLKELER (30 YENİ ÜLKE: AVRUPA, AMERİKA, ASYA/OKYANUSYA, ORTA DOĞU/AFRİKA)
        # =====================================================================
        self.stdout.write(self.style.NOTICE("Küresel ülkeler ve prosedürler aktarılıyor..."))
        all_global_datasets = [
            ("Avrupa", EUROPE_COUNTRIES),
            ("Amerika", AMERICAS_COUNTRIES),
            ("Asya & Okyanusya", ASIA_OCEANIA_COUNTRIES),
            ("Orta Doğu & Afrika", MIDEAST_AFRICA_COUNTRIES),
        ]

        total_seeded = 0
        for region_name, country_list in all_global_datasets:
            self.stdout.write(f"\n--- {region_name} Bölgesi ({len(country_list)} Ülke) ---")
            for c_dict in country_list:
                seed_country_dataset(c_dict, langs, cats, stdout=self.stdout)
                total_seeded += 1

        self.stdout.write(self.style.SUCCESS(f"\nToplam {6 + total_seeded} ülke ve tüm prosedürleri başarıyla yüklendi!"))
