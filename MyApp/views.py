
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Dashboard
def home(request):
    all_tasks = Task.objects.all().order_by('due_date', 'id')

    total_tasks = all_tasks.count()
    completed_tasks = all_tasks.filter(status='Completed').count()
    pending_tasks = all_tasks.filter(status='Pending').count()

    remaining_tasks = pending_tasks

    progress_percent = (
        round((completed_tasks / total_tasks) * 100)
        if total_tasks > 0 else 0
    )

    recent_tasks = all_tasks[:5]

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'remaining_tasks': remaining_tasks,
        'progress_percent': progress_percent,
        'tasks': recent_tasks,
        'recent_tasks': recent_tasks,
    }

    return render(request, 'home.html', context)


# View all study tasks
def task_list(request):
    tasks = Task.objects.all().order_by('due_date', 'id')

    context = {
        'tasks': tasks,
        'pending_count': tasks.filter(status='Pending').count(),
        'completed_count': tasks.filter(status='Completed').count(),
    }

    return render(request, 'Tasks.html', context)


# Create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})


# Delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(
        request,
        'task_confirm_delete.html',
        {'task': task}
    )


# Edit a task
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'task_form.html',
        {'form': form, 'task': task}
    )


# Mark a task as completed or pending
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        if task.status == 'Pending':
            task.status = 'Completed'
        else:
            task.status = 'Pending'

        task.save()

    return redirect('task_list')
