from django.conf import settings
from django.urls import URLPattern, URLResolver

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


def list_urls(lis, acc=None, tag=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        if tag != 'name':
            yield acc + [str(l.pattern)]
        yield [str(l.name)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc, tag=tag)


def call_list_urls_and_name(parm="urls"):
    return list_urls(urlconf.urlpatterns, acc=None, tag=parm)
