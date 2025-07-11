from django.shortcuts import render, redirect
from .models import Task
from .forms import *

def home(request):
    task=Task.objects.all()
    return render(request, 'index.html',{'task':task})

def add_task(request):
    if request.method == 'POST':
        task = request.POST['title']
        description= request.POST['description']
        completed = request.POST.get('completed', False)
        due_date = request.POST['duedate']
        due_time = request.POST['duetime']
        task = Task(title=task, description=description, duedate=due_date, duetime=due_time, complete=completed)
        task.save()
        return redirect('add_task')
    
    return render(request, 'add_task.html')
    
def completed(request):
    task=Task.objects.filter(complete=True)
    return render(request, 'completed.html',{'task':task})

from django.shortcuts import get_object_or_404, render
from .models import Task

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task_title = task.title
    if request.method == 'POST':
        return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))
    return render(request, 'delete.html', {'task': task, 'task_title': task_title})
def remaining(request):
    task=Task.objects.filter(complete=False)
    return render(request, 'remaining.html',{'task':task})

def task_details(request,task_id):
    task=Task.objects.get(id=task_id)
    return render(request, 'task_details.html',{'tasks':task})

from django.shortcuts import get_object_or_404, redirect

def toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))
def remove(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})