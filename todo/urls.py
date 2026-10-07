from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:id>/', views.complete, name='complete'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('clear-completed/', views.clear_completed, name='clear_completed'),
]
