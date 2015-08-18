from django.conf.urls import url

urlpatterns = [
  url(r'^register/$', 'users.views.register', name='register'),
  url(r'^login/$', 'users.views.users_login', name='login'),
  url(r'^logout/$', 'users.views.users_logout', name='logout'),
  url(r'^profile/(?P<username>\w+)/$', 'users.views.profile', name='profile'),
]