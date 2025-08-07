from django.urls import path
from . import views
from .views import PostListView, CategoryListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(),name='post-create'),
    path('<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.detail),
    # path('create/', views.create,name='blogcreate'),
    # path('<int:pk>/delete/', views.delete, name='blogdelete'),
    # path('<int:pk>/update/', views.update, name='blogupdate'),
    path('category/<slug>/',views.category,name='category'),
    path('<int:pk>/createcomment/', views.createcomment,name='createcomment'),
    path('<int:pk>/deletecomment/', views.deletecomment,name='deletecomment'),
    path('<int:pk>/updatecomment/', views.updatecomment,name='updatecomment'),
    path('createfake/',views.createfake),
    ]