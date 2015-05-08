from django.shortcuts import render

from django.http import HttpResponseRedirect

from tasks.models import Tasks
from tasks.forms import taskForm


def tasks(request, listid):
    form = taskForm()
    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = taskForm()

    return render(request, 'tasks.html', {
        'PageTitle': "CeDoTasks - Tasks",
        'task': Tasks.objects.filter(list_id=listid),
        'form': form
    })