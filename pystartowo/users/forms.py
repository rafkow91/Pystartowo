# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update(
        {
            'duplicate_username': _(
                'This username has already been taken.'
            )
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'discord_login',
            'email',
        ]

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages['duplicate_username']
        )


class UserLoginForm(AuthenticationForm):
    model = User
