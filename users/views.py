from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(ListView):
    #permission_required = 'users.view_user'
    model = User
