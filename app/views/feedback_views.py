from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from accounts.helpers import is_moderator
from app.helpers import FeedbackAttrsMixin
from app.models import Product


class CreateFeedback(FeedbackAttrsMixin, LoginRequiredMixin, generic.CreateView):
    template_name = 'products/detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs.get('product_id')
        return super(CreateFeedback, self).form_valid(form)

    def get_context_data(self, **kwargs):
        is_moder = False

        if is_moderator(self.request.user):
            is_moder = True

        return super(CreateFeedback, self).get_context_data(is_moderator=is_moder)

    def get_product(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))

    def form_invalid(self, form):
        is_moder = False
        if is_moderator(self.request.user):
            feedbacks = self.get_product().feedbacks.all()
            is_moder = True
        else:
            feedbacks = self.get_product().feedbacks.filter(is_moderated=True)

        context = {'product': self.get_product(), 'form': form, 'feedbacks': feedbacks, 'is_moderator': is_moder}
        return render(self.request, self.template_name, context)


class UpdateFeedback(FeedbackAttrsMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'feedback/update.html'

    def get_context_data(self, **kwargs):
        is_moder = False

        if is_moderator(self.request.user):
            is_moder = True

        return super().get_context_data(is_moderator=is_moder)

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.has_perm('app.change_feedback')


class DeleteFeedback(FeedbackAttrsMixin, UserPassesTestMixin, generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.has_perm('app.delete_feedback')
