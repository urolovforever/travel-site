from django.db import models
from django.utils.translation import gettext_lazy as _


class Sponsor(models.Model):
    """
    Sponsor/Partner model for displaying company logos.
    """
    name = models.CharField(_('Company Name'), max_length=200)
    logo = models.ImageField(_('Logo'), upload_to='sponsors/')
    website_url = models.URLField(_('Website URL'), blank=True, null=True)
    display_order = models.IntegerField(_('Display Order'), default=0, help_text=_('Lower numbers appear first'))
    active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name
