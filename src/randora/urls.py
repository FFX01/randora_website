from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# main url router for routing urls to app specific url routers
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^main/', include('main.urls')),
]

# The below setting is for development only. Static files should be served from
# a seperate server, such as a cdn
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)