from django.conf.urls import include, url
from django.contrib import admin
from tasks import views

urlpatterns = [

    url(r'^add/', views.new_task),
    url(r'^update/(?P<id>\d+)/', views.update_task),
    url(r'^delete/(?P<id>\d+)/', views.delete_task),

]
