from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$',views.signUpHandler, name = 'signUpHandler'),
    url(r'^check/$',views.login, name = 'check'),
    url(r'^check1/$',views.loginHandler, name = 'loginHandler'),
]
