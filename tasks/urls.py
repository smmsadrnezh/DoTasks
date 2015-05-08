from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', 'tasks.views.tasks'),
]