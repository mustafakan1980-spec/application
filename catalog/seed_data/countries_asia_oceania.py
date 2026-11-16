# -*- coding: utf-8 -*-
from datetime import date

ASIA_OCEANIA_COUNTRIES = [
    # 1. JAPONYA (JP)
    {
        'country': {
            'iso2': 'JP',
            'slug': 'jp',
            'flag_emoji': '🇯🇵',
            'primary_language': 'ja',
            'official_languages': ['ja', 'en'],
            'translations': {'ja': '日本', 'tr': 'Japonya', 'en': 'Japan', 'fr': 'Japon', 'de': 'Japan'},
        },
        'institutions': [
            {
                'slug': 'moj-isa-japan',
                'website': 'https://www.isa.go.jp/en/',
                'phone': '+81 3 5796 7112 [Sample data — unverified]',
                'email': 'info-tokyo@immi-moj.go.jp [Sample data — unverified]',
                'address': '5-5-30 Konan, Minato-ku, Tokyo 108-8255, Japan',
                'translations': {
                    'ja': {'name': '出入国在留管理庁 (Immigration Services Agency of Japan)', 'address_text': '東京都港区港南5-5-30', 'working_hours': '平日: 09:00 - 16:00'},
                    'en': {'name': 'Immigration Services Agency of Japan (ISA)', 'address_text': 'Tokyo, Japan', 'working_hours': 'Mon-Fri 09:00 - 16:00'},
                    'tr': {'name': 'Japonya Göç Hizmetleri Kurumu (ISA / 入管)', 'address_text': 'Tokyo, Japonya', 'working_hours': 'Hafta içi 09:00 - 16:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'jp-certificate-of-eligibility-coe',
                'category': 'residence-permit',
                'institution_slug': 'moj-isa-japan',
                'official_source_url': 'https://www.isa.go.jp/en/applications/procedures/16-1.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'ja': {
                        'title': '在留資格認定証明書交付申請 (Certificate of Eligibility - CoE)',
                        'summary': "日本への入国・長期滞在（就労、留学、高度専門職等）を希望する外国人が事前に出入国在留管理局から取得する重要証明書。",
                        'eligibility': "日本の受け入れ機関（企業、大学、語学学校等）から正式な内定または入学許可を得ていること [Örnek veri — doğrulanmadı]。",
                        'required_documents': "• 在留資格認定証明書交付申請書\n• 写真（縦4cm×横3cm）\n• 返信用封筒（切手貼付）または電子申請\n• 受入れ機関の法定調書合計表や会社概要\n• 学歴または職歴を証明する資料 [Örnek veri — doğrulanmadı]",
                        'steps': "1. 日本側の受入れ機関（スポンサー）が入管へCoE交付申請を提出。\n2. 出入国在留管理庁による審査。\n3. CoE（原本または電子CoEメール）の交付。\n4. 海外の日本大使館・領事館へビザ申請を提出。\n5. 日本入国時に空港で在留カード（Residence Card）を受領 [Örnek veri — doğrulanmadı]。",
                        'fees_and_duration': "入管へのCoE申請手数料は無料 [Örnek veri — doğrulanmadı]。標準処理期間: 1〜3か月。",
                        'validity': "在留資格認定証明書の有効期間は発行から3か月間（3か月以内に日本へ入国が必要）。",
                        'notes': "電子CoE（メール形式）により、紙の原本郵送を待たずに迅速にビザ申請を行えます。",
                    },
                    'en': {
                        'title': 'Application for Certificate of Eligibility (CoE)',
                        'summary': 'Pre-requisite official certificate issued by Japanese Immigration proving eligibility for a mid-to-long term status of residence (Work, Study, Highly Skilled Professional).',
                        'eligibility': 'Job offer from a registered Japanese entity or formal admission into an accredited Japanese university/school [Sample data — unverified].',
                        'required_documents': '• CoE application form\n• 40mm x 30mm photograph\n• Company category documents and tax records\n• Degree diplomas or resume\n• Return envelope or digital CoE registration [Sample data — unverified]',
                        'steps': '1. Sponsoring organization applies to Regional Immigration Bureau in Japan.\n2. Immigration processes and issues CoE.\n3. Sponsoring entity sends CoE to applicant.\n4. Applicant applies for visa at Japanese Embassy/Consulate in home country.\n5. Land in Japan (Narita/Haneda/Kansai) and receive biometric Residence Card [Sample data — unverified].',
                        'fees_and_duration': 'No immigration fee for CoE issuance [Sample data — unverified]. Processing time: 1-3 months.',
                        'validity': 'Must enter Japan within 3 months of the date of CoE issuance.',
                        'notes': 'Digital CoE via email is now widely accepted at Japanese overseas diplomatic missions.',
                    },
                    'tr': {
                        'title': 'Japonya Uygunluk Belgesi ve Oturum İzni Başvurusu (CoE - 在留資格)',
                        'summary': "Japonya'da çalışmak, üniversite okumak veya yaşamak isteyen yabancıların Japon Göç Bürosu'ndan (Nyukan) alması zorunlu olan resmi uygunluk sertifikası.",
                        'eligibility': "Japonya'daki bir şirketten iş teklifi veya akredite bir üniversiteden kabul mektubu almış olmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• CoE başvuru formu\n• 3x4 cm biyometrik fotoğraf\n• Şirket veya üniversite resmi belgeleri ve vergi dökümleri\n• Üniversite diploması ve özgeçmiş [Örnek veri — doğrulanmadı]",
                        'steps': "1. Japonya'daki işveren veya okulun bölge göç idaresine CoE başvurusu yapması.\n2. 1-3 ay içinde CoE belgesinin çıkması.\n3. Belgeyle Japonya Konsolosluğuna vize başvurusu yapılması.\n4. Japonya havalimanında (Narita, Haneda) girişte çipli Zairyu Card (Oturum Kartı) teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Göç idaresi CoE harcı ücretsizdir. İşlem süresi: 1-3 ay.",
                        'validity': "CoE belgesi düzenlendikten sonra 3 ay içinde Japonya'ya giriş yapılmalıdır.",
                        'notes': "Artık dijital e-CoE sistemiyle orijinal kâğıt beklemeden e-posta onay koduyla vize başvurusu yapılabilmektedir.",
                    }
                }
            }
        ]
    },

    # 2. GÜNEY KORE (KR)
    {
        'country': {
            'iso2': 'KR',
            'slug': 'kr',
            'flag_emoji': '🇰🇷',
            'primary_language': 'ko',
            'official_languages': ['ko', 'en'],
            'translations': {'ko': '대한민국', 'tr': 'Güney Kore', 'en': 'South Korea', 'fr': 'Corée du Sud', 'de': 'Südkorea'},
        },
        'institutions': [
            {
                'slug': 'moj-hikorea',
                'website': 'https://www.hikorea.go.kr',
                'phone': '1345 [Sample data — unverified]',
                'email': 'hikorea@moj.go.kr [Sample data — unverified]',
                'address': 'Mokdongdong-ro 151, Yangcheon-gu, Seoul, Republic of Korea',
                'translations': {
                    'ko': {'name': '법무부 출입국·외인정책본부 (HiKorea)', 'address_text': '서울특별시 양천구 목동동로 151', 'working_hours': '평일 09:00 - 18:00'},
                    'en': {'name': 'Korea Immigration Service (HiKorea)', 'address_text': 'Seoul, South Korea', 'working_hours': 'Mon-Fri 09:00 - 18:00'},
                    'tr': {'name': 'Güney Kore Adalet Bakanlığı Göç İdaresi (HiKorea)', 'address_text': 'Seul, Güney Kore', 'working_hours': 'Hafta içi 09:00 - 18:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'kr-alien-registration-card-arc',
                'category': 'residence-permit',
                'institution_slug': 'moj-hikorea',
                'official_source_url': 'https://www.hikorea.go.kr/info/InfoOrderPageR.pt',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'ko': {
                        'title': '외국인등록증 (Alien Registration Card - ARC) 발급 신청',
                        'summary': "대한민국에 90일 이상 장기 체류하는 외국인이 입국 후 90일 이내에 관할 출입국·외국인관서에 필수로 신청해야 하는 법적 신분증.",
                        'eligibility': "D-2(유학), E-7(특정활동), D-8(투자) 등 장기체류 비자를 소지하고 90일을 초과하여 체류하려는 외국인 [Örnek veri — doğrulanmadı]。",
                        'required_documents': "• 신청서 (통합신청서)\n• 여권 원본 및 사본\n• 표준규격 사진 1매 (3.5cm x 4.5cm)\n• 체류지 입증서류 (임대차계약서 또는 기숙사 입사확인서)\n• 재학증명서 또는 재직증명서 [Örnek veri — doğrulanmadı]",
                        'steps': "1. 하이코리아(hikorea.go.kr)에서 방문예약 신청.\n2. 관할 출입국·외국인청 방문 및 서류 제출.\n3. 지문 및 안면 생체정보 등록.\n4. 심사 후 약 3~4주 뒤 외국인등록증 수령 (우편 또는 방문) [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "수수료: 30,000원 + 카드 발급비 4,000원 (등기 수령 시 배송료 별도) [Örnek veri — doğrulanmadı]。처리기간: 3-4주.",
                        'validity': "부여된 체류자격 및 체류기간에 따라 결정 (통상 1년~3년, 연장 가능).",
                        'notes': "입국일로부터 90일 이내에 등록하지 않으면 출입국관리법에 따라 과태료가 부과됩니다.",
                    },
                    'en': {
                        'title': 'Alien Registration Card (ARC / Foreigner Registration)',
                        'summary': 'Mandatory identification card for foreign nationals staying in South Korea for more than 90 days from the date of entry.',
                        'eligibility': 'Long-term visa holders (D-2 student, E-7 professional, D-8 corporate investor, etc.) residing over 90 days [Sample data — unverified].',
                        'required_documents': '• Integrated application form\n• Passport and visa copy\n• 1 passport color photo (3.5x4.5cm)\n• Proof of residency (lease contract or dorm confirmation)\n• Certificate of enrollment or employment [Sample data — unverified]',
                        'steps': '1. Reserve visiting appointment on HiKorea website.\n2. Attend designated local immigration branch in person.\n3. Register fingerprints and digital facial biometrics.\n4. Pick up or receive smart ARC card by postal delivery [Sample data — unverified].',
                        'fees_and_duration': 'Government fee: 30,000 KRW + card fee: 4,000 KRW [Sample data — unverified]. Processing: 3-4 weeks.',
                        'validity': 'Tied to the authorized period of stay indicated by visa classification.',
                        'notes': 'ARC number is vital in Korea for opening bank accounts, getting a mobile contract, and accessing the National Health Insurance (NHIS).',
                    },
                    'tr': {
                        'title': 'Güney Kore Yabancı Kayıt Kartı (ARC) ve Oturum Başvurusu',
                        'summary': "Güney Kore'de 90 günden uzun kalacak tüm yabancıların (öğrenci, çalışan vb.) ülkeye girişten itibaren 90 gün içinde alması zorunlu olan çipli kimlik kartı (ARC).",
                        'eligibility': "Kore'de 90 günden uzun süreli geçerli vize (D-2, E-7, D-8 vb.) ile bulunmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Standart başvuru formu\n• Pasaport ve Kore vizesi\n• 1 adet biyometrik fotoğraf (3.5x4.5 cm)\n• Kira sözleşmesi veya yurt kabul belgesi (adres kanıtı)\n• Öğrenci belgesi veya şirket çalışma yazısı [Örnek veri — doğrulanmadı]",
                        'steps': "1. HiKorea.go.kr üzerinden randevu alma.\n2. İkamet edilen bölgedeki Göç Ofisine şahsen gidip evrak teslimi.\n3. Parmak izi ve yüz biyometri kaydı.\n4. 3-4 hafta sonra ARC kartının postaneden veya elden teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Başvuru harcı: 30.000 KRW + kart bedeli: 4.000 KRW [Örnek veri — doğrulanmadı]. Süre: 3-4 hafta.",
                        'validity': "Vize süresine bağlı olarak 1-3 yıllık verilir; Kore içinden uzatılabilir.",
                        'notes': "Kore'de telefon hattı, banka hesabı, online alışveriş ve genel sağlık sigortası (NHIS) için ARC numarası zorunludur.",
                    }
                }
            }
        ]
    },

    # 3. SİNGAPUR (SG)
    {
        'country': {
            'iso2': 'SG',
            'slug': 'sg',
            'flag_emoji': '🇸🇬',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Singapore', 'tr': 'Singapur', 'fr': 'Singapour', 'de': 'Singapur'},
        },
        'institutions': [
            {
                'slug': 'mom-singapore',
                'website': 'https://www.mom.gov.sg',
                'phone': '+65 6438 5122 [Sample data — unverified]',
                'email': 'mom_feedback@mom.gov.sg [Sample data — unverified]',
                'address': '18 Havelock Road, Singapore 059764',
                'translations': {
                    'en': {'name': 'Ministry of Manpower (MOM)', 'address_text': 'Singapore', 'working_hours': 'Mon-Fri 08:30 - 17:30'},
                    'tr': {'name': 'Singapur İnsan Gücü Bakanlığı (MOM)', 'address_text': 'Singapur', 'working_hours': 'Hafta içi 08:30 - 17:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'sg-employment-pass-compass',
                'category': 'work-permit',
                'institution_slug': 'mom-singapore',
                'official_source_url': 'https://www.mom.gov.sg/passes-and-permits/employment-pass',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Employment Pass (EP) with COMPASS Framework',
                        'summary': 'Work pass for foreign professionals, managers and executives earning at least $5,000 SGD/month ($5,500 in financial services).',
                        'eligibility': 'Job offer in Singapore, meeting qualifying salary thresholds, and passing the 40-point Complementarity Assessment Framework (COMPASS) covering salary, qualifications, diversity, and local support [Sample data — unverified].',
                        'required_documents': '• Candidate resume and degree verification report from background screening agency\n• Employer registration details\n• Passport particulars page [Sample data — unverified]',
                        'steps': '1. Employer submits application via EP eService on myMOM Portal.\n2. COMPASS scoring evaluated automatically.\n3. In-principle approval (IPA) letter issued within 10 days.\n4. Candidate arrives in Singapore, registers biometrics at Employment Pass Services Centre (EPSC).\n5. Delivery of physical EP card [Sample data — unverified].',
                        'fees_and_duration': '$105 SGD on application + $225 SGD on pass issuance [Sample data — unverified]. Fast processing: 10 business days.',
                        'validity': 'Up to 2 years for first-time candidates, renewable for up to 3 years.',
                        'notes': 'Candidates scoring 40 points across foundational and bonus criteria on COMPASS qualify for EP approval.',
                    },
                    'tr': {
                        'title': 'Singapur Nitelikli Çalışma İzni (Employment Pass — COMPASS)',
                        'summary': "Singapur'da yönetici, mühendis ve uzman pozisyonlarında çalışacak yabancı profesyonellerin puan tabanlı COMPASS sistemiyle çalışma kartı alma süreci.",
                        'eligibility': "Aylık en az 5.000 SGD (finans sektöründe 5.500 SGD) maaş teklifi ve COMPASS puanlama sisteminden en az 40 puan alma [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Özgeçmiş ve uluslararası akredite diploma doğrulama raporu\n• İşverenin resmi Singapur şirket belgeleri\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin myMOM portalı üzerinden online başvuru yapması.\n2. COMPASS sisteminden 40 puan değerlendirmesi.\n3. 10 gün içinde prensip kabul mektubu (IPA) alınması.\n4. Singapur'da EPSC merkezine giderek parmak izi verilmesi.\n5. Kartın adrese teslimi [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Başvuru harcı: 105 SGD + kart harcı: 225 SGD [Örnek veri — doğrulanmadı]. Süre: ortalama 10 iş günü.",
                        'validity': "İlk başvuruda 2 yıla kadar verilir; 3 yıla kadar uzatılabilir.",
                        'notes': "COMPASS sistemi; adayın maaşı, eğitimi, şirketteki ulusal çeşitlilik ve yerel istihdam oranını puanlar.",
                    }
                }
            }
        ]
    },

    # 4. HONG KONG (HK)
    {
        'country': {
            'iso2': 'HK',
            'slug': 'hk',
            'flag_emoji': '🇭🇰',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Hong Kong', 'tr': 'Hong Kong', 'fr': 'Hong Kong', 'de': 'Hongkong'},
        },
        'institutions': [
            {
                'slug': 'immd-hong-kong',
                'website': 'https://www.immd.gov.hk',
                'phone': '+852 2824 6111 [Sample data — unverified]',
                'email': 'enquiry@immd.gov.hk [Sample data — unverified]',
                'address': 'Immigration Tower, 7 Gloucester Road, Wan Chai, Hong Kong',
                'translations': {
                    'en': {'name': 'Immigration Department of Hong Kong (ImmD)', 'address_text': 'Hong Kong', 'working_hours': 'Mon-Fri 08:45 - 17:15'},
                    'tr': {'name': 'Hong Kong Göçmenlik Dairesi (ImmD)', 'address_text': 'Hong Kong', 'working_hours': 'Hafta içi 08:45 - 17:15'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'hk-top-talent-pass-scheme-ttps',
                'category': 'work-permit',
                'institution_slug': 'immd-hong-kong',
                'official_source_url': 'https://www.immd.gov.hk/eng/services/visas/TTPS.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Top Talent Pass Scheme (TTPS)',
                        'summary': 'Fast-track immigration scheme to attract global high-earners and graduates from the world top 100 universities to Hong Kong without prior job offer.',
                        'eligibility': 'Category A: Annual income of HK$2.5 million+; Category B: Degree from top 100 global university + 3 years experience; Category C: Degree from top 100 university within 5 years with less than 3 years experience [Sample data — unverified].',
                        'required_documents': '• Graduation certificate from world top 100 university\n• Tax assessment notices or audited accounts (for Category A)\n• Travel document and passport identification\n• Digital photograph [Sample data — unverified]',
                        'steps': '1. Submit electronic application via GovHK / ImmD portal.\n2. Pay visa fee upon application approval.\n3. Download electronic visa (e-Visa).\n4. Arrive in Hong Kong and register for Hong Kong Identity Card (HKID) [Sample data — unverified].',
                        'fees_and_duration': 'Visa fee: HK$230 [Sample data — unverified]. Rapid processing: 2-4 weeks.',
                        'validity': 'Initial stay of 24 months without needing an employment offer beforehand.',
                        'notes': 'Pass holders are free to work, switch employers, or establish businesses in Hong Kong during the 24-month validity.',
                    },
                    'tr': {
                        'title': 'Hong Kong Üstün Yetenek Vizesi (Top Talent Pass Scheme - TTPS)',
                        'summary': "Hong Kong'da önceden iş bulma şartı aranmaksızın, dünyanın ilk 100 üniversitesi mezunlarına veya yüksek gelirlilere 2 yıl süreli açık çalışma ve oturum izni.",
                        'eligibility': "Dünyanın en iyi ilk 100 üniversitesinden lisans mezunu olmak VEYA yıllık 2.5 milyon HK$ (~320.000 USD) resmi gelire sahip olmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• İlk 100 üniversite diploması ve transkripti\n• Vergi levhası veya maaş bordrosu (Kategori A için)\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. ImmD resmi portalı üzerinden online başvuru yapılması.\n2. 2-4 hafta içinde onay ve elektronik vizenin (e-Visa) indirilmesi.\n3. Hong Kong'a seyahat edip akıllı Hong Kong Kimlik Kartı (HKID) için randevu alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Vize harcı: 230 HK$ [Örnek veri — doğrulanmadı]. Süre: 2-4 hafta.",
                        'validity': "24 ay serbest çalışma ve oturum hakkı sağlar; sonrasında iş bularak uzatılabilir.",
                        'notes': "Hong Kong'da 7 yıl yasal ikamet sonrasında Hong Kong Daimi İkameti (Permanent Residency) kazanılır.",
                    }
                }
            }
        ]
    },

    # 5. AVUSTRALYA (AU)
    {
        'country': {
            'iso2': 'AU',
            'slug': 'au',
            'flag_emoji': '🇦🇺',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Australia', 'tr': 'Avustralya', 'fr': 'Australie', 'de': 'Australien'},
        },
        'institutions': [
            {
                'slug': 'home-affairs-australia',
                'website': 'https://immi.homeaffairs.gov.au',
                'phone': '+61 2 6196 0196 [Sample data — unverified]',
                'email': 'evisa.support@homeaffairs.gov.au [Sample data — unverified]',
                'address': '6 Chan Street, Belconnen ACT 2617, Australia',
                'translations': {
                    'en': {'name': 'Department of Home Affairs', 'address_text': 'Canberra, Australia', 'working_hours': 'Mon-Fri 09:00 - 17:00 AEST'},
                    'tr': {'name': 'Avustralya İçişleri Bakanlığı — Göç Dairesi (Home Affairs)', 'address_text': 'Kanberra, Avustralya', 'working_hours': 'Hafta içi 09:00 - 17:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'au-skilled-independent-visa-subclass-189',
                'category': 'work-permit',
                'institution_slug': 'home-affairs-australia',
                'official_source_url': 'https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-independent-189',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Skilled Independent Visa (Subclass 189 - Points-tested stream)',
                        'summary': 'Permanent residence visa for invited skilled workers who are not sponsored by an employer, state/territory, or family member.',
                        'eligibility': 'Nominated occupation on the relevant Medium and Long-term Strategic Skills List (MLTSSL), suitable skills assessment, minimum 65 points on points test, competent English, under 45 years old [Sample data — unverified].',
                        'required_documents': '• Positive Skills Assessment from relevant assessing body (ACS, Engineers Australia, VETASSESS)\n• English language test report (IELTS/PTE Academic)\n• Expression of Interest (EOI) via SkillSelect\n• Police certificates and health examinations [Sample data — unverified]',
                        'steps': '1. Complete skills assessment and English language test.\n2. Submit Expression of Interest (EOI) on SkillSelect.\n3. Receive formal invitation to apply from Department of Home Affairs.\n4. Lodge visa application online within 60 days of invitation.\n5. Permanent residence granted [Sample data — unverified].',
                        'fees_and_duration': 'Primary applicant fee: AUD 4,770 [Sample data — unverified]. Processing time: 3-9 months.',
                        'validity': 'Permanent residence status with 5-year travel facility.',
                        'notes': 'Live, work, and study anywhere in Australia with access to Medicare public healthcare.',
                    },
                    'tr': {
                        'title': 'Avustralya Bağımsız Nitelikli Göçmen Vizesi (Subclass 189)',
                        'summary': "Avustralya'da işveren veya eyalet sponsorluğuna gerek duymaksızın doğrudan süresiz oturum (Permanent Residency) sağlayan puan tabanlı göçmenlik programı.",
                        'eligibility': "Stratejik Nitelikli Meslekler Listesinde yer almak, mesleki denklik (Skills Assessment) onayı, en az 65 puan, 45 yaş altı olmak ve yetkin İngilizce (IELTS/PTE) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• İlgili Avustralya kurumundan (ACS, Engineers Australia vb.) mesleki denklik belgesi\n• IELTS veya PTE sınav sonuç belgesi\n• SkillSelect EOI kayıt belgesi\n• Adli sicil kaydı ve anlaşmalı hastane sağlık taraması [Örnek veri — doğrulanmadı]",
                        'steps': "1. Mesleki denklik ve İngilizce sınavını tamamlama.\n2. SkillSelect üzerinden niyet bildirimi (EOI) sunma.\n3. Resmi başvuru daveti (ITA) alma.\n4. 60 gün içinde ImmiAccount üzerinden vize dosyasını yükleme.\n5. Süresiz oturumun (PR) onaylanması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Vize harcı: 4.770 AUD [Örnek veri — doğrulanmadı]. Süre: 3-9 ay.",
                        'validity': "Süresiz oturum sağlar; 5 yıllık seyahat hakkı içerir. 4 yıl sonra vatandaşlık başvurusu yapılabilir.",
                        'notes': "Medicare ücretsiz devlet sağlık sisteminden faydalanma hakkı kazandırır.",
                    }
                }
            }
        ]
    },

    # 6. YENİ ZELANDA (NZ)
    {
        'country': {
            'iso2': 'NZ',
            'slug': 'nz',
            'flag_emoji': '🇳🇿',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'New Zealand', 'tr': 'Yeni Zelanda', 'fr': 'Nouvelle-Zélande', 'de': 'Neuseeland'},
        },
        'institutions': [
            {
                'slug': 'immigration-new-zealand',
                'website': 'https://www.immigration.govt.nz',
                'phone': '+64 9 914 4100 [Sample data — unverified]',
                'email': 'nzis@mbie.govt.nz [Sample data — unverified]',
                'address': '15 Stout Street, Wellington 6011, New Zealand',
                'translations': {
                    'en': {'name': 'Immigration New Zealand (INZ)', 'address_text': 'Wellington, New Zealand', 'working_hours': 'Mon-Fri 08:30 - 17:00 NZST'},
                    'tr': {'name': 'Yeni Zelanda Göç İdaresi (INZ)', 'address_text': 'Wellington, Yeni Zelanda', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'nz-skilled-migrant-category-resident-visa',
                'category': 'residence-permit',
                'institution_slug': 'immigration-new-zealand',
                'official_source_url': 'https://www.immigration.govt.nz/new-zealand-visas/visas/visa/skilled-migrant-category-resident-visa',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Skilled Migrant Category Resident Visa (6-Point System)',
                        'summary': 'Permanent residence visa for skilled individuals holding a job or job offer with an accredited employer in New Zealand under the streamlined 6-point system.',
                        'eligibility': 'Must claim 6 points from New Zealand occupational registration, recognized qualifications (Bachelor to PhD), or high income; and hold skilled job offer paying median wage or higher; under 56 years old; English standard met [Sample data — unverified].',
                        'required_documents': '• Job offer from accredited New Zealand employer\n• Qualifications and NZQA International Qualifications Assessment (IQA)\n• English language test certificate\n• Police clearances and medical examinations [Sample data — unverified]',
                        'steps': '1. Check eligibility and calculate 6 points.\n2. Submit Expression of Interest (EOI) online.\n3. Receive Invitation to Apply (ITA).\n4. Submit full resident visa application on Immigration Online.\n5. Resident Visa granted with indefinite stay in NZ [Sample data — unverified].',
                        'fees_and_duration': 'Application fee: NZD $4,290 [Sample data — unverified]. Processing time: 2-6 months.',
                        'validity': 'Permanent residence with 2-year travel condition, convertible to Permanent Resident Visa (PRV).',
                        'notes': 'Accredited Employer Work Visa (AEWV) holders can transition directly once meeting points.',
                    },
                    'tr': {
                        'title': 'Yeni Zelanda 6 Puanlı Nitelikli Göçmen Oturum Vizesi',
                        'summary': "Yeni Zelanda'da akredite bir şirketten iş teklifi alan profesyonellerin sadeleştirilmiş 6 puan sistemiyle doğrudan oturum izni alma süreci.",
                        'eligibility': "Mesleki tescil, üniversite derecesi veya yüksek gelir kriterlerinden toplam 6 puan toplamak, akredite iş teklifi, 55 yaş altı olmak ve IELTS dil puanı [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Akredite işveren iş teklifi belgesi\n• NZQA diploma denklik değerlendirmesi\n• IELTS sınav sonucu\n• Adli sicil ve sağlık raporu [Örnek veri — doğrulanmadı]",
                        'steps': "1. 6 puanı hesaplayıp EOI niyet bildiriminde bulunma.\n2. Başvuru daveti (ITA) alma.\n3. Online vize dosyasını sisteme yükleme.\n4. Oturum vizesinin onaylanması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Vize harcı: 4.290 NZD [Örnek veri — doğrulanmadı]. Süre: 2-6 ay.",
                        'validity': "Süresiz oturum hakkı sağlar; ilk 2 yıl seyahat şartı bulunur, sonrasında kalıcı oturuma (PRV) geçer.",
                        'notes': "Yeni Zelanda'da devlet okulları ve sağlık hizmetlerine yerli statüsünde erişim sağlar.",
                    }
                }
            }
        ]
    },

    # 7. MALEZYA (MY)
    {
        'country': {
            'iso2': 'MY',
            'slug': 'my',
            'flag_emoji': '🇲🇾',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Malaysia', 'tr': 'Malezya', 'fr': 'Malaisie', 'de': 'Malaysia'},
        },
        'institutions': [
            {
                'slug': 'imi-gov-malaysia',
                'website': 'https://esd.imi.gov.my',
                'phone': '+60 3 8880 1442 [Sample data — unverified]',
                'email': 'esdhelpdesk@imi.gov.my [Sample data — unverified]',
                'address': 'No. 15, Tingkat 1-7, (Podium) Persiaran Perdana, Presint 2, 62550 Putrajaya, Malaysia',
                'translations': {
                    'en': {'name': 'Immigration Department of Malaysia (Expatriate Services Division - ESD)', 'address_text': 'Putrajaya, Malaysia', 'working_hours': 'Mon-Fri 08:00 - 17:00'},
                    'tr': {'name': 'Malezya Göçmenlik Dairesi — Yabancı Uzman Hizmetleri (ESD)', 'address_text': 'Putrajaya, Malezya', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'my-employment-pass-category-1-2',
                'category': 'work-permit',
                'institution_slug': 'imi-gov-malaysia',
                'official_source_url': 'https://esd.imi.gov.my/portal/about-us/employment-pass/',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Malaysia Employment Pass (Category I & II)',
                        'summary': 'Work pass issued to expatriates taking up highly skilled positions in registered companies in Malaysia.',
                        'eligibility': 'Category I: Monthly salary of RM 10,000+ (contract up to 5 years); Category II: Monthly salary between RM 5,000 and RM 9,999 (contract up to 2 years) [Sample data — unverified].',
                        'required_documents': '• Employment contract and job description\n• Certified true copies of academic degrees and resume\n• Company ESD registration approval\n• Passport bio-data pages [Sample data — unverified]',
                        'steps': '1. Sponsoring company submits application online via ESD portal.\n2. Approval letter issued within 5-14 working days.\n3. Candidate applies for Single Entry Visa (if visa-required) or enters Malaysia.\n4. Pass endorsement sticker stamped at ESD centre or MYXpats Centre in Kuala Lumpur [Sample data — unverified].',
                        'fees_and_duration': 'Processing fee: RM 800 + Pass fee: RM 150-300/year [Sample data — unverified]. Processing: 2-3 weeks.',
                        'validity': 'Category I valid for up to 5 years; Category II valid for up to 2 years (renewable).',
                        'notes': 'Category I and II pass holders can bring spouses, children, and parents as dependants.',
                    },
                    'tr': {
                        'title': 'Malezya Nitelikli Çalışma İzni (Employment Pass - ESD)',
                        'summary': "Malezya'da faaliyet gösteren uluslararası veya yerel şirketlerde uzman ya da yönetici olarak istihdam edilen profesyonellerin çalışma izni.",
                        'eligibility': "Kategori I için aylık en az 10.000 RM; Kategori II için aylık en az 5.000 RM brüt maaş sözleşmesi [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Noter tasdikli diploma ve özgeçmiş\n• İş sözleşmesi ve şirket ESD onay belgesi\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. Şirketin ESD portalı üzerinden başvuruyu yapması.\n2. 5-14 gün içinde resmi onay mektubu alınması.\n3. Malezya'ya seyahat ve MYXpats merkezinde pasaporta çalışma vizesi etiketinin basılması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "ESD harcı: ~800 RM + yıllık vize harcı: ~200 RM [Örnek veri — doğrulanmadı]. Süre: 2-3 hafta.",
                        'validity': "Kategori I için 5 yıla kadar, Kategori II için 2 yıla kadar verilir.",
                        'notes': "Eş ve çocuklar için Dependant Pass aile vizesi çıkarılmasına olanak tanır.",
                    }
                }
            }
        ]
    },

    # 8. ENDONEZYA (ID)
    {
        'country': {
            'iso2': 'ID',
            'slug': 'id',
            'flag_emoji': '🇮🇩',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Indonesia', 'tr': 'Endonezya', 'fr': 'Indonésie', 'de': 'Indonesien'},
        },
        'institutions': [
            {
                'slug': 'imigrasi-indonesia',
                'website': 'https://evisa.imigrasi.go.id',
                'phone': '+62 21 522 4658 [Sample data — unverified]',
                'email': 'humas@imigrasi.go.id [Sample data — unverified]',
                'address': 'Jl. H.R. Rasuna Said Kav. 8-9, Jakarta Selatan, Indonesia',
                'translations': {
                    'en': {'name': 'Directorate General of Immigration (Ditjen Imigrasi)', 'address_text': 'Jakarta, Indonesia', 'working_hours': 'Mon-Fri 08:00 - 16:00'},
                    'tr': {'name': 'Endonezya Göçmenlik Genel Müdürlüğü (Ditjen Imigrasi)', 'address_text': 'Cakarta, Endonezya', 'working_hours': 'Hafta içi 08:00 - 16:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'id-kitas-limited-stay-permit',
                'category': 'residence-permit',
                'institution_slug': 'imigrasi-indonesia',
                'official_source_url': 'https://evisa.imigrasi.go.id',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Limited Stay Permit (KITAS / ITAS) Application',
                        'summary': 'Residency permit allowing foreign citizens to live in Indonesia for work, remote digital nomad activities (E33G), investment, or retirement.',
                        'eligibility': 'Indonesian sponsor entity (PT PMA for work/investor) or sufficient funds and foreign employment contract (for Remote Worker KITAS E33G) [Sample data — unverified].',
                        'required_documents': '• Valid passport (minimum 18 months validity)\n• Employment contract or proof of foreign remote earnings ($60,000 USD/year for remote worker pass)\n• Bank statement showing minimum $2,000 USD balance\n• Proof of accommodation in Indonesia [Sample data — unverified]',
                        'steps': '1. Apply for electronic visa (e-Visa index E33G or work visa) via evisa.imigrasi.go.id.\n2. Pay visa and processing fees online.\n3. Download approval e-Visa and enter Indonesia.\n4. Attend biometric session at local Immigration Office (Kantor Imigrasi) within 30 days.\n5. Receive electronic KITAS (e-KITAS) [Sample data — unverified].',
                        'fees_and_duration': 'Immigration fees: approx. IDR 10,000,000 - 15,000,000 depending on permit type [Sample data — unverified]. Duration: 2-4 weeks.',
                        'validity': 'Issued for 1 or 2 years, renewable.',
                        'notes': 'The E33G Remote Worker KITAS allows staying in Bali and throughout Indonesia tax-free on foreign income for up to 1 year.',
                    },
                    'tr': {
                        'title': 'Endonezya Geçici Oturum İzni (KITAS / ITAS - Bali Dijital Göçebe)',
                        'summary': "Endonezya'da (özellikle Bali) uzaktan çalışmak, iş kurmak veya yatırım yapmak isteyen yabancıların e-Visa ve KITAS oturum kartı süreci.",
                        'eligibility': "Yurt dışından uzaktan çalışanlar (E33G vizesi) için yıllık asgari 60.000 USD gelir kanıtı veya yerel şirket sponsorluğu [Örnek veri — doğrulanmadı].",
                        'required_documents': "• En az 18 ay geçerli pasaport\n• Son 3 aylık banka hesap dökümü (en az 2.000 USD bakiye)\n• Uzaktan çalışma iş sözleşmesi\n• Endonezya konaklama belgesi [Örnek veri — doğrulanmadı]",
                        'steps': "1. evisa.imigrasi.go.id portalı üzerinden online başvuru yapılması.\n2. Harçların kredi kartıyla ödenmesi ve e-Vize onayının indirilmesi.\n3. Endonezya'ya seyahat edilmesi.\n4. 30 gün içinde yerel göç ofisinde (Kantor Imigrasi) fotoğraf ve parmak izi verilmesi.\n5. e-KITAS oturum belgesinin teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Toplam göç harçları: ~10.000.000 - 15.000.000 IDR (yaklaşık 700-1.000 USD) [Örnek veri — doğrulanmadı]. Süre: 2-4 hafta.",
                        'validity': "1 yıl sürelidir; Endonezya içinden uzatılabilir.",
                        'notes': "E33G dijital göçebe vizesi sahipleri yabancı kaynaklı gelirleri için Endonezya'da yerel gelir vergisinden muaftır.",
                    }
                }
            }
        ]
    }
]
