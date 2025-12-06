from django.db import models
from django.utils.translation import gettext_lazy as _
from destinations.models import Destination
from packages.models import Package


class GalleryImage(models.Model):
    """
    Gallery Image model with multilingual caption support.
    Can be associated with either a Destination or Package (or standalone).
    """
    # Image
    image = models.ImageField(_('Image'), upload_to='gallery/')

    # Caption (will be translated by modeltranslation)
    caption = models.CharField(_('Caption'), max_length=500, blank=True)

    # Optional relationships
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('Destination')
    )
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('Package')
    )

    # Display order
    order = models.PositiveIntegerField(_('Order'), default=0)

    # Metadata
    uploaded_at = models.DateTimeField(_('Uploaded At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')
        ordering = ['order', '-uploaded_at']
        indexes = [
            models.Index(fields=['destination', 'order']),
            models.Index(fields=['package', 'order']),
        ]

    def __str__(self):
        if self.caption:
            return self.caption
        elif self.destination:
            return f"Image for {self.destination}"
        elif self.package:
            return f"Image for {self.package}"
        return f"Gallery Image {self.id}"
