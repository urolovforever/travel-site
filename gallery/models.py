from django.db import models
from django.utils.translation import gettext_lazy as _


class GalleryImage(models.Model):
    """
    Gallery Image model - standalone gallery for the website.
    """
    image = models.ImageField(_('Image'), upload_to='gallery/')
    uploaded_at = models.DateTimeField(_('Uploaded At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Gallery Image {self.id} - {self.uploaded_at.strftime('%Y-%m-%d')}"
