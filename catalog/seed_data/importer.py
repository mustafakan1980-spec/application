# -*- coding: utf-8 -*-
from datetime import date
from catalog.models import (
    Country, CountryTranslation,
    Institution, InstitutionTranslation,
    Procedure, ProcedureTranslation,
    SampleDocument, SampleDocumentTranslation,
)


def seed_country_dataset(c_dict, langs, cats, stdout=None):
    """
    Belirtilen ülke sözlüğünü (ülke, kurumlar, prosedürler, çeviriler, örnek belgeler)
    idempotent şekilde veritabanına kaydeder veya günceller.
    """
    # 1. Ülke Kaydı
    c_info = c_dict['country']
    primary_lang = langs.get(c_info['primary_language'], langs.get('en', langs.get('tr')))
    country_obj, _ = Country.objects.update_or_create(
        iso2=c_info['iso2'],
        defaults={
            'slug': c_info['slug'],
            'flag_emoji': c_info['flag_emoji'],
            'primary_language': primary_lang,
            'is_published': True,
        }
    )
    for off_code in c_info.get('official_languages', []):
        if off_code in langs:
            country_obj.official_languages.add(langs[off_code])

    for code, name in c_info.get('translations', {}).items():
        if code in langs:
            CountryTranslation.objects.update_or_create(
                country=country_obj,
                language=langs[code],
                defaults={'name': name}
            )

    if stdout:
        stdout.write(f"  [Ülke] {country_obj}")

    # 2. Kurumlar
    inst_map = {}
    for inst_data in c_dict.get('institutions', []):
        inst_obj, _ = Institution.objects.update_or_create(
            country=country_obj,
            slug=inst_data['slug'],
            defaults={
                'website': inst_data.get('website', ''),
                'phone': inst_data.get('phone', ''),
                'email': inst_data.get('email', ''),
                'address': inst_data.get('address', ''),
            }
        )
        inst_map[inst_data['slug']] = inst_obj
        for lang_code, trans_vals in inst_data.get('translations', {}).items():
            if lang_code in langs:
                InstitutionTranslation.objects.update_or_create(
                    institution=inst_obj,
                    language=langs[lang_code],
                    defaults={
                        'name': trans_vals.get('name', ''),
                        'address_text': trans_vals.get('address_text', ''),
                        'working_hours': trans_vals.get('working_hours', ''),
                    }
                )

    # 3. Prosedürler (Başvurular)
    for proc_data in c_dict.get('procedures', []):
        cat_slug = proc_data['category']
        cat_obj = cats.get(cat_slug)
        inst_obj = inst_map.get(proc_data['institution_slug'])
        proc_obj, _ = Procedure.objects.update_or_create(
            slug=proc_data['slug'],
            defaults={
                'country': country_obj,
                'institution': inst_obj,
                'category': cat_obj,
                'is_published': True,
                'last_verified_at': proc_data.get('last_verified_at', date(2026, 11, 15)),
                'official_source_url': proc_data.get('official_source_url', ''),
            }
        )
        for lang_code, trans_vals in proc_data.get('translations', {}).items():
            if lang_code in langs:
                ProcedureTranslation.objects.update_or_create(
                    procedure=proc_obj,
                    language=langs[lang_code],
                    defaults={
                        'title': trans_vals.get('title', ''),
                        'summary': trans_vals.get('summary', ''),
                        'eligibility': trans_vals.get('eligibility', ''),
                        'required_documents': trans_vals.get('required_documents', ''),
                        'steps': trans_vals.get('steps', ''),
                        'fees_and_duration': trans_vals.get('fees_and_duration', ''),
                        'validity': trans_vals.get('validity', ''),
                        'notes': trans_vals.get('notes', ''),
                    }
                )

        # 4. Örnek Belgeler
        for doc_data in proc_data.get('sample_documents', []):
            doc_obj, _ = SampleDocument.objects.update_or_create(
                procedure=proc_obj,
                storage_path=doc_data['storage_path'],
                defaults={'file_type': doc_data.get('file_type', 'PDF')}
            )
            for lang_code, doc_trans in doc_data.get('translations', {}).items():
                if lang_code in langs:
                    SampleDocumentTranslation.objects.update_or_create(
                        document=doc_obj,
                        language=langs[lang_code],
                        defaults={
                            'title': doc_trans.get('title', ''),
                            'description': doc_trans.get('description', '')
                        }
                    )

    return country_obj
