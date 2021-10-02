from django.views import generic
from app.helpers import ProductAttrsMixin


class CreateProduct(ProductAttrsMixin, generic.CreateView):
    pass


class DetailProduct(ProductAttrsMixin, generic.DetailView):
    template_name = 'products/detail.html'


class ListProduct(ProductAttrsMixin, generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'


class UpdateProduct(ProductAttrsMixin, generic.UpdateView):
    pass


class DeleteProduct(ProductAttrsMixin, generic.DeleteView):
    pass
