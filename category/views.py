from django.shortcuts import redirect, render
from home.models import user_services
from home.models import category as cat
from login.views import userLogin
# Create your views here.


def category(request, ctg):
    if request.user.is_authenticated:
        service = user_services.objects.filter(service_category=ctg).values()
        categories = cat.objects.all()
        data = {
            'services': service,
            'categories': categories,
            'heading': ctg
        }
        return render(request, 'category.html', data)
    else:
        return redirect('/login')
