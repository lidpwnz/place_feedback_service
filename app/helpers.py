from django.urls import reverse_lazy
from app.forms import ProductForm, FeedbackForm
from app.models import Product, Feedback


class ProductAttrsMixin:
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'products/product.html'

    def get_success_url(self):
        return reverse_lazy('list_product')


class FeedbackAttrsMixin:
    model = Feedback
    form_class = FeedbackForm
    object = None

    def get_success_url(self):
        return reverse_lazy('detail_product', kwargs={'pk': self.object.product.pk})
