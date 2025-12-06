from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from .models import GalleryImage


class GalleryView(ListView):
    """Public gallery view showing all images"""
    model = GalleryImage
    template_name = 'tour/gallery.html'
    context_object_name = 'images'
    paginate_by = 12  # 12 images per page

    def get_queryset(self):
        queryset = GalleryImage.objects.all().select_related('destination', 'package')

        # Filter by destination if provided
        destination_id = self.request.GET.get('destination')
        if destination_id:
            queryset = queryset.filter(destination_id=destination_id)

        # Filter by package if provided
        package_id = self.request.GET.get('package')
        if package_id:
            queryset = queryset.filter(package_id=package_id)

        return queryset.order_by('order', '-uploaded_at')
