# -*- coding: utf-8 -*-
LANGUAGES_DATA = [
    {'code': 'tr', 'name_native': 'Türkçe', 'is_rtl': False},
    {'code': 'en', 'name_native': 'English', 'is_rtl': False},
    {'code': 'fr', 'name_native': 'Français', 'is_rtl': False},
    {'code': 'de', 'name_native': 'Deutsch', 'is_rtl': False},
    {'code': 'es', 'name_native': 'Español', 'is_rtl': False},
    {'code': 'it', 'name_native': 'Italiano', 'is_rtl': False},
    {'code': 'pt', 'name_native': 'Português', 'is_rtl': False},
    {'code': 'nl', 'name_native': 'Nederlands', 'is_rtl': False},
    {'code': 'ar', 'name_native': 'العربية', 'is_rtl': True},
    {'code': 'ja', 'name_native': '日本語', 'is_rtl': False},
    {'code': 'ko', 'name_native': '한국어', 'is_rtl': False},
]

CATEGORIES_DATA = [
    {
        'slug': 'visa',
        'icon': '✈️',
        'order': 1,
        'translations': {
            'tr': 'Vize Başvuruları',
            'en': 'Visa Applications',
            'fr': 'Demandes de visa',
            'de': 'Visa-Anträge',
            'es': 'Solicitudes de visado',
            'it': 'Domande di visto',
        }
    },
    {
        'slug': 'residence-permit',
        'icon': '🏠',
        'order': 2,
        'translations': {
            'tr': 'Oturum ve İkamet İzni',
            'en': 'Residence & Work Permits',
            'fr': 'Titres de séjour',
            'de': 'Aufenthaltstitel & Niederlassung',
            'es': 'Permisos de residencia',
            'it': 'Permessi di soggiorno',
        }
    },
    {
        'slug': 'education',
        'icon': '🎓',
        'order': 3,
        'translations': {
            'tr': 'Eğitim ve Okul Kayıtları',
            'en': 'Education & School Admission',
            'fr': 'Éducation & Inscriptions scolaires',
            'de': 'Bildung & Hochschulzulassung',
            'es': 'Educación y Admisión escolar',
            'it': 'Istruzione e Iscrizioni scolastiche',
        }
    },
    {
        'slug': 'driving-license',
        'icon': '🚗',
        'order': 4,
        'translations': {
            'tr': 'Sürücü Belgesi / Ehliyet',
            'en': 'Driving Licence',
            'fr': 'Permis de conduire',
            'de': 'Führerschein',
            'es': 'Permiso de conducir',
            'it': 'Patente di guida',
        }
    },
    {
        'slug': 'passport',
        'icon': '🛂',
        'order': 5,
        'translations': {
            'tr': 'Pasaport ve Kimlik',
            'en': 'Passport & Identity',
            'fr': 'Passeport & Identité',
            'de': 'Reisepass & Ausweise',
            'es': 'Pasaporte e Identidad',
            'it': 'Passaporto e Identità',
        }
    },
    {
        'slug': 'work-permit',
        'icon': '💼',
        'order': 6,
        'translations': {
            'tr': 'Çalışma İzni & İş Piyasası',
            'en': 'Work Permits & Employment',
            'fr': 'Autorisations de travail',
            'de': 'Arbeitserlaubnis & Erwerbstätigkeit',
            'es': 'Permisos de trabajo',
            'it': 'Permessi di lavoro',
        }
    },
]
