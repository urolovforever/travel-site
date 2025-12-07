from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Admin configuration for Gallery Images"""
    list_display = ('__str__', 'uploaded_at', 'image_preview')
    list_filter = ('uploaded_at',)
    date_hierarchy = 'uploaded_at'
    readonly_fields = ('image_preview', 'uploaded_at')

    fields = ('image', 'image_preview', 'uploaded_at')

    def image_preview(self, obj):
        """Show a thumbnail preview of the image"""
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 300px;" />'
        return '-'

    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True
