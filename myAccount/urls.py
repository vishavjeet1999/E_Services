from django.urls import path
from .views import *


urlpatterns = [
    path('myServices/', myServices),
    path('setting/', setting),
    path('changePassword/', changePassword)
]
