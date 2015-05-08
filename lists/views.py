from django.shortcuts import render
from django.http import HttpResponseRedirect

from lists.models import Lists
from lists.forms import ListForm


def home(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = ListForm()

    return render(request, 'lists.html', {
        'PageTitle': "CeDoTasks - Lists",
        'list': Lists.objects.all,
        'form': form
    })