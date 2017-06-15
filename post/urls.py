from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.wall, name='wall'),
	url(r'^reply/$',views.reply, name='reply'),
	url(r'^posts/$',views.post, name='post')
	]