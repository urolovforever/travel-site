from modeltranslation.translator import register, TranslationOptions
from .models import Package


@register(Package)
class PackageTranslationOptions(TranslationOptions):
    """
    Configure which fields of Package should be translatable.
    This will create fields like: title_en, title_uz, title_ru, etc.
    """
    fields = (
        'title',
        'description',
        'duration',
        'meta_keywords',
        'meta_description'
    )
    required_languages = ('en',)  # English is required, others optional
