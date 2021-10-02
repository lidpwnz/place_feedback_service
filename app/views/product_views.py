from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from app.forms import FeedbackForm
from app.helpers import ProductAttrsMixin


class CreateProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'app.add_product'


class DetailProduct(ProductAttrsMixin, generic.DetailView):
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        return super(DetailProduct, self).get_context_data(form=FeedbackForm())


class ListProduct(ProductAttrsMixin, generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'


class UpdateProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'app.change_product'


class DeleteProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'app.delete_product'
