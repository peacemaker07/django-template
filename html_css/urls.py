from django.conf.urls import url
from html_css.views import HtmlCssList

urlpatterns = [
	url(r'^list/$', HtmlCssList.as_view(), name='list'),
]
