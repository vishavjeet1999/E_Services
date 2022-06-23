from django.shortcuts import redirect, render
from home.models import category, user_services
from django.contrib.auth.models import User

from home.views import home
from E_Services.views import main
# Create your views here.


def myServices(request):
    if request.user.is_authenticated:
        categories = category.objects.all()
        services = user_services.objects.filter(uploaded_by=request.user)
        data = {
            'categories': categories,
            'services': services
        }
        return render(request, 'myServices.html', data)
    else:
        return redirect('/login')


def setting(request):
    if request.user.is_authenticated:
        categories = category.objects.all()
        data = {
            'categories': categories,
        }
        return render(request, 'setting.html', data)
    else:
        return redirect('/login')


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_password = request.POST['old']
            new_password = request.POST['new']
            current_user = User.objects.get(username=request.user)

            if(current_user.check_password(old_password)):
                current_user.set_password(new_password)
                current_user.save()
                categories = category.objects.all()
                data = {
                    'categories': categories,
                    'success': 'Password changed successfully! Login Again with new Password'
                }
                return render(request, 'login.html', data)
            else:
                categories = category.objects.all()
                data = {
                    'categories': categories,
                    'message': 'Incorrect old password!'
                }
                return render(request, 'setting.html', data)

        return redirect(main)
    else:
        return redirect('/login')
