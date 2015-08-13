from django.conf.urls import url

urlpatterns = [
  url(r'^$', 'main.views.home', name='home'),
  url(r'^about/$', 'main.views.about', name='about'),
]