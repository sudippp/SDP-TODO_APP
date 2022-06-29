from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modify/<int:pk>/', views.modify, name='modify'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
