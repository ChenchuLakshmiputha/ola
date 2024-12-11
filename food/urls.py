from food.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('veg/',veg,name='veg'),
]