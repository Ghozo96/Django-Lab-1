from django.urls import path
from .views import todo_list, update_task, show_details, delete_task

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name='todo-list'),
    path('task/', show_details, name='details'),

    path('task/<int:task_id>/update', update_task, name='update'),
    path('task/<int:task_id>/view', show_details, name='details'),
    path('task/<int:task_id>/delete', delete_task, name='delete')
]