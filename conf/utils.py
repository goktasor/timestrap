from django.conf import settings

from .middleware.site import current_request
from .models import Conf, Site


def current_site_id():
    """
    Return the ID of the current Site by checking for a Site in the current
    request and falling back on the default ID in Django settings.
    """
    request = current_request()
    site = getattr(request, 'site', None)
    if site:
        site_id = getattr(site, 'id', None)
    else:
        site_id = settings.SITE_ID
    return site_id


def get_site_setting(name):
    site_conf = Conf.objects.get(site=Site.objects.get(id=current_site_id()))
    return getattr(site_conf, name, None)
