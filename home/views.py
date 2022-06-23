from django.http import JsonResponse
from django.shortcuts import redirect, render
from home.models import Comments, user_services, category
from login.views import login
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        services = user_services.objects.all()
        categories = category.objects.all()
        data = {
            'services': services,
            'categories': categories
        }
        return render(request, 'index.html', data)
    else:
        return redirect('/login')


def service_detail(request, id):
    if request.user.is_authenticated:
        service = user_services.objects.get(id=id)
        categories = category.objects.all()
        comments = Comments.objects.filter(service=service)
        data = {
            'service': service,
            'categories': categories,
            'comments': comments
        }
        return render(request, 'shop-details.html', data)
    else:
        return redirect('/login')


def getComments(request, id):
    if request.user.is_authenticated:
        def my_function(item): 
            temp = {
                "sno": item.sno,
                "comment": item.comment,
                "user": item.user.username,
                "sid": item.service.id,
                "timestamp": item.timestamp.strftime("%I:%M %p %d %b %Y")
            }
            return temp
        data = {
            'comments': list(map(my_function, Comments.objects.all()))
        }

        return JsonResponse(data)
    else:
        return redirect('/login')


def postComment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = request.POST['comment']
            user = request.user
            serviceSno = request.POST['serviceSno']
            service = user_services.objects.get(id=serviceSno)

            comment = Comments(comment=comment, user=user, service=service)
            comment.save()
            data = {
                'response': 'done'
            }
            return JsonResponse(data)
    else:
        return redirect('/login')


def deleteComment(request, sno):
    if request.user.is_authenticated:
        comment = Comments.objects.get(sno=sno)
        service = comment.service
        comment.delete()
        return redirect(f'/home/{service.id}')
    else:
        return redirect('/login')


def giveRating(request, id):
    if request.user.is_authenticated:
        service = user_services.objects.get(id=id)
        service.service_rating = int(request.POST['rating']) if service.service_rating == 0 else (
            service.service_rating + int(request.POST['rating']))//2
        service.save()
        return redirect(f'/home/{service.id}')
    else:
        return redirect('/login')
