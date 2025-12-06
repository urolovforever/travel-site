from modeltranslation.translator import register, TranslationOptions
from .models import Destination


@register(Destination)
class DestinationTranslationOptions(TranslationOptions):
    """
    Configure which fields of Destination should be translatable.
    This will create fields like: title_en, title_uz, title_ru, etc.
    """
    fields = ('country', 'title', 'short_description', 'description', 'meta_keywords', 'meta_description')
    required_languages = ('en',)  # English is required, others optional
