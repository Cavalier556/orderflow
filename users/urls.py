from django.urls import path
from .views import MyLoginView, logout
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', logout,name='logout'),
]