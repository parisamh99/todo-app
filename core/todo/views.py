from django.shortcuts import get_object_or_404, redirect, render
from .models import Task,User
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

@login_required
def task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            form = TaskForm()
        else:
            form = TaskForm()    
     
    tasks = Task.objects.filter(user=request.user)
    context = {"tasks": tasks, "form": form}
    return render(request, "todo/task_list.html", context)    


def update_task(request,pk):
    tasks = get_object_or_404(Task,id=pk ,user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()   
    else:
        form = TaskForm(instance=tasks)
        return render(request,'todo/task_update.html',{'form':form})

def complete_task(request,pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.completed = True
    item.save()
    return redirect('/') 



def delete_task(request,pk):
    item = get_object_or_404(Task,id=pk,user=request.user)
    item.delete()
    return redirect("/")