from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts.views import *

urlpatterns = [
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
	url(r'^logout/$', logout, name='logout'),
	
	url(r'^create/$', CreateUserView.as_view(), name='create'),
]
