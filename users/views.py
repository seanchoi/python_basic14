from django.shortcuts import render, redirect
from users.models import Users

# Create your views here.

def index(request):
    # if Users.objects.all() is not None:
    data = {
        "users" : Users.objects.all()
    }

    return render(request, 'index.html', data)

def process(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    age = request.POST['age']

    Users.objects.create(first_name = first_name, last_name = last_name, email = email, age = age)
    
    return redirect('/')

def update(request):
    field = request.POST['update_field']
    value = request.POST['new_value']
    id = request.POST['id']

    u = Users.objects.get(id=id)

    print(u)
    print(u.first_name)
    print(field)
    print(value)

    if field == 'first_name':
        u.first_name = value
        u.save()
    elif field == 'last_name':
        u.last_name = value
        u.save()
    elif field == 'email':
        u.email = value
        u.save()
    else:
        u.age = value
        u.save()
    
    return redirect('/')

def deleteUser(request):
    id = request.POST['id']

    Users.objects.get(id=id).delete()

    return redirect('/')