from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating booking inquiries"""

    class Meta:
        model = Booking
        fields = ['package', 'full_name', 'email', 'phone', 'country',
                  'number_of_people', 'preferred_date', 'message']
        widgets = {
            'package': forms.HiddenInput(),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'full_name': _('Full Name'),
            'email': _('Email Address'),
            'phone': _('Phone Number'),
            'country': _('Country'),
            'number_of_people': _('Number of People'),
            'preferred_date': _('Preferred Travel Date'),
            'message': _('Message / Special Requests'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'package',
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('country', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('number_of_people', css_class='form-group col-md-6 mb-3'),
                Column('preferred_date', css_class='form-group col-md-6 mb-3'),
            ),
            'message',
            Submit('submit', _('Submit Booking Request'), css_class='btn btn-primary btn-lg')
        )

        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if field_name != 'package':
                field.widget.attrs.update({'class': 'form-control'})
