from django.urls import reverse_lazy
from app.forms import ProductForm
from app.models import Product


class ProductAttrsMixin:
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'products/product.html'

    def get_success_url(self):
        return reverse_lazy('list_product')
