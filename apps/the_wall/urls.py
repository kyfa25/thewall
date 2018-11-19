from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^postMSG$',views.postMSG),
    url(r'^postCMT$',views.postCMT),
]