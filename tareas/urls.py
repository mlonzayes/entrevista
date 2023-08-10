from django.urls import path,include
from .views import MyTaskView


urlpatterns = [
    path('',MyTaskView.home,name='home'),
    path('tasks',MyTaskView.myTask,name='task'),
    path('create_tasks',MyTaskView.createTask,name='create_task')
]
