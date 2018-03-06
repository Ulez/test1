from django.conf.urls import  url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)$', views.show)#正则（）为取出这个值。所以传了两个：request，id；
]