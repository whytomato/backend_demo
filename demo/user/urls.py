from django.urls import path
from .views import *

urlpatterns=[
    path('register',register),
    path('sendcode',sendcode),
    path('login',login),
    path('test',test),
    path('test_1',test_redis_connection)
]