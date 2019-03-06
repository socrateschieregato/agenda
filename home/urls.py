from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.my_logout, name='my_logout')
]
