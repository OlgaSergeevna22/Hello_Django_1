from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('home/', views.func),
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),


]