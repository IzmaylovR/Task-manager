from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from models import Tasks
from forms import TaskForm

def index(request):
    all_tasks = Tasks.objects.all()
    return render_to_response('index.html', {'all_tasks': all_tasks})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def update_task(request,id):
    task = Tasks.objects.get(pk=id)
    if request.method == 'POST':
        task




def delete_task(request,id):
    task = Tasks.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect('/')