from django.shortcuts import render

from tasks.models import Tasks

from tasks.forms import TaskForm


def tasks(request, listid):
    newTaskForm = TaskForm()

    if request.method == "POST":
        delChoices = request.POST.getlist('Deletechoices[]')
        donChoices = request.POST.getlist('Donechoices[]')
        for i in delChoices:
            Tasks.objects.filter(id=i).delete()
        for i in donChoices:
            Tasks.objects.filter(id=i).update(list_id='4')

        newTaskForm = TaskForm(request.POST)
        if newTaskForm.is_valid():
            newRow = Tasks();
            newRow.title = newTaskForm.cleaned_data['title']
            newRow.list_id = int(listid)
            newRow.save()
        else:
            newTaskForm = TaskForm()

    return render(request, 'tasks.html', {
        'PageTitle': "CeDoTasks - Tasks",
        'task': Tasks.objects.filter(list_id=listid),
        'newTaskForm': newTaskForm,
    })