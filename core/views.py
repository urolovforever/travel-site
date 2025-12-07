from django.shortcuts import render
from django.views.generic import TemplateView
from sponsors.models import Sponsor


class HomeView(TemplateView):
    """Homepage view showing featured destinations and packages"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sponsors'] = Sponsor.objects.filter(active=True).order_by('display_order')
        return context


class AboutView(TemplateView):
    """About Us page"""
    template_name = 'about.html'


class ContactView(TemplateView):
    """Contact Us page"""
    template_name = 'contact.html'
