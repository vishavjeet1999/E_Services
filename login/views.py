from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from home.views import home
# Create your views here.


def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            data = {
                'message': 'Wrong Username or password!'
            }
            return render(request, 'login.html', data)
    return render(request, 'login.html')
