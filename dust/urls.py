from django.urls import path
from . import views
urlpatterns = [
    path('', views.shoplist, name='shoplist'),
    path('<int:pk>/', views.shopdetail),
    ]