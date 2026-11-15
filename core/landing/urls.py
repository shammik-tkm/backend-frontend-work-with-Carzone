from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    
    # Custom Admin Routes
    path('panel/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('panel/add/', views.custom_admin_add, name='custom_admin_add'),
    path('panel/edit/<int:pk>/', views.custom_admin_edit, name='custom_admin_edit'),
    path('panel/delete/<int:pk>/', views.custom_admin_delete, name='custom_admin_delete'),
    path('panel/categories/', views.custom_admin_categories, name='custom_admin_categories'),
    path('panel/login/', views.admin_login, name='admin_login'),
    path('panel/logout/', views.admin_logout, name='admin_logout'),
    path('panel/categories/', views.custom_admin_categories, name='custom_admin_categories'),
    path('panel/categories/add/', views.custom_admin_category_add, name='custom_admin_category_add'),
    path('panel/categories/<int:pk>/edit/', views.custom_admin_category_edit, name='custom_admin_category_edit'),
    path('panel/categories/<int:pk>/delete/', views.custom_admin_category_delete, name='custom_admin_category_delete'),

]