

from django.shortcuts import render, redirect,get_object_or_404
from .forms import CreateTaskForm
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    return render(request, "home.html")




@login_required
def tasks(request):
    tasks = task.objects.filter(user=request.user,datecomplete__isnull=True)
    return (render(request, "tasks.html",{"tasks":tasks,"estute":"Incompleted"}))

@login_required
def task_completed(request):
    tasks = task.objects.filter(user=request.user,datecomplete__isnull=False).order_by("-datecomplete")
    return render(request,"tasks.html",{"tasks":tasks,"estute":"Completed"})

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "created_task.html", {
            "form": CreateTaskForm,
        })
    else:
        try:
            form = CreateTaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        
        except ValueError:
                 return render(request, "created_task.html", {
                "error":"please provide valide data",
 
                     })


#listar tarea individual
@login_required    
def task_detail(request,task_id):
    if request.method=="GET":
        tasks=get_object_or_404(task,pk=task_id,user=request.user)
        form = CreateTaskForm(instance=tasks)
        return render(request,("task_detail.html"),{"tasks":tasks, "form":form})
    else:
        try:
            tasks=get_object_or_404(task,pk=task_id,user=request.user)
            form=CreateTaskForm(request.POST,instance=tasks)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(request,("task_detail.html"),{"tasks":tasks, "form":form, "error":"Error updating task"})

@login_required
def complete_task(request,task_id):
    tasks=get_object_or_404(task, pk=task_id, user=request.user)
    if  request.method=="POST":
        tasks.datecomplete = timezone.now()
        tasks.save()
        #print(tasks.save())
        return redirect("tasks")
    
@login_required   
def delete_task(request,task_id):
    tasks=get_object_or_404(task, pk=task_id, user=request.user)
    if  request.method=="POST":
        tasks.delete()
        return redirect("tasks")
         