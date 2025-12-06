from django.urls import path
from . import views

app_name = 'destinations'

urlpatterns = [
    # Public views
    path('', views.DestinationListView.as_view(), name='destination_list'),
    path('<slug:slug>/', views.DestinationDetailView.as_view(), name='destination_detail'),

    # CRUD views (require authentication)
    path('create/', views.DestinationCreateView.as_view(), name='destination_create'),
    path('<slug:slug>/edit/', views.DestinationUpdateView.as_view(), name='destination_update'),
    path('<slug:slug>/delete/', views.DestinationDeleteView.as_view(), name='destination_delete'),

    # JSON API endpoints
    path('api/list/', views.destination_list_json, name='destination_list_json'),
    path('api/<slug:slug>/', views.destination_detail_json, name='destination_detail_json'),
]
