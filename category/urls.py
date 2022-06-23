from django.urls import path
from .views import *


urlpatterns = [
    # path('', categories),
    path('<str:ctg>', category)
]
