from django.contrib import admin
from django.urls import path
from . import views

app_name = 'memories'
urlpatterns = [
    path('', views.index, name='home'),
    path('memorys/', views.MemoryView.as_view(), name='memorys'),
    path('memory/<int:memory_id>/', views.MemoryDetailView.as_view(), name='memory'),
    path('memory/new_memory/', views.NewMemoryView.as_view(), name='new_memory'),
    path('memory/edit_memory/<int:memory_id>/', views.EditMemoryView.as_view(), name='edit_memory'),
    path('memory/edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('memory/edit_interest/', views.EditInterstedView.as_view(), name='edit_interest'),
]