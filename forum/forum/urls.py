from django.conf.urls import include, url
from django.contrib import admin
from error.views import *
from django.conf import settings
urlpatterns = [
    # Examples:


    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("app.urls", app_name='app', namespace='app')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT }),
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error