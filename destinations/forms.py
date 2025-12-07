from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset
from .models import Destination


class DestinationForm(forms.ModelForm):
    """Form for creating/editing destinations"""

    class Meta:
        model = Destination
        fields = [
            'name', 'title', 'slug',
            'country', 'city', 'region',
            'short_description', 'description', 'things_to_do',
            'best_time_to_visit', 'average_cost',
            'main_image',
            'published', 'featured',
            'meta_title', 'meta_description', 'meta_keywords'
        ]
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 6}),
            'things_to_do': forms.Textarea(attrs={'rows': 5}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Basic Information'),
                Row(
                    Column('name', css_class='form-group col-md-6 mb-3'),
                    Column('title', css_class='form-group col-md-6 mb-3'),
                ),
                'slug',
                Row(
                    Column('country', css_class='form-group col-md-4 mb-3'),
                    Column('city', css_class='form-group col-md-4 mb-3'),
                    Column('region', css_class='form-group col-md-4 mb-3'),
                ),
            ),
            Fieldset(
                _('Description & Content'),
                'short_description',
                'description',
                'things_to_do',
            ),
            Fieldset(
                _('Travel Information'),
                Row(
                    Column('best_time_to_visit', css_class='form-group col-md-6 mb-3'),
                    Column('average_cost', css_class='form-group col-md-6 mb-3'),
                ),
            ),
            Fieldset(
                _('Media'),
                'main_image',
            ),
            Fieldset(
                _('SEO Settings'),
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            Fieldset(
                _('Status'),
                Row(
                    Column('published', css_class='form-group col-md-6 mb-3'),
                    Column('featured', css_class='form-group col-md-6 mb-3'),
                ),
            ),
            Submit('submit', _('Save Destination'), css_class='btn btn-success btn-lg')
        )

        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
