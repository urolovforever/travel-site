from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Template tag to replace or add query parameters while keeping existing ones.
    Excludes 'page' parameter from existing query string to avoid duplication.

    Usage: {% url_replace page=1 %}
    """
    query = context['request'].GET.copy()

    # Remove 'page' parameter from existing query to avoid duplication
    if 'page' in query:
        query.pop('page')

    # Update with new parameters
    query.update(kwargs)

    return '?' + urlencode(query)
