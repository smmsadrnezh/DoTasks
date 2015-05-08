from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from tasks.models import Tasks

def tasks(request, listid):
    t = get_template('tasks.html')
    pageHtml = t.render(Context({'task': Tasks.objects.filter(list_id=listid)}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': "CeDoTasks - Lists"}))
    return HttpResponse(html)