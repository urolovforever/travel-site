from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Package
from bookings.models import Booking


class BookingInline(admin.TabularInline):
    """Inline admin for bookings"""
    model = Booking
    extra = 0
    fields = ('full_name', 'email', 'number_of_people', 'preferred_date', 'status')
    readonly_fields = ('full_name', 'email', 'number_of_people', 'preferred_date')
    can_delete = False


@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    """
    Admin configuration for Package model with modeltranslation support.
    """
    list_display = ('title', 'destination', 'price', 'duration_days', 'available', 'published', 'featured')
    list_filter = ('published', 'available', 'featured', 'destination', 'created_at')
    search_fields = ('title', 'title_en', 'title_uz', 'title_ru', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('available', 'published', 'featured')

    inlines = [BookingInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'destination', 'main_image')
        }),
        ('Content', {
            'fields': ('description', 'itinerary', 'inclusions', 'exclusions')
        }),
        ('Pricing & Duration', {
            'fields': ('price', 'currency', 'duration', 'duration_days', 'max_people')
        }),
        ('SEO', {
            'fields': ('meta_keywords', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('available', 'published', 'featured')
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
