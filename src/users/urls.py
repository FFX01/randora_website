from django.conf.urls import url

urlpatterns = [
  url(r'^register/$', 'users.views.register', name='register'),
  url(r'^login/$', 'users.views.login', name='login'),
  url(r'^logout/$', 'users.views.logout', name='logout'),
  url(r'^profile/$', 'users.views.profile', name='profile'),
]