from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def tasks(request,list_id):
    t = get_template('tasks.html')
    pageHtml = t.render({'task': Tasks.get(id=list_id)})
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': "CeDoTasks - Lists"}))
    return HttpResponse(html)