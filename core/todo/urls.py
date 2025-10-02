from django.urls import path
from .views import task,update_task,delete_task,complete_task

app_name = 'todo'

urlpatterns = [
    path('', task, name="task_list"),
    path('update/<str:pk>/', update_task, name="update_task"),
    path('complete/<str:pk>/', complete_task, name="complete_task"),
    path('delete/<str:pk>/', delete_task, name="delete_task"),
    
]