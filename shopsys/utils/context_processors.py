
from shopsys import settings
from shopsys.apps.catalog.models import *

def shopsys(request):
    active_categories = Category.objects.filter(is_active=True)
    MEDIA_URL = settings.MEDIA_URL
    site_name = settings.SITE_NAME
    meta_keywords = settings.META_KEYWORDS
    meta_description = settings.META_DESCRIPTION
    return locals()
