from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from .models import Destination, DestinationGalleryImage
from .forms import DestinationForm


class DestinationListView(ListView):
    """Public list view of all published destinations"""
    model = Destination
    template_name = 'tour/destination_list.html'
    context_object_name = 'destinations'
    paginate_by = settings.ITEMS_PER_PAGE

    def get_queryset(self):
        return Destination.objects.filter(published=True).prefetch_related('gallery_images').order_by('-created_at')


class DestinationDetailView(DetailView):
    """Public detail view of a single destination"""
    model = Destination
    template_name = 'tour/destination_detail.html'
    context_object_name = 'destination'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Destination.objects.filter(published=True).prefetch_related('gallery_images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_images'] = self.object.gallery_images.all()
        return context


# CRUD Views (requires authentication)

class DestinationCreateView(LoginRequiredMixin, CreateView):
    """Create a new destination (authenticated users only)"""
    model = Destination
    form_class = DestinationForm
    template_name = 'tour/destination_form.html'
    success_url = reverse_lazy('destinations:destination_list')


class DestinationUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing destination (authenticated users only)"""
    model = Destination
    form_class = DestinationForm
    template_name = 'tour/destination_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('destinations:destination_detail', kwargs={'slug': self.object.slug})


class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a destination (authenticated users only)"""
    model = Destination
    template_name = 'tour/destination_confirm_delete.html'
    success_url = reverse_lazy('destinations:destination_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# API Endpoints (JSON)

def destination_list_json(request):
    """JSON endpoint for destinations"""
    destinations = Destination.objects.filter(published=True).values(
        'id', 'name', 'title', 'slug', 'country', 'city', 'region',
        'short_description', 'main_image', 'featured'
    )
    return JsonResponse(list(destinations), safe=False)


def destination_detail_json(request, slug):
    """JSON endpoint for a single destination"""
    destination = get_object_or_404(Destination, slug=slug, published=True)

    # Get gallery images
    gallery_images = [
        {
            'image': img.image.url if img.image else None,
            'caption': img.caption,
            'order': img.order
        }
        for img in destination.gallery_images.all()
    ]

    data = {
        'id': destination.id,
        'name': destination.name,
        'title': destination.title,
        'slug': destination.slug,
        'country': destination.country,
        'city': destination.city,
        'region': destination.region,
        'short_description': destination.short_description,
        'main_image': destination.main_image.url if destination.main_image else None,
        'gallery_images': gallery_images,
        'published': destination.published,
        'featured': destination.featured,
        'created_at': destination.created_at,
        'meta_title': destination.meta_title,
        'meta_description': destination.meta_description,
        'meta_keywords': destination.meta_keywords,
    }
    return JsonResponse(data)
