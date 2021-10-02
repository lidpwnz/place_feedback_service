from django import forms
from core.helpers import get_widget_attrs
from app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs=get_widget_attrs()),
            'category': forms.Select(attrs=get_widget_attrs(**{'class': 'form-select mb-3'})),
            'description': forms.Textarea(attrs=get_widget_attrs()),
            'image': forms.ClearableFileInput(attrs=get_widget_attrs())
        }
