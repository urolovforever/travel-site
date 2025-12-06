from django.contrib import admin
from .models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'website_url')
    list_editable = ('display_order', 'active')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'logo', 'website_url')
        }),
        ('Display Settings', {
            'fields': ('display_order', 'active')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
