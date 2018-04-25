from django.conf.urls import url

from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),  
    url(r'^home$', views.home),  
    url(r'^courts$', views.courts),
    url(r'^map$', views.map),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^new_court$', views.new_court),
    url(r'^add_court$', views.add_court),
]  