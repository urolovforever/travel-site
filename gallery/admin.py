from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Admin configuration for Gallery Images"""
    list_display = ('caption', 'destination', 'package', 'uploaded_at')
    list_filter = ('destination', 'package', 'uploaded_at')
    search_fields = ('caption',)
    date_hierarchy = 'uploaded_at'

    fieldsets = (
        ('Image', {
            'fields': ('image', 'caption')
        }),
        ('Association', {
            'fields': ('destination', 'package'),
            'description': 'Optionally link this image to a destination or package'
        }),
    )
