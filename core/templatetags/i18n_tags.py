"""
Custom template tags for multilingual support.

Usage in templates:
{% load i18n_tags %}
{{ object|get_translated:'title' }}
"""

from django import template
from django.utils.translation import get_language

register = template.Library()


@register.filter
def get_translated(obj, field_name):
    """
    Get the translated value of a field based on current language.

    Example:
        {{ destination|get_translated:'title' }}

    This will return title_en, title_uz, or title_ru depending on current language.
    Falls back to default language if translation doesn't exist.
    """
    if not obj or not field_name:
        return ''

    current_lang = get_language()

    # Try current language
    translated_field = f"{field_name}_{current_lang}"
    value = getattr(obj, translated_field, None)

    # If value is empty or None, try fallback languages
    if not value:
        fallback_langs = ['en', 'uz', 'ru']  # Priority order
        for lang in fallback_langs:
            if lang != current_lang:
                fallback_field = f"{field_name}_{lang}"
                value = getattr(obj, fallback_field, None)
                if value:
                    break

    # Ultimate fallback to base field
    if not value:
        value = getattr(obj, field_name, '')

    return value


@register.simple_tag(takes_context=True)
def get_language_name(context):
    """Get the full name of the current language"""
    from django.conf import settings
    current_lang = get_language()
    for code, name in settings.LANGUAGES:
        if code == current_lang:
            return name
    return current_lang


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    """
    Generate URL for the same page in different language.

    Usage:
        {% translate_url 'en' %}
    """
    request = context.get('request')
    if not request:
        return ''

    path = request.get_full_path()
    # Remove language prefix if exists
    for code, name in context.get('LANGUAGES', []):
        prefix = f'/{code}/'
        if path.startswith(prefix):
            path = path[len(prefix)-1:]
            break

    return f'/{lang_code}{path}'
