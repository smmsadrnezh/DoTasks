from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^lists/$', include('tasks.urls')),
    url(r'^$', 'lists.views.home'),
    url(r'^admin/', include(admin.site.urls)),
]

