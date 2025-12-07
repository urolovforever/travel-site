from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Destination


@admin.register(Destination)
class DestinationAdmin(TranslationAdmin):
    """
    Admin configuration for Destination model with modeltranslation support.
    TranslationAdmin provides language tabs in the admin interface.
    """
    list_display = ('title', 'slug', 'published', 'featured', 'created_at')
    list_filter = ('published', 'featured', 'created_at')
    search_fields = ('title', 'title_en', 'title_uz', 'title_ru', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('published', 'featured')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'main_image')
        }),
        ('Content', {
            'fields': ('short_description', 'description')
        }),
        ('SEO', {
            'fields': ('meta_keywords', 'meta_description'),
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
