from django.shortcuts import render, get_object_or_404
from django.views import generic
from app.helpers import FeedbackAttrsMixin
from app.models import Product


class CreateFeedback(FeedbackAttrsMixin, generic.CreateView):
    template_name = 'products/detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs.get('product_id')
        return super(CreateFeedback, self).form_valid(form)

    def get_product(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))

    def form_invalid(self, form):
        context = {'product': self.get_product(), 'form': form}
        return render(self.request, self.template_name, context)


class UpdateFeedback(FeedbackAttrsMixin, generic.UpdateView):
    template_name = 'feedback/update.html'


class DeleteFeedback(FeedbackAttrsMixin, generic.DeleteView):
    pass
