from modeltranslation.translator import register, TranslationOptions
from .models import GalleryImage


@register(GalleryImage)
class GalleryImageTranslationOptions(TranslationOptions):
    """
    Configure which fields of GalleryImage should be translatable.
    This will create fields like: caption_en, caption_uz, caption_ru.
    """
    fields = ('caption',)
    required_languages = ()  # No required languages for captions
