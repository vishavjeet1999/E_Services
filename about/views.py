from django.shortcuts import redirect, render
from home.models import category
from login.views import userLogin
# Create your views here.


def about(request):
    if request.user.is_authenticated:
        categories = category.objects.all()
        data = {
            'categories': categories,
        }
        return render(request, 'about.html', data)
    else:
        return redirect('/login')
