from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Cambia el nombre de la vista si es necesario
    path('idea/', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/new/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('about/', views.about_view, name='about'),  # Agrega esta línea para la vista about
]
