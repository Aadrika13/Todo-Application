from django.shortcuts import render, redirect
from .models import Todo, Profile
from django.contrib import messages


# Create your views here.
#==================================== HOME ===================================================================

def home(request):
    return render(request, 'home.html')

#==================================== TODo ===================================================================

def todo(request):

    user = request.user

    todos = Todo.objects.filter(is_completed = False,user = user)

    parameters = {
        'todos':todos,
        'user':user
    }

    return render(request, 'todo.html', parameters)

#=================================== ADD_TODO ================================================================

def add_todo(request):

    if request.method == 'POST':

        task = request.POST.get('task')
        created_at = request.POST.get('created_at')

        todo = Todo (
            user = request.user,
            task = task,
            created_at = created_at
        )

        todo.save()
        messages.success(request, 'Todo added sucessfully')
        return redirect('todo')
    
    return render(request, 'add_todo.html')

#=================================== DELETE_TODO =============================================================

def delete_todo(request, id):

    todo = Todo.objects.get(id=id)
    todo.delete()

    messages.success(request, 'Todo deleted sucessfully')
    return redirect('todo')

#=================================== UPDATE_TODO ==============================================================

def update_todo(request, id):

    todo = Todo.objects.get(id=id)

    if request.method == 'POST' :
        task = request.POST.get('task')
        created_at = request.POST.get('created_at')

        todo.task = task 
        todo.created_at = created_at

        todo.save()

        messages.success(request, 'Todo updated sucessfully')
        return redirect('todo')
    
    parameters = {
        'todo':todo
    }

    return render(request, 'update_todo.html', parameters)

#================================== MARK_COMPLETED ============================================================

def mark_completed(request, id):

    todo = Todo.objects.get(id=id)

    todo.is_completed = True
    todo.save()

    messages.success(request, 'Todo Marked Completed!!')
    return redirect('todo')

#================================== UPLOAD_PIC =================================================================

def upload_profile(request):

    if request.method == 'POST':

        profile = request.FILES['profile']

        new_profile = Profile(
            title = 'demo profile',
            profile = profile
        )

        new_profile.save()

        messages.success(request, 'Profile uploaded successfully')
        return redirect('todo')
    
    return render(request, 'upload_profile.html')