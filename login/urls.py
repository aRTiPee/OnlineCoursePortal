from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.Index, name='index'),
            url(r'^faculty/', views.Faculty.as_view(), name='faculty'),
            ]
