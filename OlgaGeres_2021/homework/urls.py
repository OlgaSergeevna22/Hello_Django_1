from django.urls import path
from .import views
urlpatterns = [
    path('home/', views.homework),
    path('', views.main_page),
]