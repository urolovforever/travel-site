from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking
from .forms import BookingForm
from packages.models import Package


class BookingCreateView(CreateView):
    """Public view to create a booking/inquiry"""
    model = Booking
    form_class = BookingForm
    template_name = 'tour/booking_form.html'
    success_url = reverse_lazy('core:home')

    def get_initial(self):
        """Pre-populate package if provided in URL"""
        initial = super().get_initial()
        package_slug = self.kwargs.get('package_slug')
        if package_slug:
            package = get_object_or_404(Package, slug=package_slug)
            initial['package'] = package
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package_slug = self.kwargs.get('package_slug')
        if package_slug:
            context['package'] = get_object_or_404(Package, slug=package_slug)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        booking = self.object

        # Send confirmation email (will print to console in development)
        subject = _('Booking Inquiry Received - {}'.format(booking.package.title))
        message = _('''
        Thank you for your booking inquiry!

        Package: {}
        Number of People: {}
        Preferred Date: {}

        We will contact you shortly at {} to confirm your booking.

        Best regards,
        Travel Team
        ''').format(
            booking.package.title,
            booking.number_of_people,
            booking.preferred_date,
            booking.email
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
            [booking.email],
            fail_silently=True,
        )

        messages.success(
            self.request,
            _('Your booking inquiry has been submitted successfully! We will contact you soon.')
        )
        return response


class BookingListView(LoginRequiredMixin, ListView):
    """Admin view to list all bookings (requires authentication)"""
    model = Booking
    template_name = 'tour/booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 20

    def get_queryset(self):
        queryset = Booking.objects.all().select_related('package', 'package__destination')

        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-created_at')
