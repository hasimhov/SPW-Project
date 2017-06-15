from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.wall, name='wall'),
	url(r'^reply/$',views.reply, name='reply'),
	url(r'^posts/$',views.post, name='post'),
	url(r'^freqapt/$',views.freqapt, name='freqapt'),
	url(r'^freq/$',views.freq, name='freq'),
	url(r'^allusers/$',views.allusers, name='allusers'),
    url(r'^profile/(?P<emailId>[\w._%+-]+@[\w.-]+\.[\w]{2,6})$', views.profile, name='profile'),
	url(r'^settings/$',views.settings, name='settings'),
	url(r'^logout/$',views.logout, name='logout'),
	url(r'^checker/$',views.checker, name='checker'),


	]