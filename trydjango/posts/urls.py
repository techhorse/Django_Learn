
from django.conf.urls import url,include
from django.contrib import admin
from posts.views import (
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update,
)



urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^delete/$', post_delete),
    url(r'^detail/$', post_detail),
    url(r'^list/$', post_list),
    url(r'^update/$', post_update),

    
]
