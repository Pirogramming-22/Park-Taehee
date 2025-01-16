from django.urls import path
from . import views

urlpatterns = [
    path('devtools/list/', views.devtool_list, name='devtool_list'),
    path('devtools/<int:id>/', views.devtool_detail, name='devtool_detail'),
    path('devtools/new/', views.devtool_create, name='devtool_create'),
    path('devtools/<int:id>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtools/<int:id>/delete/', views.devtool_delete, name='devtool_delete'),
]