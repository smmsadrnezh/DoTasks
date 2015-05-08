from django.shortcuts import render

from tasks.models import Tasks
from tasks.forms import taskForm


def tasks(request, listid):
    newTaskForm = taskForm()
    if request.method == "POST":
        newTaskForm = taskForm(request.POST)
        if newTaskForm.is_valid():
            newRow = Tasks();
            newRow.title = newTaskForm.cleaned_data['title']
            newRow.list_id = int(listid)
            newRow.save()
        else:
            newTaskForm = taskForm()

    return render(request, 'tasks.html', {
        'PageTitle': "CeDoTasks - Tasks",
        'task': Tasks.objects.filter(list_id=listid),
        'newTaskForm': newTaskForm
    })