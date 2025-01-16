from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('ideas/<int:id>/', views.idea_detail, name='idea_detail'),
    path('ideas/new/', views.idea_create, name='idea_create'),
    path('ideas/<int:id>/edit/', views.idea_edit, name='idea_edit'),
    path('ideas/<int:id>/delete/', views.idea_delete, name='idea_delete'),
    path('update_interest/<int:idea_id>/', views.update_interest, name='update_interest'),
    path('get_star_states/', views.get_star_states, name='get_star_states'),
]
