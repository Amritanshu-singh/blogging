from django.conf.urls import url
from django.contrib import admin

from .views import (
   blog_list,
   blog_create,
   blog_details,
   blog_update,
   blog_delete,

   )

urlpatterns = [
    url(r'^$', blog_list),
    url(r'^create/$', blog_create),
    url(r'^(?P<id>\d+)/$', blog_details, name = 'detail'),
    url(r'^(?P<id>\d+)/edit/$', blog_update, name = 'edit'),
    url(r'^(?P<id>\d+)/delete/$', blog_delete),
]
