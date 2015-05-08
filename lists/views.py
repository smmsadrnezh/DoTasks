from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from lists.models import Lists


# Create your views here.
def home(request):
    t = get_template('lists.html')
    pageHtml = t.render(Context({'list': Lists.objects.all}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': "CeDoTasks - Lists"}))
    return HttpResponse(html)