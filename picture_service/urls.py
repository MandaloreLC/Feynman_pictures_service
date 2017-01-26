from django.conf import settings
from django.conf.urls import url, static
from django.views.static import serve

from . import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.display_image, name="display_image"),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]