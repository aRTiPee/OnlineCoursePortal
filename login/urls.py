from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

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
            url(r'^course1.html/', views.course1, name='course1'),
            url(r'^register1/', views.register_course1, name='register1'),
            url(r'^course2.html/', views.course2, name='course2'),
            url(r'^register2/', views.register_course2, name='register2'),
            url(r'^course3.html/', views.course3, name='course3'),
            url(r'^register3/', views.register_course3, name='register3'),
            url(r'^course4.html/', views.course4, name='course4'),
            url(r'^register4/', views.register_course4, name='register4'),
            url(r'^course5.html/', views.course5, name='course5'),
            url(r'^register5/', views.register_course5, name='register5'),
            ]

if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)