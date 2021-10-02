from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import UserForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from accounts.forms import RegisterForm


class RegisterView(generic.CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegisterForm

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        login(request=self.request, user=self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('list_product')


class ProfileView(generic.DetailView):
    model = User
    context_object_name = 'user_obj'
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        if self.request.user == self.object:
            feedbacks = self.object.feedbacks.all()
        else:
            feedbacks = self.object.feedbacks.filter(is_moderated=True)

        return super(ProfileView, self).get_context_data(feedbacks=feedbacks)


class UpdateUser(UserPassesTestMixin, generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class UpdatePassword(UserPassesTestMixin, generic.UpdateView):
    model = User
    form_class = ChangePasswordForm
    template_name = 'user/update.html'

    def test_func(self):
        return self.request.user == self.get_object()

    def form_valid(self, form):
        response = super(UpdatePassword, self).form_valid(form)
        update_session_auth_hash(self.request, self.object)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
