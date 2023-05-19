from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.page1),
    path('team/', views.page2),
    path('review/', views.page3),
    
]
