from django.shortcuts import render , HttpResponse ,redirect
from home.models import Task
from home.forms import TaskForm

# Create your views here.
def home(request):
    context = {'success': False , 'name':'samar'}
    if request.method == 'POST':
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title , desc)
        ins = Task(taskTitle=title , taskDesc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html' , context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    # for item in allTasks:
    # print(item.taskTitle)
    # print(allTasks)
    return render(request, 'tasks.html' , context)

# def tasks(request):
#     if request.method == 'POST':
#         # Delete task
#         task_id = request.POST['task_id']
#         task = Task.objects.get(id=task_id)
#         task.dele9te()
#         return redirect('tasks')  # Redirect to the tasks page after deletion

#     allTasks = Task.objects.all()
#     context = {'tasks': allTasks}
#     return render(request, 'tasks.html', context)


def update(request , pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/tasks')

    else:
        form = TaskForm(instance=todo)
    context={
        'form':form

    }
    return render(request, 'update.html' , context)


def delete(request , pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/tasks')
    return render(request, 'delete.html')