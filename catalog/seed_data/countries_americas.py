# -*- coding: utf-8 -*-
from datetime import date

AMERICAS_COUNTRIES = [
    # 1. AMERİKA BİRLEŞİK DEVLETLERİ (US)
    {
        'country': {
            'iso2': 'US',
            'slug': 'us',
            'flag_emoji': '🇺🇸',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'United States', 'tr': 'Amerika Birleşik Devletleri', 'fr': 'États-Unis', 'de': 'Vereinigte Staaten'},
        },
        'institutions': [
            {
                'slug': 'state-dept-usa',
                'website': 'https://travel.state.gov',
                'phone': '+1 202 501 4444 [Sample data — unverified]',
                'email': 'visas@state.gov [Sample data — unverified]',
                'address': '2201 C St NW, Washington, DC 20520, USA',
                'translations': {
                    'en': {'name': 'U.S. Department of State — Bureau of Consular Affairs', 'address_text': 'Washington, DC, USA', 'working_hours': 'Mon-Fri 08:30 - 17:00 EST'},
                    'tr': {'name': 'ABD Dışişleri Bakanlığı — Konsolosluk İşleri Dairesi', 'address_text': 'Washington, DC, ABD', 'working_hours': 'Hafta içi 08:30 - 17:00'},
                }
            },
            {
                'slug': 'uscis-usa',
                'website': 'https://www.uscis.gov',
                'phone': '+1 800 375 5283 [Sample data — unverified]',
                'email': 'contact@uscis.dhs.gov [Sample data — unverified]',
                'address': '5900 Capital Gateway Dr, Camp Springs, MD 20746, USA',
                'translations': {
                    'en': {'name': 'U.S. Citizenship and Immigration Services (USCIS)', 'address_text': 'Washington, DC, USA', 'working_hours': 'Mon-Fri 08:00 - 17:00 EST'},
                    'tr': {'name': 'ABD Vatandaşlık ve Göçmenlik Hizmetleri (USCIS)', 'address_text': 'Washington, DC, ABD', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'us-b1-b2-visitor-visa',
                'category': 'visa',
                'institution_slug': 'state-dept-usa',
                'official_source_url': 'https://travel.state.gov/content/travel/en/us-visas/tourism-visit/visitor.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'B1/B2 Visitor Visa for Business or Tourism',
                        'summary': 'Nonimmigrant visa for persons entering the United States temporarily for business (B-1) or pleasure/tourism (B-2).',
                        'eligibility': 'Intend to remain temporarily, demonstrate residence outside US and binding ties to home country, have sufficient funds to cover expenses [Sample data — unverified].',
                        'required_documents': '• Nonimmigrant Visa Electronic Application (DS-160) Confirmation\n• Valid passport (6 months beyond intended stay)\n• 1 photo 2x2 inches (5x5 cm)\n• Interview appointment confirmation page\n• Financial and employment evidence [Sample data — unverified]',
                        'steps': '1. Complete Form DS-160 online on ceac.state.gov.\n2. Pay the non-refundable MRV visa fee.\n3. Schedule embassy/consulate interview on ais.usvisa-info.com.\n4. Attend interview with required documentation and give fingerprints.\n5. Track passport delivery via courier upon approval [Sample data — unverified].',
                        'fees_and_duration': 'Application fee: $185 USD [Sample data — unverified]. Processing time: 2-6 weeks depending on consular interview availability.',
                        'validity': 'Typically issued for up to 10 years (multiple entry); stay granted per visit usually up to 6 months upon admission.',
                        'notes': 'Form DS-160 confirmation barcode number must match the appointment scheduling record.',
                    },
                    'tr': {
                        'title': 'ABD B1/B2 Turist ve Ticari Ziyaretçi Vizesi',
                        'summary': "Amerika Birleşik Devletleri'ne turizm, tatil, aile ziyareti veya iş toplantısı amacıyla seyahat edecek kişilerin B1/B2 vize başvuru rehberi.",
                        'eligibility': "Geçici ziyaret amacı, ülkesine dönme niyetini gösterir bağlar ve masrafları karşılayacak finansal güç [Örnek veri — doğrulanmadı].",
                        'required_documents': "• DS-160 başvuru onay formu barkodu\n• Geçerli pasaport\n• 5x5 cm biyometrik fotoğraf\n• Randevu onay belgesi ve banka hesap dökümleri [Örnek veri — doğrulanmadı]",
                        'steps': "1. ceac.state.gov üzerinden DS-160 formunu doldurma.\n2. 185 USD harç ücretini ödeme.\n3. ais.usvisa-info.com üzerinden mülakat randevusu alma.\n4. Konsoloslukta yüz yüze mülakat ve parmak izi verme.\n5. Onaylanan vizenin PTT/kurye ile teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Vize harcı: 185 $ [Örnek veri — doğrulanmadı]. Süre: Randevu yoğunluğuna göre 2-6 hafta.",
                        'validity': "Genellikle 10 yıllık çok girişli verilir; her girişte I-94 ile 6 aya kadar kalış hakkı tanınır.",
                        'notes': "DS-160 formundaki bilgilerin konsolosluk mülakatında eksiksiz beyan edilmesi zorunludur.",
                    }
                },
                'sample_documents': [
                    {
                        'storage_path': 'samples/us_ds160_confirmation_sample.pdf',
                        'file_type': 'PDF',
                        'translations': {
                            'en': {'title': 'DS-160 Confirmation Page Sample [Sample Document]', 'description': 'Sample barcode confirmation sheet required at the interview.'},
                            'tr': {'title': 'DS-160 Onay Sayfası Örneği [Örnek Belge — Doğrulanmadı]', 'description': 'Konsolosluk mülakatında ibraz edilen örnek barkodlu onay sayfası.'}
                        }
                    }
                ]
            },
            {
                'slug': 'us-f1-student-visa',
                'category': 'education',
                'institution_slug': 'state-dept-usa',
                'official_source_url': 'https://travel.state.gov/content/travel/en/us-visas/study/student-visa.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'F-1 Academic Student Visa Application',
                        'summary': 'Nonimmigrant visa allowing international students to pursue full-time academic studies at SEVP-certified institutions in the US.',
                        'eligibility': 'Acceptance at a SEVP-approved school, Form I-20 issued by the institution, sufficient financial funds to cover tuition and living expenses [Sample data — unverified].',
                        'required_documents': '• Certificate of Eligibility (Form I-20)\n• SEVIS I-901 fee receipt\n• Form DS-160 confirmation\n• Passport and academic transcripts\n• Bank financial support documentation [Sample data — unverified]',
                        'steps': '1. Receive Form I-20 from accepted US college/university.\n2. Pay SEVIS I-901 fee ($350) on fmjfee.com.\n3. Complete DS-160 and pay MRV visa fee ($185).\n4. Schedule and attend visa interview at US Embassy/Consulate.\n5. Travel to US up to 30 days before program start date [Sample data — unverified].',
                        'fees_and_duration': 'SEVIS fee: $350 + MRV visa fee: $185 [Sample data — unverified]. Processing: 2-4 weeks.',
                        'validity': 'Valid for duration of status (D/S) while maintaining full-time student status.',
                        'notes': 'F-1 students are eligible for on-campus employment up to 20 hours/week and Curricular Practical Training (CPT) / Optional Practical Training (OPT).',
                    },
                    'tr': {
                        'title': 'ABD F-1 Akademik Öğrenci Vizesi Başvurusu',
                        'summary': "Amerika Birleşik Devletleri'ndeki üniversite, kolej veya dil okullarında tam zamanlı akademik eğitim alacak uluslararası öğrencilerin vize başvuru süreci.",
                        'eligibility': "SEVP onaylı bir okuldan kabul ve I-20 belgesi alma, eğitim ve yaşam giderlerini karşılayacak finansal güç [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Okuldan alınan I-20 kabul belgesi\n• SEVIS I-901 ücreti ödendi makbuzu (350 $)\n• DS-160 onay sayfası\n• Banka hesap dökümleri ve akademik transkriptler [Örnek veri — doğrulanmadı]",
                        'steps': "1. Okuldan I-20 belgesinin temini.\n2. fmjfee.com üzerinden 350 $ SEVIS harcının ödenmesi.\n3. DS-160 formu ve 185 $ vize harcının ödenmesi.\n4. Konsoloslukta mülakata katılım.\n5. Program başlangıç tarihinden en erken 30 gün önce ABD'ye giriş yapılması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "SEVIS harcı: 350 $ + vize harcı: 185 $ [Örnek veri — doğrulanmadı]. Süre: 2-4 hafta.",
                        'validity': "Eğitim süresince tam zamanlı öğrenci kalındığı sürece (Duration of Status - D/S) geçerlidir.",
                        'notes': "Haftalık 20 saate kadar kampüs içi çalışma ve mezuniyet sonrası 1-3 yıl OPT çalışma hakkı sağlar.",
                    }
                }
            }
        ]
    },

    # 2. MEKSİKA (MX)
    {
        'country': {
            'iso2': 'MX',
            'slug': 'mx',
            'flag_emoji': '🇲🇽',
            'primary_language': 'es',
            'official_languages': ['es'],
            'translations': {'es': 'México', 'tr': 'Meksika', 'en': 'Mexico', 'fr': 'Mexique', 'de': 'Mexiko'},
        },
        'institutions': [
            {
                'slug': 'inm-gob-mexico',
                'website': 'https://www.gob.mx/inm',
                'phone': '+52 800 00 46264 [Örnek veri — doğrulanmadı]',
                'email': 'atencioninm@inami.gob.mx [Örnek veri — doğrulanmadı]',
                'address': 'Homero 1832, Col. Los Morales Polanco, 11510 Ciudad de México, México',
                'translations': {
                    'es': {'name': 'Instituto Nacional de Migración (INM)', 'address_text': 'Ciudad de México, México', 'working_hours': 'Lun-Vie: 09:00 - 15:00'},
                    'tr': {'name': 'Meksika Ulusal Göç Enstitüsü (INM)', 'address_text': 'Meksiko, Meksika', 'working_hours': 'Hafta içi 09:00 - 15:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'mx-residente-temporal-solvencia',
                'category': 'residence-permit',
                'institution_slug': 'inm-gob-mexico',
                'official_source_url': 'https://www.gob.mx/tramites/ficha/expedicion-de-documento-migratorio-por-canje/INM818',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'es': {
                        'title': 'Visa y Tarjeta de Residente Temporal por Solvencia Económica',
                        'summary': "Autorización migratoria que permite residir en México por un periodo superior a 180 días y hasta 4 años a personas con solvencia económica.",
                        'eligibility': "Comprobar inversiones o ahorros bancarios en los últimos 12 meses o ingresos mensuales netos superiores a los umbrales de la UMA (aprox. 3.000 - 4.000 USD/mes) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Formato oficial de solicitud\n• Pasaporte vigente\n• Estados de cuenta bancarios de los últimos 12 meses\n• Pago de derechos migratorios\n• Fotografía tamaño infantil [Örnek veri — doğrulanmadı]",
                        'steps': "1. Cita y entrevista en consulado mexicano en el exterior para emisión de visa en pasaporte.\n2. Entrada a México y sellado de FMM en el aeropuerto.\n3. Trámite de Canje ante el INM dentro de los 30 días posteriores a la llegada.\n4. Toma de datos biométricos y firma.\n5. Entrega de la Tarjeta de Residente Temporal plástica [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Derechos de canje: aprox. 5.108 MXN para 1 año [Örnek veri — doğrulanmadı]. Plazo: 2-4 semanas.",
                        'validity': "1 año renovable por hasta 4 años; a los 4 años se puede solicitar la residencia permanente.",
                        'notes': "El trámite de canje en las oficinas del INM debe iniciarse obligatoriamente dentro de los primeros 30 días naturales de estancia en México.",
                    },
                    'tr': {
                        'title': 'Meksika Geçici İkamet İzni (Residente Temporal) Başvurusu',
                        'summary': "Meksika'da 180 günden uzun süre yasal olarak yaşamak isteyen yabancıların ekonomik yeterlilik veya uzaktan çalışma yoluyla oturum kartı alma süreci.",
                        'eligibility': "Son 12 aya ait banka birikimi kanıtı VEYA aylık düzenli net gelir kanıtı (aylık ~3.000 - 4.000 USD) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Pasaport\n• Son 12 aya ait kaşeli banka hesap dökümleri\n• Başvuru formu ve biyometrik fotoğraf\n• INM harç ödendi makbuzu [Örnek veri — doğrulanmadı]",
                        'steps': "1. Meksika Konsolosluğundan geçici oturum vizesi alma.\n2. Meksika'ya giriş yaparak havalimanında FMM formunu onaylatma.\n3. Girişten itibaren 30 gün içinde INM ofisine 'Canje' (kart değişim) başvurusu yapma.\n4. Parmak izi verme ve yeşil Residente Temporal kartını teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Konsolosluk harcı: 53 $ + INM kart harcı: ~5.108 MXN [Örnek veri — doğrulanmadı]. Süre: 2-4 hafta.",
                        'validity': "İlk yıl 1 yıllık verilir; 4 yıla kadar uzatılabilir. 4 yıl sonunda süresiz oturuma (Residente Permanente) hak kazanılır.",
                        'notes': "Meksika'ya vardıktan sonra 30 gün içinde INM'ye gidilmezse vize geçersiz kalır.",
                    }
                }
            }
        ]
    },

    # 3. BREZİLYA (BR)
    {
        'country': {
            'iso2': 'BR',
            'slug': 'br',
            'flag_emoji': '🇧🇷',
            'primary_language': 'pt',
            'official_languages': ['pt'],
            'translations': {'pt': 'Brasil', 'tr': 'Brezilya', 'en': 'Brazil', 'es': 'Brasil', 'fr': 'Brésil'},
        },
        'institutions': [
            {
                'slug': 'policia-federal-brasil',
                'website': 'https://www.gov.br/pf/pt-br',
                'phone': '+55 61 2024 8000 [Örnek veri — doğrulanmadı]',
                'email': 'atendimento.imigracao@pf.gov.br [Örnek veri — doğrulanmadı]',
                'address': 'SAS Quadra 6 Lotes 9/10, Brasília - DF, 70070-900, Brasil',
                'translations': {
                    'pt': {'name': 'Polícia Federal — Divisão de Imigração', 'address_text': 'Brasília, Brasil', 'working_hours': 'Seg-Sex: 08:00 - 17:00'},
                    'tr': {'name': 'Brezilya Federal Polisi — Göç Dairesi (Polícia Federal)', 'address_text': 'Brasília, Brezilya', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            },
            {
                'slug': 'receita-federal-brasil',
                'website': 'https://www.gov.br/receitafederal/pt-br',
                'phone': '146 [Örnek veri — doğrulanmadı]',
                'email': 'cpf.residente.exterior@rfb.gov.br [Örnek veri — doğrulanmadı]',
                'address': 'Brasília, DF, Brasil',
                'translations': {
                    'pt': {'name': 'Receita Federal do Brasil (RFB)', 'address_text': 'Brasília, Brasil', 'working_hours': 'Seg-Sex: 08:00 - 18:00'},
                    'tr': {'name': 'Brezilya Gelir İdaresi (Receita Federal - CPF)', 'address_text': 'Brezilya', 'working_hours': 'Online ve şube mesaisi'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'br-cpf-cadastro-pessoas-fisicas',
                'category': 'passport',
                'institution_slug': 'receita-federal-brasil',
                'official_source_url': 'https://www.gov.br/pt-br/servicos/inscrever-no-cpf-no-exterior',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'pt': {
                        'title': 'Inscrição no CPF para Estrangeiros (Cadastro de Pessoas Físicas)',
                        'summary': "Registo de identificação tributária fundamental no Brasil para compra de bens, contratação de serviços, abertura de conta bancária e vistos.",
                        'eligibility': "Qualquer cidadão estrangeiro no Brasil ou no exterior que necessite de identificador fiscal para operações econômicas [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Documento de identidade ou passaporte válido\n• Certidão de nascimento ou casamento com filiação\n• Formulário online de inscrição (FCPF)\n• Foto 'selfie' segurando o documento de identidade [Örnek veri — doğrulanmadı]",
                        'steps': "1. Preenchimento do formulário FCPF no portal da Receita Federal.\n2. Envio do formulário com documentos anexos por e-mail à Receita Federal ou apresentação no consulado.\n3. Processamento e atribuição do número de 11 dígitos.\n4. Emissão do comprovante de inscrição no CPF digital [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Gratuito quando solicitado pela internet ou consulado [Örnek veri — doğrulanmadı]. Emissão: 1 a 3 dias úteis.",
                        'validity': "O número de CPF é definitivo e vitalício.",
                        'notes': "O CPF é exigido em praticamente todos os procedimentos burocráticos no Brasil, inclusive para alugar imóveis ou comprar passagens de ônibus.",
                    },
                    'tr': {
                        'title': 'Brezilya Yabancılar İçin Vergi ve Kimlik Numarası (CPF) Başvurusu',
                        'summary': "Brezilya'da banka hesabı açmak, ev kiralamak, telefon hattı almak ve resmi işlem yapabilmek için gereken 11 haneli CPF kimlik numarası.",
                        'eligibility': "Brezilya'da işlem yapacak tüm yabancı ülke vatandaşları (Brezilya'ya gitmeden konsolosluk/online üzerinden de alınabilir) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Geçerli pasaport\n• Doğum belgesi (anne ve baba adını gösteren)\n• Online FCPF başvuru formu\n• Pasaportla çekilmiş selfie fotoğrafı [Örnek veri — doğrulanmadı]",
                        'steps': "1. Receita Federal web sitesinden online formu doldurma.\n2. Evrakları e-posta veya konsolosluk aracılığıyla iletme.\n3. 1-3 gün içinde 11 haneli CPF numarasının atanması ve dijital belgenin indirilmesi [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Online başvurular tamamen ücretsizdir. Süre: 1-3 iş günü.",
                        'validity': "CPF numarası ömür boyu geçerlidir.",
                        'notes': "Brezilya'da SIM kart almaktan market alışverişine kadar her alanda CPF numarası sorulur.",
                    }
                }
            }
        ]
    },

    # 4. ARJANTİN (AR)
    {
        'country': {
            'iso2': 'AR',
            'slug': 'ar',
            'flag_emoji': '🇦🇷',
            'primary_language': 'es',
            'official_languages': ['es'],
            'translations': {'es': 'Argentina', 'tr': 'Arjantin', 'en': 'Argentina', 'fr': 'Argentine', 'de': 'Argentinien'},
        },
        'institutions': [
            {
                'slug': 'migraciones-argentina',
                'website': 'https://www.argentina.gob.ar/interior/migraciones',
                'phone': '+54 11 4317 0200 [Örnek veri — doğrulanmadı]',
                'email': 'info@migraciones.gob.ar [Örnek veri — doğrulanmadı]',
                'address': 'Av. Antártida Argentina 1355, C1104ACA Buenos Aires, Argentina',
                'translations': {
                    'es': {'name': 'Dirección Nacional de Migraciones (DNM)', 'address_text': 'Buenos Aires, Argentina', 'working_hours': 'Lun-Vie: 08:00 - 15:00'},
                    'tr': {'name': 'Arjantin Ulusal Göç Müdürlüğü (DNM - Radex)', 'address_text': 'Buenos Aires, Arjantin', 'working_hours': 'Hafta içi 08:00 - 15:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'ar-radex-residencia-temporaria',
                'category': 'residence-permit',
                'institution_slug': 'migraciones-argentina',
                'official_source_url': 'https://www.argentina.gob.ar/interior/migraciones/radex',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'es': {
                        'title': 'Solicitud de Residencia Temporaria y DNI para Extranjeros (Radex)',
                        'summary': "Sistema digital de radicación a distancia para gestionar la residencia legal temporaria y la obtención del Documento Nacional de Identidad (DNI) argentino.",
                        'eligibility': "Extranjeros con motivo de radicación (estudios, trabajo, nómada digital, rentista o vínculos familiares) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Pasaporte vigente\n• Certificado de antecedentes penales del país de origen apostillado y traducido\n• Certificado de antecedentes penales argentinos (RNR)\n• Comprobante de domicilio (declaración jurada en policía)\n• Constancia de ingresos o inscripción universitaria [Örnek veri — doğrulanmadı]",
                        'steps': "1. Creación de expediente en la plataforma digital RaDEX.\n2. Pago de la tasa de radicación migratoria.\n3. Subida telemática de todos los requisitos.\n4. Turno presencial en Sede Central de Migraciones para control documental y biometría.\n5. Envío del plástico de DNI al domicilio por Correo Argentino [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Tasa migratoria no Mercosur: approx. 40.000 ARS + DNI [Örnek veri — doğrulanmadı]. Tiempo: 1-3 meses.",
                        'validity': "Residencia temporaria válida por 1 o 2 años según criterio, renovable.",
                        'notes': "La 'Residencia Precaria' descargable del portal RaDEX otorga pleno derecho a trabajar y estudiar legalmente mientras se tramita el DNI.",
                    },
                    'tr': {
                        'title': 'Arjantin Geçici Oturum İzni ve DNI Kimlik Kartı Başvurusu (RaDEX)',
                        'summary': "Arjantin'de üniversite, uzaktan çalışma veya iş sebebiyle yaşamak isteyen yabancıların RaDEX sistemi üzerinden oturum izni ve DNI kimlik kartı alma süreci.",
                        'eligibility': "Yasal giriş yapmış olmak, temiz adli sicil kaydı ve ikamet gerekçesi (eğitim, çalışma, gelir beyanı vb.) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Pasaport fotokopisi\n• Apostilli ve yeminli İspanyolca tercümeli adli sicil kaydı\n• Arjantin sabıka kaydı (RNR)\n• İkametgâh beyanı (Polis onaylı)\n• Gelir veya okul kabul belgesi [Örnek veri — doğrulanmadı]",
                        'steps': "1. RaDEX portalı üzerinden online başvuru oluşturma.\n2. Göç harcını ödeme ve belgeleri yükleme.\n3. 'Residencia Precaria' geçici oturum belgesini indirme.\n4. DNM merkezinde parmak izi randevusuna katılma.\n5. DNI plastik kartının posta yoluyla adrese teslimi [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Göç harcı: ~40.000 ARS [Örnek veri — doğrulanmadı]. Süre: 1-3 ay.",
                        'validity': "1 veya 2 yıl geçerlidir; 2 yıl kesintisiz yasal ikamet sonrası Arjantin vatandaşlığına başvurulabilir.",
                        'notes': "RaDEX'ten indirilen geçici ikamet belgesi (Residencia Precaria) kart çıkana kadar tam yasal çalışma ve eğitim hakkı tanır.",
                    }
                }
            }
        ]
    }
]
