from abc import abstractmethod
from typing import Any
from django.urls import reverse_lazy
from django.views import View
from accounts.helpers import is_moderator
from app.forms import ProductForm, FeedbackForm
from app.models import Product, Feedback


class BaseAttrsMixin(View):
    model: Any
    form_class: Any
    context_object_name: str
    template_name: str
    is_moder: bool
    object: None
    permission: str

    def dispatch(self, request, *args, **kwargs):
        self.is_moder = is_moderator(self.request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(is_moderator=self.is_moder, **kwargs)

    @abstractmethod
    def get_success_url(self):
        return NotImplementedError


class ProductAttrsMixin(BaseAttrsMixin):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'products/product.html'

    def get_success_url(self):
        return reverse_lazy('list_product')


class FeedbackAttrsMixin(BaseAttrsMixin):
    model = Feedback
    form_class = FeedbackForm

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.has_perm(self.permission)

    def get_success_url(self):
        return reverse_lazy('detail_product', kwargs={'pk': self.object.product.pk})
