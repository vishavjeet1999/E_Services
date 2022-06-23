from django.urls import path
from home.views import *


urlpatterns = [
    path('', home),
    path('postComment', postComment),
    path('deleteComment/<int:sno>', deleteComment),
    path('getComments/<int:id>', getComments),
    path('<int:id>', service_detail),
    path('giveRating/<int:id>', giveRating)
]
