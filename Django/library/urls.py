from django.urls import path
from . import views
urlpatterns = [
    path('', views.booklist, name='booklist'),
    path('<int:pk>/', views.bookdetail),
    path('create/', views.create, name='bookcreate'),
    ]