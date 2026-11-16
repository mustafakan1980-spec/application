# -*- coding: utf-8 -*-
from datetime import date

MIDEAST_AFRICA_COUNTRIES = [
    # 1. SUUDİ ARABİSTAN (SA)
    {
        'country': {
            'iso2': 'SA',
            'slug': 'sa',
            'flag_emoji': '🇸🇦',
            'primary_language': 'ar',
            'official_languages': ['ar', 'en'],
            'translations': {'ar': 'المملكة العربية السعودية', 'tr': 'Suudi Arabistan', 'en': 'Saudi Arabia', 'fr': 'Arabie saoudite', 'de': 'Saudi-Arabien'},
        },
        'institutions': [
            {
                'slug': 'qiwa-jawazat-saudi',
                'website': 'https://qiwa.sa',
                'phone': '19911 [Örnek veri — doğrulanmadı]',
                'email': 'support@qiwa.sa [Örnek veri — doğrulanmadı]',
                'address': 'Riyadh, Kingdom of Saudi Arabia',
                'translations': {
                    'ar': {'name': 'منصة قوى والجوازات (Qiwa & Jawazat)', 'address_text': 'الرياض، المملكة العربية السعودية', 'working_hours': 'الأحد - الخميس: 08:00 - 16:00'},
                    'en': {'name': 'Qiwa Platform & General Directorate of Passports (Jawazat)', 'address_text': 'Riyadh, Saudi Arabia', 'working_hours': 'Sun-Thu 08:00 - 16:00'},
                    'tr': {'name': 'Suudi Arabistan İş Gücü Portalı (Qiwa) ve Göç Dairesi (Jawazat)', 'address_text': 'Riyad, Suudi Arabistan', 'working_hours': 'Pazar - Perşembe: 08:00 - 16:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'sa-iqama-work-residence-permit',
                'category': 'residence-permit',
                'institution_slug': 'qiwa-jawazat-saudi',
                'official_source_url': 'https://qiwa.sa/en/services/work-permit-service',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Iqama (Work and Residence Permit) Issuance via Qiwa & Absher',
                        'summary': 'Mandatory identification and residence card for foreign expatriates employed in the Kingdom of Saudi Arabia.',
                        'eligibility': 'Authenticated electronic employment contract registered on Qiwa platform, passing medical examination (GAMCA / Efada), entry on a valid work visa [Sample data — unverified].',
                        'required_documents': '• Qiwa authenticated electronic contract\n• Medical fitness test report (Efada system)\n• Medical insurance policy compliant with CCHI\n• Valid passport with work visa entry stamp [Sample data — unverified]',
                        'steps': '1. Employer registers contract and issues work permit on Qiwa platform.\n2. Expatriate undergoes medical screening in Saudi Arabia.\n3. Employer pays Jawazat Iqama fee and insurance levy via SADAD banking.\n4. Jawazat issues Muqeem digital residency and physical Iqama card via Absher Individual / Business [Sample data — unverified].',
                        'fees_and_duration': 'Iqama fee: SAR 650/year + Expatriate levy (Maktab Amal fee paid by employer) [Sample data — unverified]. Processing: 1-2 weeks.',
                        'validity': 'Issued for 1 year, renewable annually.',
                        'notes': 'Expatriate workers can transfer sponsorship or exit and re-enter independently through the Labor Reform Initiative on Qiwa/Absher.',
                    },
                    'tr': {
                        'title': 'Suudi Arabistan İkamet ve Çalışma Kartı (Iqama / Qiwa)',
                        'summary': "Suudi Arabistan Krallığı'nda çalışan yabancı profesyonellerin resmi kimlik ve oturum belgesi olan Iqama kartı çıkarma süreci.",
                        'eligibility': "Qiwa portalı üzerinden onaylanmış resmi elektronik iş sözleşmesi, sağlık taraması (Efada) onayı ve çalışma vizesiyle giriş [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Qiwa dijital onaylı iş sözleşmesi\n• Suudi Arabistan içi sağlık tarama raporu (Efada)\n• CCHI onaylı sağlık sigortası\n• Pasaport ve giriş mührü [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin Qiwa platformu üzerinden çalışma iznini (Work permit) onaylaması.\n2. Çalışanın Suudi Arabistan'da sağlık kontrolünden geçmesi.\n3. SADAD bankacılık sistemi üzerinden harçların yatırılması.\n4. Jawazat (Pasaport Dairesi) tarafından Absher üzerinden Iqama kartının basılması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Iqama kart harcı: 650 SAR/yıl + işveren çalışma harçları [Örnek veri — doğrulanmadı]. Süre: 1-2 hafta.",
                        'validity': "1 yıl geçerlidir; her yıl elektronik olarak yenilenir.",
                        'notes': "Iqama olmadan banka hesabı, araç kiralama, ehliyet veya SIM kart işlemleri yapılamaz.",
                    }
                }
            }
        ]
    },

    # 2. BİRLEŞİK ARAP EMİRLİKLERİ (AE)
    {
        'country': {
            'iso2': 'AE',
            'slug': 'ae',
            'flag_emoji': '🇦🇪',
            'primary_language': 'ar',
            'official_languages': ['ar', 'en'],
            'translations': {'ar': 'الإمارات العربية المتحدة', 'tr': 'Birleşik Arap Emirlikleri', 'en': 'United Arab Emirates', 'fr': 'Émirats arabes unis', 'de': 'Vereinigte Arabische Emirate'},
        },
        'institutions': [
            {
                'slug': 'icp-emirates-identity',
                'website': 'https://icp.gov.ae',
                'phone': '600 522222 [Sample data — unverified]',
                'email': 'contact@icp.gov.ae [Sample data — unverified]',
                'address': 'Abu Dhabi, United Arab Emirates',
                'translations': {
                    'ar': {'name': 'الهيئة الاتحادية للهوية والجنسية والجمارك وأمن المنافذ (ICP)', 'address_text': 'أبوظبي، الإمارات العربية المتحدة', 'working_hours': 'الإثنين - الخميس: 07:30 - 15:30'},
                    'en': {'name': 'Federal Authority for Identity, Citizenship, Customs and Port Security (ICP)', 'address_text': 'Abu Dhabi, UAE', 'working_hours': 'Mon-Thu 07:30 - 15:30'},
                    'tr': {'name': 'BAE Federal Kimlik, Vatandaşlık ve Liman Güvenliği Kurumu (ICP)', 'address_text': 'Abu Dabi / Dubai, BAE', 'working_hours': 'Pazartesi - Perşembe: 07:30 - 15:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'ae-golden-visa-10-year-residency',
                'category': 'residence-permit',
                'institution_slug': 'icp-emirates-identity',
                'official_source_url': 'https://u.ae/en/information-and-services/visa-and-emirates-id/residence-visas/golden-visa',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'UAE 10-Year Golden Visa (Investors, Executives & Tech Specialists)',
                        'summary': 'Long-term residency visa allowing foreign talents to live, work, or study in Dubai and the UAE without a local national sponsor.',
                        'eligibility': 'Real estate investors (property worth AED 2 million+), highly qualified executives (monthly basic salary AED 30,000+ with Bachelor degree), tech innovators, or Ph.D. researchers [Sample data — unverified].',
                        'required_documents': '• Valid passport copy\n• Title deed from Dubai Land Department (for property stream) or salary certificate and 6-month bank statements (for executive stream)\n• UAE health insurance policy\n• Medical fitness test certificate [Sample data — unverified]',
                        'steps': '1. Nominate eligibility on ICP or GDRFA portal.\n2. Receive initial approval and 6-month multiple entry visa to finalize procedures.\n3. Complete medical fitness screening and Emirates ID biometrics in the UAE.\n4. Issuance of 10-year digital residency and physical Emirates ID card [Sample data — unverified].',
                        'fees_and_duration': 'Processing fees: approx. AED 2,800 - 4,000 depending on emirate [Sample data — unverified]. Duration: 1-3 weeks.',
                        'validity': '10 years, 100% renewable automatically upon meeting conditions.',
                        'notes': 'Holders can stay outside the UAE for longer than 6 months without invalidating their residency status; includes family and domestic helpers.',
                    },
                    'tr': {
                        'title': 'BAE 10 Yıllık Altın Vize (Golden Visa) Oturum İzni',
                        'summary': "Dubai ve Birleşik Arap Emirlikleri'nde yerel kefil (sponsor) gerekmeden 10 yıl süreyle oturma, çalışma ve şirket kurma hakkı veren prestijli ikamet programı.",
                        'eligibility': "En az 2 milyon AED (~545.000 USD) değerinde gayrimenkul yatırımı VEYA aylık asgari 30.000 AED maaş alan yönetici/mühendis olmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Tapu tescil belgesi (Tapu Dairesi onaylı) veya maaş bordrosu ile banka dökümü\n• Üniversite diploması (Bakanlık onaylı denkliği)\n• BAE sağlık tarama raporu\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. ICP veya GDRFA Dubai sistemi üzerinden ön onay başvurusu.\n2. BAE'de sağlık testi ve Emirates ID parmak izi randevusunu tamamlama.\n3. 10 yıllık oturum vizesinin onaylanması ve Emirates ID kartının teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Toplam işlem harcı: ~2.800 - 4.000 AED [Örnek veri — doğrulanmadı]. Süre: 1-3 hafta.",
                        'validity': "10 yıl geçerlidir; koşullar devam ettikçe 10 yıllık periyotlarla kesintisiz yenilenir.",
                        'notes': "Altın Vize sahipleri BAE dışında 6 aydan uzun süre kalsalar dahi vizeleri iptal olmaz.",
                    }
                }
            }
        ]
    },

    # 3. KATAR (QA)
    {
        'country': {
            'iso2': 'QA',
            'slug': 'qa',
            'flag_emoji': '🇶🇦',
            'primary_language': 'ar',
            'official_languages': ['ar', 'en'],
            'translations': {'ar': 'دولة قطر', 'tr': 'Katar', 'en': 'Qatar', 'fr': 'Qatar', 'de': 'Katar'},
        },
        'institutions': [
            {
                'slug': 'moi-qatar-metrash',
                'website': 'https://portal.moi.gov.qa',
                'phone': '+974 236 6666 [Sample data — unverified]',
                'email': 'info@moi.gov.qa [Sample data — unverified]',
                'address': 'Doha, State of Qatar',
                'translations': {
                    'ar': {'name': 'وزارة الداخلية القطرية (Metrash2 / MOI)', 'address_text': 'الدوحة، دولة قطر', 'working_hours': 'الأحد - الخميس: 07:00 - 14:00'},
                    'en': {'name': 'Ministry of Interior Qatar (MOI & Metrash2)', 'address_text': 'Doha, Qatar', 'working_hours': 'Sun-Thu 07:00 - 14:00'},
                    'tr': {'name': 'Katar İçişleri Bakanlığı — Göç İdaresi (MOI / Metrash2)', 'address_text': 'Doha, Katar', 'working_hours': 'Pazar - Perşembe: 07:00 - 14:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'qa-qatar-id-residence-permit',
                'category': 'residence-permit',
                'institution_slug': 'moi-qatar-metrash',
                'official_source_url': 'https://portal.moi.gov.qa/qatarvisacenter/',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Qatar Residence Permit (QID / QVC Process)',
                        'summary': 'Residency permit card issued by Ministry of Interior for foreign workers under the sponsorship of an employer in Qatar.',
                        'eligibility': 'Official employment contract attested by the Ministry of Labour (MADLSA), biometric and medical clearance at Qatar Visa Centre (QVC) or in Qatar [Sample data — unverified].',
                        'required_documents': '• Valid passport\n• Ministry-attested employment contract\n• Medical commission clearance (blood test & chest X-ray)\n• Criminal clearance certificate [Sample data — unverified]',
                        'steps': '1. Sponsoring employer applies for work entry visa.\n2. Medical and biometric procedures completed at QVC or upon arrival at Medical Commission.\n3. Fingerprint enrollment at CEID (Criminal Evidences and Information Department).\n4. Issuance of official smart Qatar ID (QID) card via Metrash2 [Sample data — unverified].',
                        'fees_and_duration': 'Government fee: approx. QAR 1,000 - 1,200/year (paid by employer) [Sample data — unverified]. Processing: 1-3 weeks.',
                        'validity': 'Issued for 1 to 3 years depending on employer request.',
                        'notes': 'The 11-digit QID number is the primary legal identifier for all government, banking, healthcare, and telecommunication services in Qatar.',
                    },
                    'tr': {
                        'title': 'Katar Oturum İzni ve QID Kimlik Kartı Başvurusu',
                        'summary': "Katar'da istihdam edilen yabancı çalışanların İçişleri Bakanlığı (MOI) ve Metrash2 üzerinden resmi ikamet izni ve akıllı kimlik kartı (QID) alma süreci.",
                        'eligibility': "Çalışma Bakanlığı onaylı resmi iş sözleşmesi, tıbbi komisyon sağlık taraması ve parmak izi onayı [Örnek veri — doğrulanmadı].",
                        'required_documents': "• En az 6 ay geçerli pasaport\n• Onaylı Katar iş sözleşmesi\n• Medical Commission kan ve akciğer tarama raporu\n• Adli sicil belgesi [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin çalışma vizesi çıkarması.\n2. Katar'a varışta Medical Commission sağlık taraması ve CEID parmak izi kaydı.\n3. Metrash2 üzerinden QID kart basım talebi.\n4. QID plastik akıllı kartın teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Resmi harç: ~1.000 QAR/yıl (işveren tarafından karşılanır) [Örnek veri — doğrulanmadı]. Süre: 1-3 hafta.",
                        'validity': "1 ile 3 yıl arasında düzenlenir; sözleşme sürdükçe yenilenir.",
                        'notes': "11 haneli QID numarası Katar'daki tüm bankacılık, sağlık ve resmi işlemlerde kullanılan tek anahtardır.",
                    }
                }
            }
        ]
    },

    # 4. MISIR (EG)
    {
        'country': {
            'iso2': 'EG',
            'slug': 'eg',
            'flag_emoji': '🇪🇬',
            'primary_language': 'ar',
            'official_languages': ['ar', 'en'],
            'translations': {'ar': 'جمهورية مصر العربية', 'tr': 'Mısır', 'en': 'Egypt', 'fr': 'Égypte', 'de': 'Ägypten'},
        },
        'institutions': [
            {
                'slug': 'egypt-evisa-portal',
                'website': 'https://visa2egypt.gov.eg',
                'phone': '+20 2 2795 7229 [Sample data — unverified]',
                'email': 'support@visa2egypt.gov.eg [Sample data — unverified]',
                'address': 'Mugamma El Tahrir / Abbasiya, Cairo, Egypt',
                'translations': {
                    'ar': {'name': 'بوابة التأشيرة الإلكترونية المصرية (مصلحة الجوازات)', 'address_text': 'العباسية، القاهرة، مصر', 'working_hours': 'الأحد - الخميس: 08:30 - 15:00'},
                    'en': {'name': 'Egypt e-Visa Portal & Passports Administration', 'address_text': 'Cairo, Egypt', 'working_hours': 'Sun-Thu 08:30 - 15:00'},
                    'tr': {'name': 'Mısır Elektronik Vize Portalı ve Pasaport İdaresi', 'address_text': 'Kahire, Mısır', 'working_hours': 'Pazar - Perşembe: 08:30 - 15:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'eg-official-evisa-tourism',
                'category': 'visa',
                'institution_slug': 'egypt-evisa-portal',
                'official_source_url': 'https://visa2egypt.gov.eg',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Official Egypt Electronic Tourist Visa (e-Visa)',
                        'summary': 'Official electronic travel authorization system for eligible foreign citizens visiting Egypt for tourism purposes.',
                        'eligibility': 'Citizens of over 70 eligible countries (including EU, UK, US, Canada, Turkey) holding passports with at least 6 months validity [Sample data — unverified].',
                        'required_documents': '• Valid passport with minimum 6 months validity from arrival date\n• Credit/Debit card for online payment\n• Hotel reservation or tourist itinerary\n• Host invitation letter (if visiting relatives) [Sample data — unverified]',
                        'steps': '1. Create account on official portal visa2egypt.gov.eg (beware of imitation copycat sites).\n2. Complete application form with travel and accommodation details.\n3. Pay fee securely online.\n4. Receive approval email and download official PDF e-Visa.\n5. Present printed e-Visa copy at passport control on arrival [Sample data — unverified].',
                        'fees_and_duration': 'Single entry: $25 USD / Multiple entry: $60 USD [Sample data — unverified]. Processing time: 3-7 days.',
                        'validity': 'Single entry valid for 90 days (stay up to 30 days); Multiple entry valid for 180 days.',
                        'notes': 'Always verify that you are on the official government domain visa2egypt.gov.eg to avoid inflated third-party fees.',
                    },
                    'tr': {
                        'title': 'Mısır Resmî Elektronik Turist Vizesi (e-Visa)',
                        'summary': "Mısır'a turistik seyahat gerçekleştirecek Türk ve yabancı vatandaşların resmi kamu portalı üzerinden elektronik vize alma süreci.",
                        'eligibility': "En az 6 ay geçerli pasaporta sahip olmak ve turistik gezi amacı taşımak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Pasaport fotokopisi/taraması\n• Otel rezervasyonu veya seyahat planı\n• Kredi kartı [Örnek veri — doğrulanmadı]",
                        'steps': "1. Resmi visa2egypt.gov.eg portalında hesap açma.\n2. Seyahat ve pasaport bilgilerini doldurma.\n3. 25 $ harcı kartla ödeme.\n4. 3-7 gün içinde onay e-postasını ve barkodlu PDF vizeyi indirme.\n5. Mısır havalimanında pasaport kontrolüne çıktısını ibraz etme [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Tek giriş: 25 $ / Çok giriş: 60 $ [Örnek veri — doğrulanmadı]. Sonuçlanma: 3-7 gün.",
                        'validity': "Tek girişli vize 90 gün geçerlidir; ülkede en fazla 30 gün kalış hakkı tanır.",
                        'notes': "Google aramalarında çıkan yüksek komisyonlu taklit aracı siteler yerine doğrudan resmi devlet sitesi (visa2egypt.gov.eg) kullanılmalıdır.",
                    }
                }
            }
        ]
    },

    # 5. KENYA (KE)
    {
        'country': {
            'iso2': 'KE',
            'slug': 'ke',
            'flag_emoji': '🇰🇪',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Kenya', 'tr': 'Kenya', 'fr': 'Kenya', 'de': 'Kenia'},
        },
        'institutions': [
            {
                'slug': 'ecitizen-immigration-kenya',
                'website': 'https://www.etakenya.go.ke',
                'phone': '+254 110 922 063 [Sample data — unverified]',
                'email': 'support@etakenya.go.ke [Sample data — unverified]',
                'address': 'Nyayo House, Kenyatta Avenue, Nairobi, Kenya',
                'translations': {
                    'en': {'name': 'State Department for Immigration (eCitizen & eTA Kenya)', 'address_text': 'Nairobi, Kenya', 'working_hours': 'Mon-Fri 08:00 - 17:00'},
                    'tr': {'name': 'Kenya Göçmenlik Departmanı — Elektronik Seyahat İdaresi (eTA)', 'address_text': 'Nairobi, Kenya', 'working_hours': 'Hafta içi 08:00 - 17:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'ke-electronic-travel-authorisation-eta',
                'category': 'visa',
                'institution_slug': 'ecitizen-immigration-kenya',
                'official_source_url': 'https://www.etakenya.go.ke',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Kenya Electronic Travel Authorisation (eTA)',
                        'summary': 'Mandatory digital entry authorisation system that replaced traditional paper and eVisa for all international visitors entering Kenya.',
                        'eligibility': 'All foreign nationals traveling to Kenya for tourism, business, conferences, or transit (except citizens of East African Community partner states) [Sample data — unverified].',
                        'required_documents': '• Valid passport (6 months validity)\n• Selfie or passport-type photo\n• Confirmed return or onward airline ticket\n• Hotel booking confirmation or host invitation letter [Sample data — unverified]',
                        'steps': '1. Visit official site etakenya.go.ke or official mobile app.\n2. Upload passport photo page and selfie.\n3. Complete questionnaire with flight and lodging information.\n4. Pay processing fee online.\n5. Receive eTA approval document via email within 72 hours [Sample data — unverified].',
                        'fees_and_duration': 'Standard fee: approx. $32 - $35 USD [Sample data — unverified]. Processing time: up to 72 hours.',
                        'validity': 'Single entry valid for travel up to 90 days from issuance date.',
                        'notes': 'Apply at least 3 days prior to planned departure to avoid boarding denial.',
                    },
                    'tr': {
                        'title': 'Kenya Elektronik Seyahat Yetkilendirmesi (Kenya eTA)',
                        'summary': "Kenya'ya seyahat edecek tüm yabancı yolcuların seyahat öncesinde online olarak alması zorunlu olan yeni nesil dijital giriş izni.",
                        'eligibility': "Kenya'ya turizm, iş veya transit geçiş amacıyla seyahat edecek tüm yabancı ülke vatandaşları [Örnek veri — doğrulanmadı].",
                        'required_documents': "• En az 6 ay geçerli pasaport\n• Biyometrik selfie fotoğraf\n• Gidiş-dönüş uçak bileti\n• Otel rezervasyonu veya davetiye mektubu [Örnek veri — doğrulanmadı]",
                        'steps': "1. etakenya.go.ke resmi adresi üzerinden formu doldurma.\n2. Pasaport ve selfie fotoğrafını yükleme.\n3. Yaklaşık 34 $ başvuru harcını ödeme.\n4. 72 saat içinde e-posta ile onaylanan QR kodlu eTA belgesini alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "eTA işlem ücreti: ~34 $ [Örnek veri — doğrulanmadı]. Sonuçlanma: azami 72 saat.",
                        'validity': "Düzenlendiği tarihten itibaren 90 gün içinde tek giriş için geçerlidir.",
                        'notes': "Uçuşa kabul edilmek için eTA onayının seyahatten en az 3 gün önce alınmış olması gerekir.",
                    }
                }
            }
        ]
    },

    # 6. SUDAN (SD)
    {
        'country': {
            'iso2': 'SD',
            'slug': 'sd',
            'flag_emoji': '🇸🇩',
            'primary_language': 'ar',
            'official_languages': ['ar', 'en'],
            'translations': {'ar': 'جمهورية السودان', 'tr': 'Sudan', 'en': 'Sudan', 'fr': 'Soudan', 'de': 'Sudan'},
        },
        'institutions': [
            {
                'slug': 'passports-civil-sudan',
                'website': 'https://passports.gov.sd',
                'phone': '+249 183 779 990 [Sample data — unverified]',
                'email': 'contact@passports.gov.sd [Sample data — unverified]',
                'address': 'Port Sudan / Khartoum, Sudan',
                'translations': {
                    'ar': {'name': 'الإدارة العامة للجوازات والهجرة والسجل المدني', 'address_text': 'بورتسودان / الخرطوم، السودان', 'working_hours': 'الأحد - الخميس: 08:00 - 15:00'},
                    'en': {'name': 'General Directorate of Passports and Civil Registry', 'address_text': 'Port Sudan / Khartoum, Sudan', 'working_hours': 'Sun-Thu 08:00 - 15:00'},
                    'tr': {'name': 'Sudan Pasaport, Göç ve Nüfus Genel Müdürlüğü', 'address_text': 'Port Sudan / Hartum, Sudan', 'working_hours': 'Pazar - Perşembe: 08:00 - 15:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'sd-biometric-passport-issuance',
                'category': 'passport',
                'institution_slug': 'passports-civil-sudan',
                'official_source_url': 'https://passports.gov.sd',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Sudanese Biometric Electronic Passport Issuance and Renewal',
                        'summary': 'Issuance of the electronic smart passport for Sudanese citizens through civil registry centers and embassies abroad.',
                        'eligibility': 'Sudanese nationality confirmed with National Identification Number (الرقم الوطني) [Sample data — unverified].',
                        'required_documents': '• Original National Identification Number certificate (الرقم الوطني)\n• Previous passport (for renewal) or police report (for lost passport)\n• Fee payment voucher\n• Biometric photograph and fingerprint verification [Sample data — unverified]',
                        'steps': '1. Book appointment at passport issuance center (Port Sudan or designated overseas embassies).\n2. Present National Number certificate and verify civil registry records.\n3. Record biometric photo and fingerprints.\n4. Passport booklet printed and issued [Sample data — unverified].',
                        'fees_and_duration': 'Fees vary according to age and diplomatic mission [Sample data — unverified]. Delivery: 1-4 weeks.',
                        'validity': 'Valid for 10 years for adults (5 years for commercial/business and minors).',
                        'notes': 'Possession of an authenticated Sudanese National ID Number is mandatory before initiating passport procedures.',
                    },
                    'tr': {
                        'title': 'Sudan Biyometrik Pasaport Başvuru ve Yenileme Süreci',
                        'summary': "Sudan vatandaşlarının uluslararası seyahatleri için biyometrik çipli pasaport alma ve yenileme süreci.",
                        'eligibility': "Sudan Ulusal Kimlik Numarasına (الرقم الوطني) sahip olmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Orijinal Ulusal Numara belgesi\n• Varsa eski pasaport veya kayıp tutanağı\n• Harç ödendi makbuzu [Örnek veri — doğrulanmadı]",
                        'steps': "1. Pasaport merkezine (Port Sudan veya yurt dışı elçilikler) başvuru.\n2. Nüfus kaydı doğrulaması.\n3. Parmak izi ve fotoğraf kaydı.\n4. Pasaport defterinin basılması ve teslimi [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Resmi harçlar yaş ve başvuru merkezine göre değişir. Süre: 1-4 hafta [Örnek veri — doğrulanmadı].",
                        'validity': "Yetişkinler için 10 yıl, çocuklar için 5 yıl geçerlidir.",
                        'notes': "Ulusal Numara (National Number) kaydı olmadan pasaport başvurusu yapılamaz.",
                    }
                }
            }
        ]
    },

    # 7. GÜNEY AFRİKA CUMHURİYETİ (ZA)
    {
        'country': {
            'iso2': 'ZA',
            'slug': 'za',
            'flag_emoji': '🇿🇦',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'South Africa', 'tr': 'Güney Afrika Cumhuriyeti', 'fr': 'Afrique du Sud', 'de': 'Südafrika'},
        },
        'institutions': [
            {
                'slug': 'dha-south-africa',
                'website': 'https://www.dha.gov.za',
                'phone': '+27 800 60 11 90 [Sample data — unverified]',
                'email': 'csc@dha.gov.za [Sample data — unverified]',
                'address': 'Hallmark Building, 230 Johannes Ramokhoase St, Pretoria, South Africa',
                'translations': {
                    'en': {'name': 'Department of Home Affairs (DHA)', 'address_text': 'Pretoria, South Africa', 'working_hours': 'Mon-Fri 08:00 - 15:30'},
                    'tr': {'name': 'Güney Afrika İçişleri Bakanlığı (Department of Home Affairs - DHA)', 'address_text': 'Pretorya, Güney Afrika', 'working_hours': 'Hafta içi 08:00 - 15:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'za-critical-skills-work-visa',
                'category': 'work-permit',
                'institution_slug': 'dha-south-africa',
                'official_source_url': 'https://www.dha.gov.za/index.php/types-of-visas/critical-skills-work-visa',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Critical Skills Work Visa (Section 19(4))',
                        'summary': 'Work visa issued to foreign nationals possessing skills or qualifications listed in the South African Critical Skills list, without requiring employer labor certification.',
                        'eligibility': 'Profession featured on national Critical Skills List, foreign degree verified by SAQA, registration with relevant South African statutory professional council [Sample data — unverified].',
                        'required_documents': '• SAQA (South African Qualifications Authority) evaluation certificate\n• Professional body registration certificate or letter\n• Employment offer letter meeting salary benchmarks\n• Police clearances and radiological/medical reports [Sample data — unverified]',
                        'steps': '1. Obtain SAQA evaluation of foreign academic degrees.\n2. Secure professional registration with statutory body.\n3. Lodge application at VFS Global visa facilitation centre or South African embassy.\n4. Biometrics captured and forwarded to DHA.\n5. Receive visa outcome [Sample data — unverified].',
                        'fees_and_duration': 'DHA visa fee: ZAR 1,520 + VFS service fee [Sample data — unverified]. Processing time: 4-12 weeks.',
                        'validity': 'Issued for up to 5 years; provides pathway to permanent residence under Section 27(a).',
                        'notes': 'Applicants with 5 years of relevant post-qualification experience can apply directly for Permanent Residence in South Africa.',
                    },
                    'tr': {
                        'title': 'Güney Afrika Kritik Beceriler Çalışma Vizesi (Critical Skills Work Visa)',
                        'summary': "Güney Afrika'da aranan kritik mesleklerde uzmanlığı olan mühendis, bilim insanı ve profesyonellerin yerel işgücü kısıtlamalarına tabi olmadan çalışma izni alma süreci.",
                        'eligibility': "Kritik Beceriler Listesinde yer alan meslek sahibi olmak, SAQA diploma denklik onayı ve ilgili meslek odasına tescil [Örnek veri — doğrulanmadı].",
                        'required_documents': "• SAQA yabancı diploma denklik belgesi\n• Güney Afrika meslek odası (Engineering Council vb.) üyelik belgesi\n• İş teklifi sözleşmesi\n• Polis sabıka kaydı ve akciğer röntgen sağlık raporu [Örnek veri — doğrulanmadı]",
                        'steps': "1. SAQA üzerinden diploma denklik değerlendirmesi alma.\n2. Meslek odası kaydını tamamlama.\n3. VFS Global veya elçilik üzerinden vize dosyasını teslim etme.\n4. DHA incelemesi sonrası 5 yıllık çalışma vizesini alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "DHA harcı: 1.520 ZAR + VFS hizmet bedeli [Örnek veri — doğrulanmadı]. Süre: 4-12 hafta.",
                        'validity': "5 yıla kadar düzenlenir; mezuniyet sonrası 5 yıl kıdemi olanlar doğrudan kalıcı oturuma başvurabilir.",
                        'notes': "İşverenin Çalışma Bakanlığı'ndan zahmetli yerel arama sertifikası (Labor Certificate) alma zorunluluğu yoktur.",
                    }
                }
            }
        ]
    },

    # 8. ZİMBABVE (ZW)
    {
        'country': {
            'iso2': 'ZW',
            'slug': 'zw',
            'flag_emoji': '🇿🇼',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Zimbabwe', 'tr': 'Zimbabve', 'fr': 'Zimbabwe', 'de': 'Simbabwe'},
        },
        'institutions': [
            {
                'slug': 'evisa-immigration-zimbabwe',
                'website': 'https://www.evisa.gov.zw',
                'phone': '+263 242 791 913 [Sample data — unverified]',
                'email': 'admin@evisa.gov.zw [Sample data — unverified]',
                'address': 'Linquenda House, Nelson Mandela Ave, Harare, Zimbabwe',
                'translations': {
                    'en': {'name': 'Department of Immigration Zimbabwe', 'address_text': 'Harare, Zimbabwe', 'working_hours': 'Mon-Fri 08:00 - 16:30'},
                    'tr': {'name': 'Zimbabve Göçmenlik Dairesi (eVisa Zimbabwe)', 'address_text': 'Harare, Zimbabve', 'working_hours': 'Hafta içi 08:00 - 16:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'zw-electronic-visa-evisa',
                'category': 'visa',
                'institution_slug': 'evisa-immigration-zimbabwe',
                'official_source_url': 'https://www.evisa.gov.zw',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Official Zimbabwe e-Visa Application (Tourism & Business)',
                        'summary': 'Electronic visa authorization issued by the Department of Immigration for travelers entering Zimbabwe through international ports of entry.',
                        'eligibility': 'Travelers falling under Category B (visa on arrival/online) or Category C (visa required before travel) holding valid passport [Sample data — unverified].',
                        'required_documents': '• Passport bio-data page (valid at least 6 months)\n• Passport-size photograph\n• Address in Zimbabwe / hotel booking or residential invitation\n• Previous Zimbabwe visas (if any) [Sample data — unverified]',
                        'steps': '1. Register an account on evisa.gov.zw.\n2. Complete application form with travel dates and point of entry.\n3. Upload supporting passport and photo documents.\n4. Receive approval letter by email within 2-3 business days.\n5. Present letter and pay fee at port of entry (Victoria Falls / Harare Airport) or online [Sample data — unverified].',
                        'fees_and_duration': 'Single entry: $30 USD / Double entry: $45 USD [Sample data — unverified]. Processing time: 2-3 working days.',
                        'validity': 'Valid for entry within 3 months; allows stay of up to 30 days for holiday visits.',
                        'notes': 'KAZA Univisa option ($50 USD) is available at Victoria Falls allowing travel between Zimbabwe and Zambia.',
                    },
                    'tr': {
                        'title': 'Zimbabve Resmî Elektronik Vize (eVisa) Başvurusu',
                        'summary': "Zimbabve'ye (Victoria Şelaleleri, safari veya iş) seyahat edecek kişilerin İçişleri Bakanlığı online portalından e-Vize onay mektubu alma süreci.",
                        'eligibility': "En az 6 ay geçerli pasaport ve turistik konaklama belgesi [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Pasaport fotoğraflı sayfası\n• Biyometrik vesikalık fotoğraf\n• Otel rezervasyonu veya davetiye mektubu [Örnek veri — doğrulanmadı]",
                        'steps': "1. evisa.gov.zw üzerinden hesap açma.\n2. Seyahat planı ve giriş kapısını (Harare, Victoria Falls vb.) seçme.\n3. Başvuruyu gönderme.\n4. 2-3 gün içinde e-posta ile onay mektubunu indirme.\n5. Giriş kapısında onay mektubuyla pasaporta vize bastırma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Tek giriş: 30 $ / Çift giriş: 45 $ / KAZA Zambiya-Zimbabve ortak vizesi: 50 $ [Örnek veri — doğrulanmadı]. Süre: 2-3 iş günü.",
                        'validity': "Düzenlendiği tarihten itibaren 3 ay geçerlidir; 30 güne kadar kalış izni verir.",
                        'notes': "Victoria Şelaleleri'ni gezecekler için hem Zimbabve hem Zambiya'ya geçiş sağlayan KAZA Univisa avantajlıdır.",
                    }
                }
            }
        ]
    }
]
