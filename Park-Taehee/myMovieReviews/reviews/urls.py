from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('reviews/<int:id>/', views.review_detail, name='review_detail'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/<int:id>/edit/', views.review_edit, name='review_edit'),
    path('reviews/<int:id>/delete/', views.review_delete, name='review_delete'),
]