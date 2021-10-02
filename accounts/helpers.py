from django import forms
from django.core.exceptions import ValidationError


class UserValidationMixin(forms.ModelForm):
    email = forms.EmailField(required=True)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise ValidationError('First name or last name required!')

        return self.cleaned_data
