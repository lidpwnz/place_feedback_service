from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from app.helpers import FeedbackAttrsMixin
from app.models import Product


class CreateFeedback(FeedbackAttrsMixin, LoginRequiredMixin, generic.CreateView):
    template_name = 'products/detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs.get('product_id')
        return super(CreateFeedback, self).form_valid(form)

    def get_product(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))

    def form_invalid(self, form):
        self.request.session['invalid_form_data'] = self.request.POST
        return redirect(self.request.META['HTTP_REFERER'])


class UpdateFeedback(FeedbackAttrsMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'feedback/update.html'
    permission = 'app.change_feedback'


class DeleteFeedback(FeedbackAttrsMixin, UserPassesTestMixin, generic.DeleteView):
    permission = 'app.delete_feedback'
