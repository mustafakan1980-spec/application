# -*- coding: utf-8 -*-
from datetime import date

EUROPE_COUNTRIES = [
    # 1. İTALYA (IT)
    {
        'country': {
            'iso2': 'IT',
            'slug': 'it',
            'flag_emoji': '🇮🇹',
            'primary_language': 'it',
            'official_languages': ['it'],
            'translations': {'it': 'Italia', 'tr': 'İtalya', 'en': 'Italy', 'de': 'Italien', 'fr': 'Italie'},
        },
        'institutions': [
            {
                'slug': 'questura-roma-polizia',
                'website': 'https://www.poliziadistato.it',
                'phone': '+39 06 4686 [Örnek veri — doğrulanmadı]',
                'email': 'immigrazione.roma@poliziadistato.it [Örnek veri — doğrulanmadı]',
                'address': 'Via San Vitale 15, 00184 Roma, Italia',
                'translations': {
                    'it': {'name': "Polizia di Stato — Ufficio Immigrazione (Questura)", 'address_text': 'Roma, Italia', 'working_hours': 'Lun-Ven: 08:30 - 13:30'},
                    'tr': {'name': 'İtalya Emniyet Müdürlüğü — Göç İdaresi (Questura)', 'address_text': 'Roma, İtalya', 'working_hours': 'Hafta içi 08:30 - 13:30'},
                }
            },
            {
                'slug': 'motorizzazione-civile-roma',
                'website': 'https://www.ilportaledellautomobilista.it',
                'phone': '+39 06 87401 [Örnek veri — doğrulanmadı]',
                'email': 'motorizzazione@mit.gov.it [Örnek veri — doğrulanmadı]',
                'address': 'Via Salaria 1045, Roma, Italia',
                'translations': {
                    'it': {'name': 'Ministero delle Infrastrutture e dei Trasporti (Motorizzazione Civile)', 'address_text': 'Roma, Italia', 'working_hours': 'Lun-Ven: 08:30 - 12:30'},
                    'tr': {'name': 'İtalya Ulaştırma Bakanlığı Sürücü Belgesi Dairesi (Motorizzazione)', 'address_text': 'Roma, İtalya', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'it-permesso-di-soggiorno-studio',
                'category': 'residence-permit',
                'institution_slug': 'questura-roma-polizia',
                'official_source_url': 'https://www.portaleimmigrazione.it',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'it': {
                        'title': 'Permesso di Soggiorno per motivi di Studio (Kit Giallo)',
                        'summary': "Procedura per la richiesta del permesso di soggiorno elettronico per studenti stranieri giunti in Italia con visto di tipo D.",
                        'eligibility': "Titolari di visto per studio D e iscrizione confermata presso università o istituto accreditato in Italia [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Kit postale (Modulo 1)\n• Copia passaporto e visto\n• Codice Fiscale\n• Iscrizione universitaria\n• Assicurazione sanitaria\n• Marca da bollo 16 EUR [Örnek veri — doğrulanmadı]",
                        'steps': "1. Ritiro gratuito del Kit Giallo presso gli uffici di Poste Italiane.\n2. Compilazione del Modulo 1 e acquisto marca da bollo.\n3. Invio della busta allo sportello postale 'Amico' e rilascio ricevuta con data convocazione.\n4. Appuntamento in Questura per fotosegnalamento e impronte.\n5. Ritiro del permesso elettronico plastificato [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Frais postali: 30 EUR + bollo 16 EUR + contributo rilascio ca. 70-80 EUR [Örnek veri — doğrulanmadı]. Durata: 2-4 mesi.",
                        'validity': "Valido 1 anno, rinnovabile fino al termine del corso di studi.",
                        'notes': "La ricevuta postale (cedolino) con QR code ha valore legale per il soggiorno e per viaggiare nel Paese di origine.",
                    },
                    'tr': {
                        'title': 'İtalya Öğrenci Oturum İzni Başvurusu (Permesso di Soggiorno - Kit Giallo)',
                        'summary': "D tipi öğrenci vizesiyle İtalya'ya gelen yabancı öğrencilerin İtalyan Postanesi (Poste Italiane) ve Emniyet (Questura) üzerinden oturum kartı alma süreci.",
                        'eligibility': "Geçerli D tipi ulusal öğrenci vizesi ve İtalya'daki üniversiteye resmi kayıt [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Postaneden alınan Kit Giallo Form 1\n• Pasaport ve vize fotokopisi\n• Codice Fiscale (Vergi numarası)\n• Üniversite kayıt belgesi\n• Sağlık sigortası ve 16 € damga pulu (marca da bollo) [Örnek veri — doğrulanmadı]",
                        'steps': "1. Postaneden sarı başvuru kitini (Kit Giallo) ücretsiz alma.\n2. Form 1'i doldurup damga pulunu yapıştırma.\n3. Sportello Amico yetkili postanesinden dosyayı gönderme ve randevu fişini alma.\n4. Randevu gününde Questura'da parmak izi verme.\n5. Kart hazır olduğunda SMS bildirimi ile teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Posta ücreti: 30 € + damga pulu: 16 € + kart bedeli: ~70-80 € [Örnek veri — doğrulanmadı]. Süre: 2-4 ay.",
                        'validity': "Genellikle 1 yıllık düzenlenir; eğitim süresince her yıl yenilenir.",
                        'notes': "Postanenin verdiği barkodlu makbuz (cedolino) oturum kartı çıkana kadar yasal kalış hakkı sağlar.",
                    }
                },
                'sample_documents': [
                    {
                        'storage_path': 'samples/it_modulo1_permesso_soggiorno.pdf',
                        'file_type': 'PDF',
                        'translations': {
                            'it': {'title': 'Modulo 1 Kit Giallo per Permesso di Soggiorno [Modello]', 'description': 'Esempio di modulo compilato per la richiesta postale.'},
                            'tr': {'title': 'Kit Giallo Modulo 1 Örnek Başvuru Formu [Örnek Belge — Doğrulanmadı]', 'description': 'İtalya oturum izni başvurusunda postane üzerinden doldurulan örnek form.'}
                        }
                    }
                ]
            },
            {
                'slug': 'it-patente-di-guida-b',
                'category': 'driving-license',
                'institution_slug': 'motorizzazione-civile-roma',
                'official_source_url': 'https://www.ilportaledellautomobilista.it',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'it': {
                        'title': 'Conseguimento della Patente di Guida B',
                        'summary': "Procedura per il conseguimento della patente di guida per autoveicoli (Categoria B) in Italia tramite autoscuola o da privatista.",
                        'eligibility': "Almeno 18 anni compiuti, residenza anagrafica o soggiorno regolare in Italia [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Modello TT 2112\n• Certificato medico con foto\n• Documento di identità e codice fiscale\n• Ricevute pagamenti PagoPA\n• 3 fototessere [Örnek veri — doğrulanmadı]",
                        'steps': "1. Iscrizione presso autoscuola o Motorizzazione.\n2. Esame di teoria a quiz informatizzato.\n3. Rilascio del 'Foglio Rosa' per esercitazioni pratiche.\n4. Guide obbligatorie certificate (almeno 6 ore).\n5. Esame pratico di guida e consegna immediata della patente [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Diritti e bolli di Stato ca. 100 EUR + costi scuola guida [Örnek veri — doğrulanmadı]. Durata: 2-5 mesi.",
                        'validity': "Valida 10 anni fino ai 50 anni di età.",
                        'notes': "Ai neopatentati si applicano limitazioni di potenza per il primo anno e limiti di velocità per 3 anni.",
                    },
                    'tr': {
                        'title': 'İtalya B Sınıfı Sürücü Belgesi (Patente B) Başvurusu',
                        'summary': "İtalya'da otomobil kullanabilmek için B sınıfı ehliyet alma, teorik sınav (quiz) ve direksiyon sınav süreci.",
                        'eligibility': "18 yaşını doldurmuş olmak ve İtalya'da yasal ikametgâha (Residenza) sahip olmak [Örnek veri — doğrulanmadı].",
                        'required_documents': "• TT 2112 başvuru formu\n• Doktor sağlık ve göz raporu\n• Kimlik belgesi ve Codice Fiscale\n• PagoPA harç makbuzları\n• 3 adet vesikalık fotoğraf [Örnek veri — doğrulanmadı]",
                        'steps': "1. Sürücü kursuna kayıt veya bireysel başvuru.\n2. 30 soruluk teorik quiz sınavını geçme.\n3. Pratik sürüş için 'Foglio Rosa' geçici izin belgesi alma.\n4. Zorunlu gece ve otoyol sürüş derslerini tamamlama.\n5. Direksiyon sınavını başarıyla geçerek kartı alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Devlet harçları ~100 € + kurs masrafları [Örnek veri — doğrulanmadı]. Süre: 2-5 ay.",
                        'validity': "50 yaşına kadar 10 yılda bir yenilenir.",
                        'notes': "İlk defa ehliyet alanlar (neopatentati) için ilk 1 yıl araç motor gücü sınırı uygulanır.",
                    }
                }
            }
        ]
    },

    # 2. İSPANYA (ES)
    {
        'country': {
            'iso2': 'ES',
            'slug': 'es',
            'flag_emoji': '🇪🇸',
            'primary_language': 'es',
            'official_languages': ['es'],
            'translations': {'es': 'España', 'tr': 'İspanya', 'en': 'Spain', 'de': 'Spanien', 'fr': 'Espagne'},
        },
        'institutions': [
            {
                'slug': 'extranjeria-policia-spain',
                'website': 'https://sede.administracionespublicas.gob.es',
                'phone': '+34 91 537 10 00 [Örnek veri — doğrulanmadı]',
                'email': 'informacion.extranjeria@correo.gob.es [Örnek veri — doğrulanmadı]',
                'address': 'Calle García de Paredes 65, 28010 Madrid, España',
                'translations': {
                    'es': {'name': 'Oficinas de Extranjería y Cuerpo Nacional de Policía', 'address_text': 'Madrid, España', 'working_hours': 'Lun-Vie: 09:00 - 14:00'},
                    'tr': {'name': 'İspanya Yabancılar Dairesi ve Ulusal Polis Teşkilatı (Extranjería)', 'address_text': 'Madrid, İspanya', 'working_hours': 'Hafta içi 09:00 - 14:00'},
                }
            },
            {
                'slug': 'dgt-trafico-spain',
                'website': 'https://sede.dgt.gob.es',
                'phone': '060 [Örnek veri — doğrulanmadı]',
                'email': 'dgt@dgt.es [Örnek veri — doğrulanmadı]',
                'address': 'Calle Josefa Valcárcel 28, 28027 Madrid, España',
                'translations': {
                    'es': {'name': 'Dirección General de Tráfico (DGT)', 'address_text': 'Madrid, España', 'working_hours': 'Lun-Vie: 08:30 - 14:30'},
                    'tr': {'name': 'İspanya Genel Trafik Müdürlüğü (DGT)', 'address_text': 'Madrid, İspanya', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'es-visado-nomada-digital',
                'category': 'visa',
                'institution_slug': 'extranjeria-policia-spain',
                'official_source_url': 'https://prie.comercio.gob.es/es-es/Paginas/Teletrabajadores-Caracter-Internacional.aspx',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'es': {
                        'title': 'Visado y Autorización de Residencia para Nómadas Digitales (Ley de Startups)',
                        'summary': "Permiso oficial para profesionales extranjeros que teletrabajan a distancia para empresas ubicadas fuera de España.",
                        'eligibility': "Graduados universitarios o con 3 años de experiencia, contrato de trabajo a distancia de al menos 3 meses de antigüedad, ingresos mensuales mínimos del 200% del SMI (aprox. 2.646 EUR/mes) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Formulario oficial EX-10\n• Contrato mercantil o laboral de teletrabajo\n• Acreditación de ingresos y extractos bancarios\n• Certificado de antecedentes penales apostillado\n• Seguro médico privado sin copago en España [Örnek veri — doğrulanmadı]",
                        'steps': "1. Solicitud en consulado (visado de 1 año) o telemática desde España ante la UGE (autorización de 3 años).\n2. Aportación de documentación traducida por traductor jurado.\n3. Resolución favorable en plazo de 20 días hábiles.\n4. Toma de huellas en comisaría de policía (Cita previa TIE).\n5. Recogida de la Tarjeta de Identidad de Extranjero (TIE) [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Tasa 790-038: 73,26 EUR [Örnek veri — doğrulanmadı]. Plazo de resolución legal: 20 días hábiles.",
                        'validity': "Hasta 3 años cuando se solicita desde España, renovable por 2 años más.",
                        'notes': "Permite acogerse al régimen fiscal especial de impatriados (Ley Beckham) con un tipo fijo de IRPF del 24%.",
                    },
                    'tr': {
                        'title': 'İspanya Dijital Göçebe Vizesi ve Oturum İzni (Digital Nomad Visa)',
                        'summary': "İspanya dışındaki şirketler için uzaktan çalışan yazılımcı ve profesyonellerin Startup Yasası kapsamında 3 yıla kadar oturum izni alma süreci.",
                        'eligibility': "Üniversite diploması veya 3 yıl kıdem, en az 3 aydır süren uzaktan çalışma sözleşmesi ve aylık asgari brüt 2.646 € gelir kanıtı [Örnek veri — doğrulanmadı].",
                        'required_documents': "• EX-10 başvuru formu\n• Uzaktan çalışma iş sözleşmesi ve şirket izin yazısı\n• Son 3 aylık banka hesap dökümleri\n• Apostilli adli sicil kaydı (yeminli İspanyolca tercümeli)\n• İspanya tam kapsamlı özel sağlık sigortası [Örnek veri — doğrulanmadı]",
                        'steps': "1. İspanya içinden dijital sertifikayla UGE portalına online başvuru (veya konsolosluktan vize alma).\n2. 20 iş günü içinde onay alınması.\n3. Polisten parmak izi (TIE) randevusu alma.\n4. Parmak izi verme ve TIE plastik kartını teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Resmi başvuru harcı: 73,26 € [Örnek veri — doğrulanmadı]. Hızlı sonuçlanma: 20 iş günü.",
                        'validity': "İspanya içinden başvurularda 3 yıllık düzenlenir; 2 yıl daha uzatılabilir.",
                        'notes': "Beckham Yasası vergi avantajından faydalanarak 6 yıla kadar %24 sabit gelir vergisi ödenebilir.",
                    }
                },
                'sample_documents': [
                    {
                        'storage_path': 'samples/es_formulario_ex10_nomada.pdf',
                        'file_type': 'PDF',
                        'translations': {
                            'es': {'title': 'Formulario EX-10 Autorización de Residencia [Modelo]', 'description': 'Modelo oficial para la tramitación de residencia para teletrabajadores.'},
                            'tr': {'title': 'İspanya EX-10 Oturum İzni Başvuru Formu [Örnek Belge — Doğrulanmadı]', 'description': 'Dijital göçebe ve yabancı ikamet başvurularında kullanılan resmi form örneği.'}
                        }
                    }
                ]
            },
            {
                'slug': 'es-nie-numero-identidad-extranjero',
                'category': 'passport',
                'institution_slug': 'extranjeria-policia-spain',
                'official_source_url': 'https://www.policia.es/_es/tramites_extranjeria.php',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'es': {
                        'title': 'Asignación de Número de Identidad de Extranjero (NIE)',
                        'summary': "Número personal, único y exclusivo que deben poseer los extranjeros en España a efectos de identificación fiscal, económica y administrativa.",
                        'eligibility': "Extranjeros con intereses económicos, profesionales o sociales en España [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Formulario oficial EX-15\n• Pasaporte original y copia de la página de datos\n• Justificante del motivo que fundamenta la solicitud (compra de vivienda, contrato de trabajo, constitución de empresa)\n• Tasa 790 código 012 pagada [Örnek veri — doğrulanmadı]",
                        'steps': "1. Reserva de cita previa en sede electrónica ('Policía - Asignación de NIE').\n2. Pago de la tasa 790-012 en el banco.\n3. Comparecencia en la comisaría o consulado con los documentos.\n4. Entrega del certificado de asignación de NIE en papel blanco [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Tasa: 9,84 EUR [Örnek veri — doğrulanmadı]. Emisión: 1-5 días hábiles.",
                        'validity': "El número NIE es vitalicio y permanente.",
                        'notes': "El NIE no equivale a un permiso de residencia; es un identificador tributario y administrativo.",
                    },
                    'tr': {
                        'title': 'İspanya Yabancı Kimlik ve Vergi Numarası (NIE) Başvurusu',
                        'summary': "İspanya'da banka hesabı açmak, ev kiralamak, araç satın almak veya çalışmak için zorunlu olan resmi yabancı kimlik numarası (NIE).",
                        'eligibility': "İspanya'da ekonomik, mesleki veya eğitim amaçlı işlem yapacak tüm yabancılar [Örnek veri — doğrulanmadı].",
                        'required_documents': "• EX-15 başvuru formu\n• Pasaport fotokopisi\n• NIE talep gerekçesi (ev kiralama sözleşmesi, iş teklifi, üniversite kabulü)\n• Modelo 790-012 vergi ödendi makbuzu [Örnek veri — doğrulanmadı]",
                        'steps': "1. sede.administracionespublicas.gob.es üzerinden 'Asignación de NIE' randevusu alma.\n2. Bankadan 9,84 € harç yatırma.\n3. Randevu gününde polis merkezine evrakları sunma.\n4. Beyaz NIE sertifikasını teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Harç: 9,84 € [Örnek veri — doğrulanmadı]. Teslim: 1-5 iş günü.",
                        'validity': "Atanan NIE numarası ömür boyu geçerlidir.",
                        'notes': "Beyaz kâğıt NIE tek başına oturum izni hakkı vermez, kimlik ve vergi takip numarasıdır.",
                    }
                }
            }
        ]
    },

    # 3. HOLLANDA (NL)
    {
        'country': {
            'iso2': 'NL',
            'slug': 'nl',
            'flag_emoji': '🇳🇱',
            'primary_language': 'nl',
            'official_languages': ['nl', 'en'],
            'translations': {'nl': 'Nederland', 'tr': 'Hollanda', 'en': 'Netherlands', 'de': 'Niederlande', 'fr': 'Pays-Bas'},
        },
        'institutions': [
            {
                'slug': 'ind-immigratie-nederland',
                'website': 'https://ind.nl',
                'phone': '+31 88 043 0430 [Örnek veri — doğrulanmadı]',
                'email': 'informatie@ind.nl [Örnek veri — doğrulanmadı]',
                'address': 'Rijnstraat 8, 2515 XP Den Haag, Nederland',
                'translations': {
                    'nl': {'name': 'Immigratie- en Naturalisatiedienst (IND)', 'address_text': 'Den Haag, Nederland', 'working_hours': 'Ma-Vr: 09:00 - 17:00'},
                    'tr': {'name': 'Hollanda Göç ve Vatandaşlık Dairesi (IND)', 'address_text': 'Lahey, Hollanda', 'working_hours': 'Hafta içi 09:00 - 17:00'},
                    'en': {'name': 'Immigration and Naturalisation Service (IND)', 'address_text': 'The Hague, Netherlands', 'working_hours': 'Mon-Fri: 09:00 - 17:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'nl-kennismigrant-highly-skilled',
                'category': 'work-permit',
                'institution_slug': 'ind-immigratie-nederland',
                'official_source_url': 'https://ind.nl/en/residence-permits/work/highly-skilled-migrant',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Highly Skilled Migrant Residence Permit (Kennismigrant)',
                        'summary': 'Residence permit for qualified foreign specialists employed by a recognized sponsor employer in the Netherlands.',
                        'eligibility': 'Employment contract with IND-recognized sponsor and meeting the statutory gross monthly salary threshold (under 30: €3,992, 30 and older: €5,446) [Sample data — unverified].',
                        'required_documents': '• Valid passport copy\n• Signed employment contract\n• Recognized sponsor application declaration\n• Antecedents certificate [Sample data — unverified]',
                        'steps': '1. Employer submits TEV application online directly to IND.\n2. IND issues approval decision within 2 to 4 weeks.\n3. Employee collects MVV entry visa at Dutch embassy (if required).\n4. Travel to Netherlands, register at Municipality (Gemeente) for BSN, and collect biometric residence card at IND desk [Sample data — unverified].',
                        'fees_and_duration': 'IND application fee: €380 [Sample data — unverified]. Fast processing: 2-4 weeks.',
                        'validity': 'Issued for the duration of the employment contract up to 5 years.',
                        'notes': 'Eligible employees may qualify for the lucrative 30% tax ruling facility.',
                    },
                    'tr': {
                        'title': 'Hollanda Nitelikli Göçmen Çalışma ve Oturum İzni (Kennismigrant)',
                        'summary': "Hollanda'daki yetkili (IND onaylı) bir işverenden iş teklifi alan uzmanların hızlı oturum ve çalışma izni süreci.",
                        'eligibility': "IND tarafından tanınan bir işverenle sözleşme ve yasal asgari brüt maaş kriteri (30 yaş altı: ~3.992 €, 30 yaş ve üstü: ~5.446 €) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Geçerli pasaport\n• İş sözleşmesi\n• İşverenin IND sponsorluk başvuru formu\n• Sabıka kaydı beyanı (Antecedents certificate) [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin IND portalı üzerinden başvuruyu doğrudan yapması.\n2. 2-4 hafta içinde onay kararı gelmesi.\n3. Konsolosluktan MVV vizesi alma.\n4. Hollanda'ya giderek belediyeden (Gemeente) BSN numarası çıkarma ve IND ofisinden kartı teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "IND başvuru harcı: 380 € [Örnek veri — doğrulanmadı]. Süre: 2-4 hafta.",
                        'validity': "İş sözleşmesi süresince (en fazla 5 yıl) verilir.",
                        'notes': "Koşulları sağlayan çalışanlar %30 vergi indirimi (30% ruling) avantajından yararlanabilir.",
                    }
                }
            }
        ]
    },

    # 4. İSVİÇRE (CH)
    {
        'country': {
            'iso2': 'CH',
            'slug': 'ch',
            'flag_emoji': '🇨🇭',
            'primary_language': 'de',
            'official_languages': ['de', 'fr', 'it', 'en'],
            'translations': {'de': 'Schweiz', 'tr': 'İsviçre', 'en': 'Switzerland', 'fr': 'Suisse', 'it': 'Svizzera'},
        },
        'institutions': [
            {
                'slug': 'sem-migrationsamt-schweiz',
                'website': 'https://www.sem.admin.ch',
                'phone': '+41 58 465 11 11 [Örnek veri — doğrulanmadı]',
                'email': 'info@sem.admin.ch [Örnek veri — doğrulanmadı]',
                'address': 'Quellenweg 6, 3003 Bern-Wabern, Schweiz',
                'translations': {
                    'de': {'name': 'Staatssekretariat für Migration (SEM)', 'address_text': 'Bern, Schweiz', 'working_hours': 'Mo-Fr: 08:30 - 16:30'},
                    'tr': {'name': 'İsviçre Federal Göç Müsteşarlığı (SEM)', 'address_text': 'Bern, İsviçre', 'working_hours': 'Hafta içi mesai saatleri'},
                    'en': {'name': 'State Secretariat for Migration (SEM)', 'address_text': 'Bern, Switzerland', 'working_hours': 'Mon-Fri: 08:30 - 16:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'ch-aufenthaltsbewilligung-b',
                'category': 'residence-permit',
                'institution_slug': 'sem-migrationsamt-schweiz',
                'official_source_url': 'https://www.sem.admin.ch/sem/de/home/themen/arbeit/nicht-eu_efta-angehoerige.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'de': {
                        'title': 'Aufenthaltsbewilligung B (Jahresaufenthalter) für Erwerbstätige',
                        'summary': "Kantonale und eidgenössische Bewilligung für Drittstaatsangehörige mit einem qualifizierten Arbeitsvertrag in der Schweiz.",
                        'eligibility': "Besondere berufliche Qualifikation (Führungskräfte, Spezialisten), Vorrang von Schweizer und EU-Arbeitskräften geprüft (Inländervorrang), Einhaltung von Kontingenten [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Arbeitsvertrag mit orts- und branchenüblichem Lohn\n• Lebenslauf und Diplome\n• Begründungsschreiben des Arbeitgebers zur Unentbehrlichkeit\n• Gültiger Reisepass [Örnek veri — doğrulanmadı]",
                        'steps': "1. Arbeitgeber reicht Gesuch beim kantonalen Migrations- und Arbeitsamt ein.\n2. Prüfung durch den Kanton und Weiterleitung an das SEM.\n3. Zustimmung des Bundes (SEM).\n4. Ermächtigung zur Visumserteilung für die Schweizer Botschaft.\n5. Einreise und Anmeldung bei der Einwohnerkontrolle [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Kantons- und Bundesgebühren ca. 150-300 CHF [Örnek veri — doğrulanmadı]. Bearbeitungszeit: 8-16 Wochen.",
                        'validity': "In der Regel für 1 Jahr erteilt, jährlich verlängerbar.",
                        'notes': "Für Angehörige von Drittstaaten gelten strenge jährliche Bundeskontingente.",
                    },
                    'tr': {
                        'title': 'İsviçre B Tipi Oturum ve Çalışma İzni (Aufenthaltsbewilligung B)',
                        'summary': "İsviçre'de nitelikli bir iş teklifi alan AB dışı profesyonellerin kanton ve federal makamlarca onaylanan yıllık oturum izni.",
                        'eligibility': "Yüksek nitelikli uzmanlık, yerli ve AB iş gücü önceliği kuralının karşılanması ve federal kanton kotaları [Örnek veri — doğrulanmadı].",
                        'required_documents': "• İsviçre iş sözleşmesi\n• Üniversite diploması ve detaylı CV\n• Şirketin yerli iş gücü arama gerekçe dosyası\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin kanton göç idaresine başvuru yapması.\n2. Kanton onayı ve federal SEM incelemesi.\n3. Onay sonrası İsviçre Konsolosluğundan D vizesi alma.\n4. İsviçre'ye varışta ikamet kaydı (Einwohnerkontrolle) yaptırma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Kanton ve federal harçlar: ~150-300 CHF [Örnek veri — doğrulanmadı]. Süre: 8-16 hafta.",
                        'validity': "1 yıllık düzenlenir; her yıl yenilenebilir.",
                        'notes': "Üçüncü ülke vatandaşları için yıllık sınırlı kontenjan kotaları uygulanır.",
                    }
                }
            }
        ]
    },

    # 5. İRLANDA (IE)
    {
        'country': {
            'iso2': 'IE',
            'slug': 'ie',
            'flag_emoji': '🇮🇪',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'en': 'Ireland', 'tr': 'İrlanda', 'fr': 'Irlande', 'de': 'Irland'},
        },
        'institutions': [
            {
                'slug': 'irish-immigration-delivery-inis',
                'website': 'https://www.irishimmigration.ie',
                'phone': '+353 1 616 7700 [Sample data — unverified]',
                'email': 'immigrationsupport@justice.ie [Sample data — unverified]',
                'address': '13-14 Burgh Quay, Dublin 2, Ireland',
                'translations': {
                    'en': {'name': 'Immigration Service Delivery (ISD) & DETE', 'address_text': 'Dublin, Ireland', 'working_hours': 'Mon-Fri 09:00 - 17:00'},
                    'tr': {'name': 'İrlanda Adalet Bakanlığı Göç İdaresi (ISD)', 'address_text': 'Dublin, İrlanda', 'working_hours': 'Hafta içi 09:00 - 17:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'ie-critical-skills-employment-permit',
                'category': 'work-permit',
                'institution_slug': 'irish-immigration-delivery-inis',
                'official_source_url': 'https://enterprise.gov.ie/en/what-we-do/workplace-and-skills/employment-permits/permit-types/critical-skills-employment-permit/',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Critical Skills Employment Permit (CSEP)',
                        'summary': 'Employment permit designed to attract highly skilled professionals (ICT, engineering, healthcare) into the Irish labour market.',
                        'eligibility': 'Eligible occupation on the Critical Skills list with minimum remuneration of €38,000/year (or €64,000/year for non-listed professions) [Sample data — unverified].',
                        'required_documents': '• Job offer on company letterhead\n• Employer registration details\n• Relevant degree qualifications\n• Passport identification pages [Sample data — unverified]',
                        'steps': '1. Apply online via EPOS (Employment Permits Online System).\n2. DETE processing and decision issuance.\n3. Apply for entry visa (if required).\n4. Register in Ireland at ISD Burgh Quay for Irish Residence Permit (IRP Stamp 1) [Sample data — unverified].',
                        'fees_and_duration': 'Permit fee: €1,000 (€900 refunded if refused) [Sample data — unverified]. Processing time: 4-8 weeks.',
                        'validity': 'Issued for 2 years; eligible for Stamp 4 permanent residence pathway thereafter.',
                        'notes': 'Fast-track to family reunification without mandatory waiting periods.',
                    },
                    'tr': {
                        'title': 'İrlanda Kritik Beceriler Çalışma İzni (Critical Skills Employment Permit)',
                        'summary': "İrlanda'da teknoloji, mühendislik veya sağlık alanlarında onaylı iş teklifi alan uzmanların 2 yıllık çalışma ve oturum izni süreci.",
                        'eligibility': "Kritik Beceriler Meslek Listesinde yer alan bir pozisyonda yıllık asgari 38.000 € maaş teklifi [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Resmi iş sözleşmesi ve teklif mektubu\n• Lisans/yüksek lisans diploması\n• Pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. EPOS portalından DETE çalışma izni başvurusu yapılması.\n2. Onay belgesi ile D tipi çalışma vizesi alma.\n3. İrlanda'ya varışta IRP (Stamp 1) oturum kartı randevusuna gitme [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "İzin harcı: 1.000 € + IRP kartı: 300 € [Örnek veri — doğrulanmadı]. Süre: 4-8 hafta.",
                        'validity': "2 yıllık verilir; 2 yıl sonunda Stamp 4 süresiz çalışma hakkına dönüşür.",
                        'notes': "Eş ve çocukların İrlanda'ya hemen gelerek tam zamanlı çalışma hakkı bulunur.",
                    }
                }
            }
        ]
    },

    # 6. PORTEKİZ (PT)
    {
        'country': {
            'iso2': 'PT',
            'slug': 'pt',
            'flag_emoji': '🇵🇹',
            'primary_language': 'pt',
            'official_languages': ['pt'],
            'translations': {'pt': 'Portugal', 'tr': 'Portekiz', 'en': 'Portugal', 'fr': 'Portugal', 'de': 'Portugal'},
        },
        'institutions': [
            {
                'slug': 'aima-portugal',
                'website': 'https://aima.gov.pt',
                'phone': '+351 217 115 000 [Örnek veri — doğrulanmadı]',
                'email': 'geral@aima.gov.pt [Örnek veri — doğrulanmadı]',
                'address': 'Avenida António Augusto de Aguiar 20, 1069-119 Lisboa, Portugal',
                'translations': {
                    'pt': {'name': 'Agência para a Integração, Migrações e Asilo (AIMA)', 'address_text': 'Lisboa, Portugal', 'working_hours': 'Seg-Sex: 08:30 - 16:30'},
                    'tr': {'name': 'Portekiz Göç ve İltica İdaresi (AIMA)', 'address_text': 'Lizbon, Portekiz', 'working_hours': 'Hafta içi mesai saatleri'},
                    'en': {'name': 'Agency for Integration, Migration and Asylum (AIMA)', 'address_text': 'Lisbon, Portugal', 'working_hours': 'Mon-Fri: 08:30 - 16:30'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'pt-visto-d8-nomada-digital',
                'category': 'visa',
                'institution_slug': 'aima-portugal',
                'official_source_url': 'https://vistos.mne.gov.pt/pt/vistos-nacionais/documentacao-instrutoria/residencia/trabalho-remoto-nomadas-digitais',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'pt': {
                        'title': 'Visto D8 para Nómadas Digitais (Trabalho Remoto)',
                        'summary': "Visto de residência para cidadãos de países terceiros que exerçam atividade profissional subordinada ou independente prestada remotamente a entidades fora de Portugal.",
                        'eligibility': "Comprovação de rendimentos médios mensais equivalentes a pelo menos quatro salários mínimos nacionais (aprox. 3.280 EUR/mês) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Contrato de trabalho ou prestação de serviços\n• Comprovativos de rendimentos e extratos bancários dos últimos 3 meses\n• Atestado de residência fiscal\n• Seguro de viagem ou seguro de saúde\n• Certificado de registo criminal apostilado [Örnek veri — doğrulanmadı]",
                        'steps': "1. Submissão do pedido no consulado de Portugal através do portal E-Vistos.\n2. Entrevista e recolha biométrica no consulado.\n3. Emissão do visto com validade de 120 dias e marcação prévia na AIMA.\n4. Comparência na AIMA em Portugal para emissão do cartão de residência [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Taxa de visto consular: 90 EUR + taxa de emissão de título AIMA: ca. 170 EUR [Örnek veri — doğrulanmadı]. Prazo: 30-60 dias.",
                        'validity': "Título de residência inicial válido por 2 anos, renovável por períodos sucessivos de 3 anos.",
                        'notes': "Permite requerer a nacionalidade portuguesa após 5 anos de residência legal.",
                    },
                    'tr': {
                        'title': 'Portekiz D8 Dijital Göçebe Vizesi (Visto D8 Nómada Digital)',
                        'summary': "Portekiz dışında yerleşik şirketlere uzaktan çalışan profesyonellerin D8 vizesi ve 2 yıllık ikamet izni alma süreci.",
                        'eligibility': "Portekiz asgari ücretinin en az 4 katı tutarında (aylık ~3.280 €) düzenli uzaktan çalışma geliri [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Uzaktan çalışma sözleşmesi\n• Son 3 aylık banka hesap dökümleri\n• Portekiz vergi numarası (NIF) ve banka hesabı\n• Apostilli adli sicil kaydı\n• Seyahat sağlık sigortası [Örnek veri — doğrulanmadı]",
                        'steps': "1. E-Vistos portalından konsolosluk başvurusunun yapılması.\n2. 120 günlük giriş vizesiyle Portekiz'e seyahat.\n3. Vizeye ekli AIMA randevusunda parmak izi verilmesi.\n4. 2 yıllık plastik oturum kartının adrese teslimi [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Konsolosluk harcı: 90 € + AIMA kart harcı: ~170 € [Örnek veri — doğrulanmadı]. Süre: 30-60 gün.",
                        'validity': "İlk kart 2 yıllık verilir; 3 yıl daha uzatılabilir. 5 yıl sonunda vatandaşlık başvurusu yapılabilir.",
                        'notes': "Portekiz'de NIF numarası almak başvuru sürecinin ilk ön koşuludur.",
                    }
                }
            }
        ]
    },

    # 7. YUNANİSTAN (GR)
    {
        'country': {
            'iso2': 'GR',
            'slug': 'gr',
            'flag_emoji': '🇬🇷',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'tr': 'Yunanistan', 'en': 'Greece', 'fr': 'Grèce', 'de': 'Griechenland'},
        },
        'institutions': [
            {
                'slug': 'ministry-migration-greece',
                'website': 'https://migration.gov.gr',
                'phone': '+30 213 212 8400 [Örnek veri — doğrulanmadı]',
                'email': 'info@migration.gov.gr [Örnek veri — doğrulanmadı]',
                'address': 'Thivon 196-198, Agios Ioannis Rentis 182 33, Athina, Greece',
                'translations': {
                    'en': {'name': 'Ministry of Migration and Asylum', 'address_text': 'Athens, Greece', 'working_hours': 'Mon-Fri 08:30 - 15:30'},
                    'tr': {'name': 'Yunanistan Göç ve İltica Bakanlığı', 'address_text': 'Atina, Yunanistan', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'gr-golden-visa-residence-permit',
                'category': 'residence-permit',
                'institution_slug': 'ministry-migration-greece',
                'official_source_url': 'https://migration.gov.gr/en/service/golden-visa/',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Golden Visa Permanent Residence Permit for Investors',
                        'summary': 'Five-year renewable permanent residence permit granted to third-country nationals investing in real estate in Greece.',
                        'eligibility': 'Purchase of real estate property in Greece meeting the tiered threshold (€800,000 in prime regions like Attica/Thessaloniki/Mykonos/Santorini; €400,000 in other regions; or €250,000 for listed architectural buildings) [Sample data — unverified].',
                        'required_documents': '• Notarized property purchase contract and land registry certificate\n• Clean criminal record from home country\n• Full private health insurance\n• Valid passport copy [Sample data — unverified]',
                        'steps': '1. Obtain Greek tax number (AFM) and open bank account.\n2. Complete real estate purchase.\n3. Lawyer submits online application on Ministry of Migration portal.\n4. Attend biometric appointment in Greece.\n5. Receive 5-year permanent residence card [Sample data — unverified].',
                        'fees_and_duration': 'State fee: €2,000 for main applicant + €16 card fee [Sample data — unverified]. Processing: 2-4 months.',
                        'validity': 'Valid for 5 years and renewable indefinitely as long as property ownership is maintained.',
                        'notes': 'No minimum stay requirement in Greece; includes spouse, children up to 21, and parents of both spouses.',
                    },
                    'tr': {
                        'title': 'Yunanistan Altın Vize (Golden Visa) Yatırımcı Oturum İzni',
                        'summary': "Yunanistan'da gayrimenkul yatırımı yapan yabancı yatırımcılara ve ailelerine 5 yıllık süresiz yenilenebilir Schengen oturum izni sağlayan program.",
                        'eligibility': "Yasal kademeli eşiklere göre gayrimenkul alımı (Atina, Selanik ve popüler adalarda 800.000 €; diğer bölgelerde 400.000 €; tarihi bina restorasyonlarında 250.000 €) [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Noter onaylı gayrimenkul alım satım sözleşmesi ve tapu tescil belgesi\n• AFM vergi numarası\n• Apostilli adli sicil kaydı\n• Özel sağlık sigortası ve pasaport fotokopisi [Örnek veri — doğrulanmadı]",
                        'steps': "1. AFM vergi numarası çıkarıp gayrimenkul satın alımını tamamlama.\n2. Göç Bakanlığı portalından online başvuru yapılması.\n3. Yunanistan'da parmak izi verme.\n4. 5 yıllık oturum kartını teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Devlet harcı: 2.000 € + kart bedeli: 16 € [Örnek veri — doğrulanmadı]. Süre: 2-4 ay.",
                        'validity': "5 yıl geçerlidir; gayrimenkul mülkiyeti sürdükçe her 5 yılda bir süresiz yenilenir.",
                        'notes': "Yunanistan'da fiziki olarak yaşama veya ikamet etme zorunluluğu yoktur; tüm Schengen ülkelerinde serbest dolaşım sağlar.",
                    }
                }
            }
        ]
    },

    # 8. AVUSTURYA (AT)
    {
        'country': {
            'iso2': 'AT',
            'slug': 'at',
            'flag_emoji': '🇦🇹',
            'primary_language': 'de',
            'official_languages': ['de'],
            'translations': {'de': 'Österreich', 'tr': 'Avusturya', 'en': 'Austria', 'fr': 'Autriche'},
        },
        'institutions': [
            {
                'slug': 'bmi-bundesministerium-inneres',
                'website': 'https://www.migration.gv.at',
                'phone': '+43 1 53126 [Örnek veri — doğrulanmadı]',
                'email': 'post@bmi.gv.at [Örnek veri — doğrulanmadı]',
                'address': 'Herrengasse 7, 1010 Wien, Österreich',
                'translations': {
                    'de': {'name': 'Bundesministerium für Inneres (BMI) & AMS', 'address_text': 'Wien, Österreich', 'working_hours': 'Mo-Fr: 08:00 - 15:00'},
                    'tr': {'name': 'Avusturya İçişleri Bakanlığı ve İş Kurumu (AMS)', 'address_text': 'Viyana, Avusturya', 'working_hours': 'Hafta içi mesai saatleri'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'at-rot-weiss-rot-karte',
                'category': 'work-permit',
                'institution_slug': 'bmi-bundesministerium-inneres',
                'official_source_url': 'https://www.migration.gv.at/de/formen-der-zuwanderung/dauerhafte-zuwanderung/fachkraefte-in-mangelberufen/',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'de': {
                        'title': 'Rot-Weiß-Rot-Karte für Fachkräfte in Mangelberufen',
                        'summary': "Kriteriengeleitetes Zuwanderungssystem (Punktesystem) zur Niederlassung und Beschäftigung bei einem bestimmten Arbeitgeber in Österreich.",
                        'eligibility': "Erreichen der Mindestpunkte (mind. 55 von 90 Punkten bei Fachkräften in Mangelberufen bzw. 70 Punkte bei sonstigen Schlüsselkräften) und verbindliches Arbeitsplatzangebot [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Arbeitgebererklärung\n• Ausbildungsnachweise und Arbeitszeugnisse\n• Sprachdiplome (Deutsch A1-B2 oder Englisch B1-B2)\n• Nachweis über ortsübliche Unterkunft\n• Geburtsurkunde und Strafregisterauszug [Örnek veri — doğrulanmadı]",
                        'steps': "1. Einreichung des Antrags bei der österreichischen Vertretungsbehörde im Ausland oder direkt in Österreich bei der Aufenthaltsbehörde.\n2. Prüfung der Arbeitsmarktbedingungen durch das Arbeitsmarktservice (AMS).\n3. Ausstellung der Karte durch die Niederlassungsbehörde (z.B. MA 35 in Wien) [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Verwaltungsabgabe: 160 EUR [Örnek veri — doğrulanmadı]. Dauer: ca. 6-10 Wochen.",
                        'validity': "Gültig für 24 Monate; danach Umstieg auf die Rot-Weiß-Rot-Karte Plus (freier Arbeitsmarktzugang) möglich.",
                        'notes': "Ehepartner erhalten sofort eine Rot-Weiß-Rot-Karte Plus mit unbeschränktem Zugang zum österreichischen Arbeitsmarkt.",
                    },
                    'tr': {
                        'title': 'Avusturya Kırmızı-Beyaz-Kırmızı Kart (Rot-Weiß-Rot-Karte) Çalışma İzni',
                        'summary': "Avusturya'da nitelikli mesleklerde iş teklifi alan uzmanların puan tabanlı sistemle 2 yıllık oturum ve çalışma izni alma süreci.",
                        'eligibility': "Puanlama sisteminden en az 55-70 puan alma (yaş, meslek eğitimi, iş deneyimi, Almanca/İngilizce dil puanı) ve iş sözleşmesi [Örnek veri — doğrulanmadı].",
                        'required_documents': "• Arbeitgebererklärung işveren beyan formu\n• Diploma ve transkript\n• Dil sertifikası (ÖSD/Goethe Almanca veya IELTS İngilizce)\n• Avusturya'da konaklama kanıtı ve adli sicil kaydı [Örnek veri — doğrulanmadı]",
                        'steps': "1. Konsolosluğa veya Avusturya'da ikamet dairesine (MA 35) başvuru sunulması.\n2. Avusturya İş Kurumu (AMS) puan ve işgücü onayı.\n3. Kırmızı-Beyaz-Kırmızı kartın teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Harç: 160 € [Örnek veri — doğrulanmadı]. İşlem süresi: 6-10 hafta.",
                        'validity': "24 ay geçerlidir; 2 yıl sonunda serbest çalışma hakkı veren Rot-Weiß-Rot-Karte Plus'a dönüştürülür.",
                        'notes': "Başvuru sahibinin eşi ilk günden itibaren sınırsız çalışma iznine sahip olur.",
                    }
                }
            }
        ]
    },

    # 9. İSVEÇ (SE)
    {
        'country': {
            'iso2': 'SE',
            'slug': 'se',
            'flag_emoji': '🇸🇪',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'tr': 'İsveç', 'en': 'Sweden', 'fr': 'Suède', 'de': 'Schweden'},
        },
        'institutions': [
            {
                'slug': 'migrationsverket-sweden',
                'website': 'https://www.migrationsverket.se',
                'phone': '+46 77 123 52 35 [Sample data — unverified]',
                'email': 'kontakt@migrationsverket.se [Sample data — unverified]',
                'address': 'Slottsholmsgatan 10, 601 70 Norrköping, Sweden',
                'translations': {
                    'en': {'name': 'Swedish Migration Agency (Migrationsverket)', 'address_text': 'Norrköping, Sweden', 'working_hours': 'Mon-Fri 09:00 - 15:00'},
                    'tr': {'name': 'İsveç Göçmenler Genel Müdürlüğü (Migrationsverket)', 'address_text': 'Norrköping, İsveç', 'working_hours': 'Hafta içi 09:00 - 15:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'se-work-permit-migrationsverket',
                'category': 'work-permit',
                'institution_slug': 'migrationsverket-sweden',
                'official_source_url': 'https://www.migrationsverket.se/English/Private-individuals/Working-in-Sweden.html',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Swedish Work Permit (Arbetstillstånd)',
                        'summary': 'Application process for non-EU professionals who have been offered employment in Sweden.',
                        'eligibility': 'Valid job offer with monthly salary of at least 80% of Swedish median salary (currently approx. 28,480 SEK/month), job advertised on EURES/Arbetsförmedlingen for 10 days, terms aligned with Swedish collective agreements [Sample data — unverified].',
                        'required_documents': '• Employment offer initiated by employer in web portal\n• Relevant trade union opinion statement (Fackligt yttrande)\n• Valid passport pages\n• Proof of comprehensive insurance package [Sample data — unverified]',
                        'steps': '1. Employer initiates offer on Migrationsverket e-service.\n2. Relevant Swedish trade union reviews employment terms.\n3. Employee completes application online and pays fee.\n4. Biometrics recorded at embassy or service centre.\n5. Receive decision and work permit card [Sample data — unverified].',
                        'fees_and_duration': 'Application fee: 2,200 SEK [Sample data — unverified]. Processing time: 1-3 months.',
                        'validity': 'Valid for the period of the employment contract, up to 2 years (renewable).',
                        'notes': 'Permanent residence (PUT) can be applied for after 4 years of working in Sweden.',
                    },
                    'tr': {
                        'title': 'İsveç Çalışma ve Oturum İzni (Arbetstillstånd)',
                        'summary': "İsveç'te bir işverenden istihdam teklifi alan yabancı çalışanların Migrationsverket üzerinden çalışma izni süreci.",
                        'eligibility': "İsveç medyan maaşının en az %80'i (aylık ~28.480 SEK) maaş teklifi, ilanın 10 gün açık kalmış olması ve sendika şartlarına uygunluk [Örnek veri — doğrulanmadı].",
                        'required_documents': "• İşverenin online portalda başlattığı iş teklifi\n• İlgili İsveç sendikası onay yazısı (Fackligt yttrande)\n• Pasaport fotokopisi\n• Sigorta teminat belgesi [Örnek veri — doğrulanmadı]",
                        'steps': "1. İşverenin dijital ortamda başvuruyu başlatması.\n2. Sendika incelemesi ve onayı.\n3. Çalışanın online formu tamamlayıp harcı ödemesi.\n4. Konsoloslukta parmak izi verme.\n5. Çalışma kartını teslim alma [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Harç: 2.200 SEK [Örnek veri — doğrulanmadı]. Süre: 1-3 ay.",
                        'validity': "2 yıla kadar verilir; 4 yıl tamamlandıktan sonra süresiz oturum (PUT) hakkı doğar.",
                        'notes': "Sendika görüşünün olumlu olması onay için kritik önem taşır.",
                    }
                }
            }
        ]
    },

    # 10. POLONYA (PL)
    {
        'country': {
            'iso2': 'PL',
            'slug': 'pl',
            'flag_emoji': '🇵🇱',
            'primary_language': 'en',
            'official_languages': ['en'],
            'translations': {'tr': 'Polonya', 'en': 'Poland', 'de': 'Polen', 'fr': 'Pologne'},
        },
        'institutions': [
            {
                'slug': 'mazowiecki-urzad-wojewodzki',
                'website': 'https://migrant.wsc.mazowieckie.pl',
                'phone': '+48 22 695 67 73 [Sample data — unverified]',
                'email': 'legalizacjapobytu@mazowieckie.pl [Sample data — unverified]',
                'address': 'ul. Marszałkowska 3/5, 00-624 Warszawa, Polska',
                'translations': {
                    'en': {'name': 'Voivodeship Department of Foreigners (Urząd Wojewódzki)', 'address_text': 'Warsaw, Poland', 'working_hours': 'Mon-Fri 08:00 - 16:00'},
                    'tr': {'name': 'Polonya Mazovya Valiliği Yabancılar Dairesi (Wojewoda)', 'address_text': 'Varşova, Polonya', 'working_hours': 'Hafta içi 08:00 - 16:00'},
                }
            }
        ],
        'procedures': [
            {
                'slug': 'pl-karta-pobytu-czasowego',
                'category': 'residence-permit',
                'institution_slug': 'mazowiecki-urzad-wojewodzki',
                'official_source_url': 'https://migrant.wsc.mazowieckie.pl/en/procedury/temporary-residence-and-work-permit',
                'last_verified_at': date(2026, 11, 14),
                'translations': {
                    'en': {
                        'title': 'Temporary Residence and Work Permit (Karta Pobytu)',
                        'summary': 'Single combined permit allowing foreign nationals to legally reside and work in Poland for up to 3 years.',
                        'eligibility': 'Legal stay in Poland, employment contract with monthly salary not less than minimum wage (currently 4,300 PLN gross), health insurance, and secured accommodation [Sample data — unverified].',
                        'required_documents': '• 2 copies of Annex 1 (Załącznik nr 1) completed by employer\n• 4 passport photographs\n• Original passport and copies\n• Proof of health insurance and rental agreement\n• Tax office confirmation [Sample data — unverified]',
                        'steps': '1. Complete application in inPol portal and book appointment at Voivodeship Office.\n2. Submit documents in person and give biometrics.\n3. Receive official stamp in passport authorizing stay during processing.\n4. Receive positive decision (decyzja).\n5. Collect biometric residence card (Karta Pobytu) [Sample data — unverified].',
                        'fees_and_duration': 'Application fee: 440 PLN + 100 PLN plastic card fee [Sample data — unverified]. Duration: 3-6 months.',
                        'validity': 'Issued for the duration of employment up to 3 years.',
                        'notes': 'The red stamp in the passport legally protects your stay while your application is being processed.',
                    },
                    'tr': {
                        'title': 'Polonya Oturum ve Çalışma Kartı (Karta Pobytu)',
                        'summary': "Polonya'da çalışan veya eğitim gören yabancıların valilik (Urząd Wojewódzki) nezdinde aldığı 3 yıla kadar geçerli geçici oturum izni.",
                        'eligibility': "Polonya'da yasal bulunmak, asgari ücretin üzerinde iş sözleşmesi, sağlık sigortası ve konut kira sözleşmesi [Örnek veri — doğrulanmadı].",
                        'required_documents': "• İşverenin doldurduğu Załącznik 1 eki\n• 4 adet biyometrik fotoğraf\n• Pasaport fotokopisi\n• ZUS sigorta kaydı ve kira sözleşmesi\n• Harç yatırıldı makbuzu [Örnek veri — doğrulanmadı]",
                        'steps': "1. inPol portalı üzerinden form doldurup randevu alma.\n2. Valilik yabancılar şubesine giderek evrak teslimi ve parmak izi verme.\n3. Pasaporta inceleme sürerken yasal kalış sağlayan kırmızı mührün basılması.\n4. Karar (decyzja) onayı ve Karta Pobytu kartının teslim alınması [Örnek veri — doğrulanmadı].",
                        'fees_and_duration': "Başvuru harcı: 440 PLN + kart basım harcı: 100 PLN [Örnek veri — doğrulanmadı]. Süre: 3-6 ay.",
                        'validity': "İş sözleşmesine bağlı olarak 3 yıla kadar verilir.",
                        'notes': "Pasaporta basılan kırmızı valilik mührü (czerwona pieczątka) kart çıkana kadar ülkede yasal kalış hakkı tanır.",
                    }
                }
            }
        ]
    }
]
