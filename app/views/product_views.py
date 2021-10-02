from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

from accounts.helpers import is_moderator
from app.forms import FeedbackForm
from app.helpers import ProductAttrsMixin


class CreateProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'app.add_product'


class DetailProduct(ProductAttrsMixin, generic.DetailView):
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        is_moder = False
        if is_moderator(self.request.user):
            feedbacks = self.object.feedbacks.all()
            is_moder = True
        else:
            feedbacks = self.object.feedbacks.filter(is_moderated=True)

        return super(DetailProduct, self).get_context_data(form=FeedbackForm(),
                                                           feedbacks=feedbacks, is_moderator=is_moder)


class ListProduct(ProductAttrsMixin, generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'


class UpdateProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'app.change_product'


class DeleteProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'app.delete_product'
