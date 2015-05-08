from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', 'tasks.views.tasks'),
]