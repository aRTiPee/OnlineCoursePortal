from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.Index, name='index'),
            url(r'^signin/', views.signin, name='signin'),
            url(r'^signup.html/', views.Index4, name='index4'),
            url(r'^signup/', views.signup, name='signup'),
            url(r'^log_out/', views.log_out, name='log_out'),
            ]
