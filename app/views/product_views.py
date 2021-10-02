from django.views import generic

from app.forms import FeedbackForm
from app.helpers import ProductAttrsMixin


class CreateProduct(ProductAttrsMixin, generic.CreateView):
    pass


class DetailProduct(ProductAttrsMixin, generic.DetailView):
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        return super(DetailProduct, self).get_context_data(form=FeedbackForm())


class ListProduct(ProductAttrsMixin, generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'


class UpdateProduct(ProductAttrsMixin, generic.UpdateView):
    pass


class DeleteProduct(ProductAttrsMixin, generic.DeleteView):
    pass
