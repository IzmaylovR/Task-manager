from django.conf.urls import url
from userlogin import views

urlpatterns = [

    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),



]
