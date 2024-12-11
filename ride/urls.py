from ride.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('nonveg/',nonveg,name='nonveg'),
]