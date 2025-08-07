from django.urls import path
from . import views
#http://127.0.0.1
urlpatterns = [
    path("", views.landing, name='landing'),
    path("aboutme/", views.about, name='About'),

]
