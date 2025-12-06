from django.shortcuts import render
from django.views.generic import TemplateView
from destinations.models import Destination
from packages.models import Package
from gallery.models import GalleryImage


class HomeView(TemplateView):
    """Homepage view showing featured destinations and packages"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_destinations'] = Destination.objects.filter(
            published=True, featured=True
        ).order_by('-created_at')[:3]
        context['featured_packages'] = Package.objects.filter(
            published=True, available=True, featured=True
        ).select_related('destination').order_by('-created_at')[:3]
        context['latest_gallery_images'] = GalleryImage.objects.all().order_by('-uploaded_at')[:5]
        return context


class AboutView(TemplateView):
    """About Us page"""
    template_name = 'about.html'


class ContactView(TemplateView):
    """Contact Us page"""
    template_name = 'contact.html'
