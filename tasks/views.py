from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from models import Tasks
from forms import TaskForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    all_tasks = Tasks.objects.all()
    return render_to_response('index.html', {'all_tasks': all_tasks,
                                             'username': auth.get_user(request).username})

@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def update_task(request, id):
    task = Tasks.objects.get(pk=id)
    form = TaskForm(request.POST or None, instance=task)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'create_task.html', {'form': form})

@login_required
def delete_task(request, id):
    task = Tasks.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect('/')
