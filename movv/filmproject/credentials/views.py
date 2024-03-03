from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('filmapp/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/')

    return render(request, "auth.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['password1']
        if password == conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "usernametaken")
                print("usernametaken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save();
                print("user created")
                return redirect('/')
        else:
            messages.info(request, "password not matched")
            return redirect('/')


    return render(request, "auth.html")

def logout(request):
    auth.logout(request)
    return redirect('/')