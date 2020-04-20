from django.conf.urls import  url
from cmdb import  views

urlpatterns = [
    url(r'^api$',views.index),
    url(r'^show_server$',views.show_server),

]