from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	path('login/',views.loginview, name='login'),
	path('logout/',views.logoutview, name='logout'),
	path('register/', views.register, name='register')
]