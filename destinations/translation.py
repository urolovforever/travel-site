from modeltranslation.translator import register, TranslationOptions
from .models import Destination, DestinationGalleryImage


@register(Destination)
class DestinationTranslationOptions(TranslationOptions):
    """
    Configure which fields of Destination should be translatable.
    This will create fields like: title_en, title_uz, title_ru, etc.
    """
    fields = (
        'name',
        'title',
        'country',
        'city',
        'region',
        'short_description',
        'meta_title',
        'meta_description',
        'meta_keywords',
    )
    required_languages = ('en',)  # English is required, others optional


@register(DestinationGalleryImage)
class DestinationGalleryImageTranslationOptions(TranslationOptions):
    """
    Configure which fields of DestinationGalleryImage should be translatable.
    """
    fields = ('caption',)
    required_languages = ('en',)
