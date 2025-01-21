from django.urls import path
from . import views

urlpatterns = [
    path('', views.pirostagram_list, name='pirostagram_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]
