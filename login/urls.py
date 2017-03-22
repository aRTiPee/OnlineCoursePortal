from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.Index, name='index'),
            url(r'^signin/', views.signin, name='signin'),
            url(r'^signup.html/', views.IndexSignUp, name='IndexSignUp'),
            url(r'^signup/', views.signup, name='signup'),
            url(r'^log_out/', views.log_out, name='log_out'),
            url(r'^courses.html/', views.courses, name='courses'),
            url(r'^news.html/', views.news, name='news'),
            url(r'^about.html/', views.about, name='about'),
            url(r'^signup_faculty.html/', views.IndexSignup_faculty, name='IndexSignup_faculty'),
            url(r'^signup_faculty/', views.signup_faculty, name='signup_faculty'),
            ]
