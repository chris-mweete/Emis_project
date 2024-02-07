
from .views import dashboard, index, login, logout, register
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('register', register,name='register'),
    path('login', login,name='login' ),
    path('dashboard', dashboard,name='login'),
     path('logout', logout,name='logout'),
]