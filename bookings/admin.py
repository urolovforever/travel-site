from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin configuration for Bookings"""
    list_display = ('full_name', 'package', 'email', 'number_of_people', 'preferred_date', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'preferred_date', 'package__destination')
    search_fields = ('full_name', 'email', 'phone', 'package__title')
    date_hierarchy = 'created_at'
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at', 'total_price')

    fieldsets = (
        ('Booking Details', {
            'fields': ('package', 'status', 'preferred_date', 'number_of_people', 'total_price')
        }),
        ('Customer Information', {
            'fields': ('full_name', 'email', 'phone', 'country')
        }),
        ('Message', {
            'fields': ('message', 'admin_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_confirmed', 'mark_as_cancelled']

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, f'{queryset.count()} bookings marked as confirmed.')
    mark_as_confirmed.short_description = 'Mark selected bookings as confirmed'

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, f'{queryset.count()} bookings marked as cancelled.')
    mark_as_cancelled.short_description = 'Mark selected bookings as cancelled'
