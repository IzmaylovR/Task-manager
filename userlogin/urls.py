from django.conf.urls import url
from tasks import views

urlpatterns = [

    url(r'^add/', views.new_task),
    url(r'^update/(?P<id>\d+)/', views.update_task),
    url(r'^delete/(?P<id>\d+)/', views.delete_task),

]
