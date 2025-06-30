from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_scans, name='get_scans'),
    path('add/', views.add_scan, name='add_scan'),
    path('edit/<int:scan_id>/', views.edit_scan, name='edit_scan'),
    path('delete/<int:scan_id>/', views.delete_scan, name='delete_scan'),

]