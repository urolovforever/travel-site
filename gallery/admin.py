from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(TranslationAdmin):
    """Admin configuration for Gallery Images"""
    list_display = ('caption', 'destination', 'package', 'order', 'uploaded_at')
    list_filter = ('destination', 'package', 'uploaded_at')
    search_fields = ('caption', 'caption_en', 'caption_uz', 'caption_ru')
    list_editable = ('order',)
    date_hierarchy = 'uploaded_at'

    fieldsets = (
        ('Image', {
            'fields': ('image', 'caption', 'order')
        }),
        ('Association', {
            'fields': ('destination', 'package'),
            'description': 'Optionally link this image to a destination or package'
        }),
    )
