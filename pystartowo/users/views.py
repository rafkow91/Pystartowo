from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
    CreateView,
    FormView,
    ListView,
)

from django.views import View
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserCreationForm, UserLoginForm


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        'first_name',
        'last_name',
        'discord_login',
        'bio',
    ]

    model = User
    success_url = '/success/'
    success_message = _('Profile Updated')

    def get_success_url(self):
        return reverse(
            'users:details',
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            'users:detail',
            kwargs={'username': self.request.user.username},
        )


user_redirect_view = UserRedirectView.as_view()


class UserCounterView(View):
    model = User
    template_name = 'users/user_counter.html'

    def get(self, request):
        users_counter = User.objects.count()
        return render(request, self.template_name, {'users_counter': users_counter})


user_counter_view = UserCounterView.as_view()


class UserListView(ListView):
    model = User


user_list_view = UserListView.as_view()


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()

        try:
            user_group = Group.objects.get(name='UsersGroup')
        except:
            Group.objects.create(name='UsersGroup')
            user_group = Group.objects.get(name='UsersGroup')

        instance.groups.add(user_group)

        instance.save()
        form.save_m2m()

        return redirect(reverse('homepage'))


user_register_view = UserRegisterView.as_view()


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'


user_login_view = UserLoginView.as_view()
