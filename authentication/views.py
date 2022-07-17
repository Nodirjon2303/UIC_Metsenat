from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def loginView(request,*args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'error': "Username and password is not correct"}
    return render(request, 'login.html', context)
