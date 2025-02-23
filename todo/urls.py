from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('completed/', views.completed, name='completed'),
    path('delete/<str:task_id>/', views.delete, name='delete'),
    path('remaining/', views.remaining, name='remaining'),
    path('task_details/<str:task_id>/', views.task_details, name='task_details'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle/<str:task_id>/', views.toggle, name='toggle'),
    path('remove/<str:task_id>/', views.remove, name='remove'),

]
