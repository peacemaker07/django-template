from django.conf.urls import url
from cmn.views import CmnList

urlpatterns = [
	url(r'^list/$', CmnList.as_view(), name='list'),
]
