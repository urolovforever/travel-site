from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Destination, DestinationGalleryImage


class GalleryImageInline(TranslationTabularInline):
    """Inline admin for gallery images with translation support"""
    model = DestinationGalleryImage
    extra = 1
    fields = ('image', 'caption', 'order')
    ordering = ['order']


@admin.register(Destination)
class DestinationAdmin(TranslationAdmin):
    """
    Admin configuration for Destination model with modeltranslation support.
    TranslationAdmin provides language tabs in the admin interface.
    """
    list_display = ('title', 'country', 'city', 'published', 'featured', 'created_at')
    list_filter = ('published', 'featured', 'country', 'created_at')
    search_fields = ('title', 'title_en', 'title_uz', 'title_ru', 'name', 'city', 'country', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('published', 'featured')
    inlines = [GalleryImageInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'slug')
        }),
        ('Location', {
            'fields': ('country', 'city', 'region')
        }),
        ('Content', {
            'fields': ('short_description', 'description', 'things_to_do')
        }),
        ('Travel Information', {
            'fields': ('best_time_to_visit', 'average_cost')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('published', 'featured')
        }),
    )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
