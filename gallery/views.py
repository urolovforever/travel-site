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
        queryset = GalleryImage.objects.all()
        return queryset.order_by('-uploaded_at')
