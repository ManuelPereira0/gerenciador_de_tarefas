from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

# Create your views here.
@login_required
def taskList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasks_done_recently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    tasks_done = Task.objects.filter(done='done', user=request.user).count()
    tasks_doing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks, 'tasks_done_recently': tasks_done_recently,
    'tasks_done': tasks_done, 'tasks_doing': tasks_doing})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk = id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task = form.save()
            messages.info(request,'Tarefa criada com sucesso!')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addTask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            task.save()
            messages.info(request,"Tarefa editada com sucesso!")
            return redirect('/')
        else:
            return render(request, 'tasks/editTask.html', {'task': task, 'form': form})
    else:
        return render(request, 'tasks/editTask.html', {'task': task, 'form': form})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.done == 'doing' or task.done == 'to do':
        task.done = 'done'
    else:
        task.done = 'doing'
    task.save()
    return redirect('/')