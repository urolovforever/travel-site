from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    # Create booking
    path('create/<slug:package_slug>/', views.BookingCreateView.as_view(), name='booking_create'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create_generic'),

    # List bookings (admin only)
    path('list/', views.BookingListView.as_view(), name='booking_list'),
]
