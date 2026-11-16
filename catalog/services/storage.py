import logging
from django.conf import settings
from supabase import create_client

logger = logging.getLogger(__name__)


def get_supabase_client():
    """
    Supabase Storage istemcisini başlatır.
    service_role anahtarı yalnızca sunucu tarafında güvenle kullanılır;
    yoksa anon anahtarına düşer.
    """
    url = getattr(settings, 'SUPABASE_URL', None)
    key = (
        getattr(settings, 'SUPABASE_SERVICE_ROLE_KEY', None)
        or getattr(settings, 'SUPABASE_ANON_KEY', None)
    )
    if not url or not key:
        logger.warning("Supabase URL veya anahtarı settings üzerinde eksik.")
        return None
    try:
        return create_client(url, key)
    except Exception as exc:
        logger.error("Supabase istemcisi başlatılamadı: %s", exc)
        return None


def create_sample_document_signed_url(storage_path: str, expires_in: int = 60) -> str | None:
    """
    Supabase Storage private bucket ('sample-documents') içindeki dosya için
    kısa ömürlü (örn. 60 sn) imzalı indirme bağlantısı oluşturur.

    Başarılı olursa imzalı URL dizgisi (string) döner.
    Dosya bulunamazsa veya hata oluşursa None döner.
    """
    if not storage_path:
        return None

    client = get_supabase_client()
    if not client:
        return None

    bucket_name = getattr(settings, 'SUPABASE_STORAGE_BUCKET', 'sample-documents')

    try:
        res = client.storage.from_(bucket_name).create_signed_url(storage_path, expires_in)
        if isinstance(res, dict):
            return res.get('signedURL') or res.get('signedUrl')
        return str(res) if res else None
    except Exception as exc:
        logger.warning(
            "Supabase Storage signed URL oluşturulamadı (bucket: %s, path: %s): %s",
            bucket_name,
            storage_path,
            exc
        )
        return None
