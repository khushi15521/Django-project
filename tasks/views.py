from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import UserRegistrationForm, TaskForm
from datetime import date
from django.db.models import Q

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def get_task_stats(user):
    tasks = Task.objects.filter(user=user)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
    return {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'progress': progress,
    }

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        
    # Filter by priority
    priority = request.GET.get('priority', '')
    if priority and priority != 'All':
        tasks = tasks.filter(priority=priority)
        
    # Filter by category
    category = request.GET.get('category', '')
    if category and category != 'All':
        tasks = tasks.filter(category=category)

    stats = get_task_stats(request.user)
    form = TaskForm()
    
    context = {
        'tasks': tasks,
        'stats': stats,
        'search_query': search_query,
        'current_priority': priority,
        'current_category': category,
        'form': form,
        'active_nav': 'dashboard'
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def today_tasks(request):
    today = date.today()
    tasks = Task.objects.filter(user=request.user, due_date=today)
    stats = get_task_stats(request.user)
    form = TaskForm()
    
    context = {
        'tasks': tasks,
        'stats': stats,
        'form': form,
        'active_nav': 'today'
    }
    return render(request, 'tasks/today.html', context)

@login_required
def upcoming_tasks(request):
    today = date.today()
    tasks = Task.objects.filter(user=request.user, due_date__gt=today).order_by('due_date')
    stats = get_task_stats(request.user)
    form = TaskForm()
    
    context = {
        'tasks': tasks,
        'stats': stats,
        'form': form,
        'active_nav': 'upcoming'
    }
    return render(request, 'tasks/upcoming.html', context)

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=True)
    stats = get_task_stats(request.user)
    form = TaskForm()
    
    context = {
        'tasks': tasks,
        'stats': stats,
        'form': form,
        'active_nav': 'completed'
    }
    return render(request, 'tasks/completed.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully')
            # Determine where to redirect based on HTTP_REFERER if possible, or dashboard
            next_url = request.POST.get('next', 'dashboard')
            return redirect(next_url)
    return redirect('dashboard')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            next_url = request.POST.get('next', 'dashboard')
            return redirect(next_url)
    return redirect('dashboard')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully')
        next_url = request.POST.get('next', 'dashboard')
        return redirect(next_url)
    return redirect('dashboard')

@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        status = 'completed' if task.completed else 'marked pending'
        messages.success(request, f'Task {status}')
        next_url = request.POST.get('next', 'dashboard')
        return redirect(next_url)
    return redirect('dashboard')
