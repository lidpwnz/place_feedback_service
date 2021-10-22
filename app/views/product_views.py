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
        all_feedbacks = self.object.feedbacks.all()
        feedbacks = all_feedbacks if is_moderator(self.request.user) else all_feedbacks.filter(is_moderated=True)
        form = FeedbackForm()

        if 'invalid_form_data' in self.request.session:
            data = self.request.session.pop('invalid_form_data')
            form = FeedbackForm(data=data)

        return super().get_context_data(form=form, feedbacks=feedbacks)


class ListProduct(ProductAttrsMixin, generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'


class UpdateProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'app.change_product'


class DeleteProduct(ProductAttrsMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'app.delete_product'
