from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.http import JsonResponse
from .models import Package
from .forms import PackageForm


class PackageListView(ListView):
    """Public list view of all available packages"""
    model = Package
    template_name = 'tour/package_list.html'
    context_object_name = 'packages'
    paginate_by = settings.ITEMS_PER_PAGE

    def get_queryset(self):
        queryset = Package.objects.filter(published=True, available=True).prefetch_related('gallery_images')

        # Filter by price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset.order_by('-created_at')


class PackageDetailView(DetailView):
    """Public detail view of a single package"""
    model = Package
    template_name = 'tour/package_detail.html'
    context_object_name = 'package'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Package.objects.filter(published=True).prefetch_related('gallery_images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_images'] = self.object.gallery_images.all()
        return context


# CRUD Views (requires authentication)

class PackageCreateView(LoginRequiredMixin, CreateView):
    """Create a new package (authenticated users only)"""
    model = Package
    form_class = PackageForm
    template_name = 'tour/package_form.html'
    success_url = reverse_lazy('packages:package_list')


class PackageUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing package (authenticated users only)"""
    model = Package
    form_class = PackageForm
    template_name = 'tour/package_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('packages:package_detail', kwargs={'slug': self.object.slug})


class PackageDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a package (authenticated users only)"""
    model = Package
    template_name = 'tour/package_confirm_delete.html'
    success_url = reverse_lazy('packages:package_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# API Endpoints (JSON)

def package_list_json(request):
    """JSON endpoint for packages"""
    packages = Package.objects.filter(published=True, available=True).values(
        'id', 'title', 'slug', 'price', 'currency', 'duration', 'main_image', 'featured'
    )
    return JsonResponse(list(packages), safe=False)


def package_detail_json(request, slug):
    """JSON endpoint for a single package"""
    package = get_object_or_404(Package, slug=slug, published=True)

    # Get gallery images
    gallery_images = [
        {
            'image': img.image.url if img.image else None,
            'caption': img.caption,
            'order': img.order
        }
        for img in package.gallery_images.all()
    ]

    data = {
        'id': package.id,
        'title': package.title,
        'slug': package.slug,
        'description': package.description,
        'price': str(package.price),
        'currency': package.currency,
        'duration': package.duration,
        'max_people': package.max_people,
        'main_image': package.main_image.url if package.main_image else None,
        'gallery_images': gallery_images,
        'available': package.available,
    }
    return JsonResponse(data)
