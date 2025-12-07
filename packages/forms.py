from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset
from .models import Package


class PackageForm(forms.ModelForm):
    """Form for creating/editing packages"""

    class Meta:
        model = Package
        fields = ['title', 'slug', 'description', 'itinerary',
                  'price', 'currency', 'duration', 'duration_days', 'max_people',
                  'inclusions', 'exclusions', 'main_image',
                  'available', 'published', 'featured',
                  'meta_keywords', 'meta_description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'itinerary': forms.Textarea(attrs={'rows': 6}),
            'inclusions': forms.Textarea(attrs={'rows': 4}),
            'exclusions': forms.Textarea(attrs={'rows': 4}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Basic Information'),
                Row(
                    Column('title', css_class='form-group col-md-8 mb-3'),
                    Column('slug', css_class='form-group col-md-4 mb-3'),
                ),
                'description',
                'itinerary',
                'main_image',
            ),
            Fieldset(
                _('Pricing & Details'),
                Row(
                    Column('price', css_class='form-group col-md-4 mb-3'),
                    Column('currency', css_class='form-group col-md-2 mb-3'),
                    Column('duration', css_class='form-group col-md-3 mb-3'),
                    Column('duration_days', css_class='form-group col-md-3 mb-3'),
                ),
                'max_people',
            ),
            Fieldset(
                _('Inclusions & Exclusions'),
                'inclusions',
                'exclusions',
            ),
            Fieldset(
                _('SEO'),
                'meta_keywords',
                'meta_description',
            ),
            Fieldset(
                _('Status'),
                Row(
                    Column('available', css_class='form-group col-md-4 mb-3'),
                    Column('published', css_class='form-group col-md-4 mb-3'),
                    Column('featured', css_class='form-group col-md-4 mb-3'),
                ),
            ),
            Submit('submit', _('Save Package'), css_class='btn btn-success btn-lg')
        )

        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
