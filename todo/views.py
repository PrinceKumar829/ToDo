from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Todo.objects.create(title=title)

        return redirect('index')

    filter_type = request.GET.get('filter', 'all')

    if filter_type == 'active':
        todos = Todo.objects.filter(completed=False)

    elif filter_type == 'completed':
        todos = Todo.objects.filter(completed=True)

    else:
        todos = Todo.objects.all()

    total_count = Todo.objects.count()
    completed_count = Todo.objects.filter(completed=True).count()
    pending_count = Todo.objects.filter(completed=False).count()

    return render(request, 'todo/index.html', {
        'todos': todos,
        'total_count': total_count,
        'completed_count': completed_count,
        'pending_count': pending_count,
        'filter_type': filter_type,
    })


def complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('index')


def edit(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            todo.title = title
            todo.save()

        return redirect('index')

    return render(request, 'todo/edit.html', {'todo': todo})


def clear_completed(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('index')
