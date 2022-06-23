from django.shortcuts import redirect
from home.models import user_services
from login.views import *
from django.contrib.auth import logout


def main(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return redirect('/login')


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')


def delete(request, id):
    if request.user.is_authenticated:
        service = user_services.objects.get(id=id)
        service.delete()
        return redirect(home)
    else:
        return redirect('/login')
