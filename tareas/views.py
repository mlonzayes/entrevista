from django.shortcuts import render
from .forms import *
from .models import *


class MyTaskView:

    def home(request):
        return render(request,"index.html")
    
    def myTask(request):

        return render(request,"tasks/tasks.html",{})
    
    def createTask(request):
        form=MyTaskForm()
        print(request.POST)
        return render(request,"tasks/create_tasks.html",{
            'form':form
        })
