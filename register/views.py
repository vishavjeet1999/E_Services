from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        try:
            myUser = User.objects.create_user(username, email, password)
            myUser.first_name = first_name
            myUser.last_name = last_name
            myUser.save()
            data = {
                'success': 'User Successfully Created!'
            }
            return render(request, 'login.html', data)
        except:
            data = {
                'message': 'User Already Exists for this Email Address!'
            }
            return render(request, 'register.html', data)
    return render(request, 'register.html')
