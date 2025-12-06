from django.db import models
from django.utils.translation import gettext_lazy as _
from packages.models import Package


class Booking(models.Model):
    """
    Booking/Inquiry model to store customer booking requests.
    """
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('confirmed', _('Confirmed')),
        ('cancelled', _('Cancelled')),
        ('completed', _('Completed')),
    ]

    # Package reference
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name=_('Package')
    )

    # Customer information
    full_name = models.CharField(_('Full Name'), max_length=200)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=20)
    country = models.CharField(_('Country'), max_length=100, blank=True)

    # Booking details
    number_of_people = models.PositiveIntegerField(_('Number of People'), default=1)
    preferred_date = models.DateField(_('Preferred Travel Date'))
    message = models.TextField(_('Message/Special Requests'), blank=True)

    # Status & Metadata
    status = models.CharField(_('Status'), max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(_('Total Price'), max_digits=10, decimal_places=2, blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    # Admin notes
    admin_notes = models.TextField(_('Admin Notes'), blank=True)

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.full_name} - {self.package.title} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        # Calculate total price if not set
        if not self.total_price and self.package:
            self.total_price = self.package.price * self.number_of_people
        super().save(*args, **kwargs)
