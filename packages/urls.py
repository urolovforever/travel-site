from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    # Public views
    path('', views.PackageListView.as_view(), name='package_list'),
    path('<slug:slug>/', views.PackageDetailView.as_view(), name='package_detail'),

    # CRUD views (require authentication)
    path('create/', views.PackageCreateView.as_view(), name='package_create'),
    path('<slug:slug>/edit/', views.PackageUpdateView.as_view(), name='package_update'),
    path('<slug:slug>/delete/', views.PackageDeleteView.as_view(), name='package_delete'),

    # JSON API endpoints
    path('api/list/', views.package_list_json, name='package_list_json'),
    path('api/<slug:slug>/', views.package_detail_json, name='package_detail_json'),
]
