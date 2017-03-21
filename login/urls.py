from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.Index, name='index'),
            url(r'^full-width.html/', views.Index2, name='index2'),
            url(r'^style-demo.html/', views.Index3, name='index3'),
            ]
