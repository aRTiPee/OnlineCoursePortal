from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.Index, name='index'),
            url(r'^full-width.html/', views.Index2, name='index2'),
            url(r'^style-demo.html/', views.Index3, name='index3'),
            url(r'^signup.html/', views.Index4, name='index4'),
            url(r'^signup/', views.signup, name='signup'),
            ]
