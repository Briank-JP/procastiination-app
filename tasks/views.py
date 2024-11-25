from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

# Create your views here.
# Homepage
def homepage(request):
    return render(request, 'tasks/homepage.html')
# fetching all tasks from the database
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# creating a task
def create_task(request):
    # if the form is submited
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm() #display an empty form
    return render(request, 'tasks/create_task.html', {'form': form})

# updating/editing a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task) #prefill the form with data
            
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

#deleting tasks
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST': #if the delete is confirmed
        task.delete() # delete the instance
        return redirect('task_list')  #return to the task list
       
    return render(request, 'tasks/delete_task.html', {'task': task})