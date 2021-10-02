from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.helpers import UserValidationMixin


class RegisterForm(UserValidationMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class UserForm(UserValidationMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
        }


class ChangePasswordForm(UserCreationForm):
    old_password = forms.CharField(strip=False,
                                   widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                                   help_text=password_validation.password_validators_help_text_html(),
                                   )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('old_password',)
        exclude = ('username',)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise ValidationError('Invalid old password!')
        return old_password
