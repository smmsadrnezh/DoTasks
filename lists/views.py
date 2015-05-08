from django.shortcuts import render

from lists.models import Lists
from lists.forms import ListForm


def home(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            tform = Lists()
            tform.title = form.cleaned_data['title']
            tform.save()
        else:
            form = ListForm()

    return render(request, 'lists.html', {
        'PageTitle': "CeDoTasks - Lists",
        'list': Lists.objects.all,
        'form': form
    })