from django.shortcuts import render

from django.http import HttpResponseRedirect

from tasks.models import Tasks
from tasks.forms import taskForm


def tasks(request, listid):
    form = taskForm()
    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            tform = Tasks();
            tform.title = form.cleaned_data['title']
            tform.list_id = int(listid)
            tform.save()
        else:
            form = taskForm()

    return render(request, 'tasks.html', {
        'PageTitle': "CeDoTasks - Tasks",
        'task': Tasks.objects.filter(list_id=listid),
        'form': form
    })