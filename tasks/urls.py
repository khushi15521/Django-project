from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', views.dashboard, name='dashboard'),
    path('today/', views.today_tasks, name='today_tasks'),
    path('upcoming/', views.upcoming_tasks, name='upcoming_tasks'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/complete/', views.toggle_complete, name='toggle_complete'),
]
