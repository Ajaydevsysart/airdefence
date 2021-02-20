from django.urls import path
from . import views

urlpatterns = [
    path('addairman',views.addairman,name='addairman'),
    path('user',views.user,name='user'),
       
]