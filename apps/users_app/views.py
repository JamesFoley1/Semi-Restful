from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'users/index.html', {"users" : Users.objects.all() })

def new(request):
    return render(request, 'users/index1.html')

def display(request, id):
    return render(request, 'users/index2.html', {"users" : Users.objects.get(id = id) })

def edit(request, id):
    return render(request, 'users/index3.html', {"users" : Users.objects.get(id = id) })

def create(request):
    if request.method == 'POST':
        Users.objects.create(name = request.POST['name'], email = request.POST['email'])
        return redirect('/new')

def update(request, id):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tags, value in errors.items():
            messages.error(request, value, extra_tags=tags)
            return redirect('/edit/'+id)
    else:
        users = Users.objects.get(id = id)
        users.name = request.POST['name']
        users.email = request.POST['email']
        users.save()
        messages.success(request, "Users successfully updated!")
        return redirect('/')

def delete(request, id):
    Users.objects.get(id = id).delete()
    return redirect('/')