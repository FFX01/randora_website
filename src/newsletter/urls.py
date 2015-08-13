from django.conf.urls import url

urlpatterns = [
  url(r'^$', 'newsletter.views.home', name='home'),
  url(r'^signed_up/$', 'newsletter.views.signed_up', name='signed_up')
]