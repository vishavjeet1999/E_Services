from django.shortcuts import redirect, render
from home.models import category, user_services
from home.views import home
# Create your views here.


def newService(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newService = user_services()
            newService.image = request.FILES['my_image']
            newService.service_name = request.POST['name']
            newService.service_charges = int(request.POST['charges'])
            newService.service_description = request.POST['desc']
            newService.service_rating = 0
            newService.service_category = request.POST['category']
            newService.uploaded_by = request.user
            newService.service_lat = float(request.POST['latitude'])
            newService.service_long = float(request.POST['longitude'])
            if (newService.service_lat and newService.service_long):
                newService.save()
                return redirect(home)
        categories = category.objects.all()
        data = {
            'categories': categories,
        }
        return render(request, 'newService.html', data)
    else:
        return redirect('/login')
