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
        queryset = Package.objects.filter(published=True, available=True)

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
        return Package.objects.filter(published=True)


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
    data = {
        'id': package.id,
        'title': package.title,
        'slug': package.slug,
        'description': package.description,
        'price': str(package.price),
        'currency': package.currency,
        'duration': package.duration,
        'duration_days': package.duration_days,
        'max_people': package.max_people,
        'inclusions': package.inclusions,
        'exclusions': package.exclusions,
        'main_image': package.main_image.url if package.main_image else None,
        'available': package.available,
        'featured': package.featured,
    }
    return JsonResponse(data)
