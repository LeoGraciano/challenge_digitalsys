from typing import Any
from django import forms
from django.contrib.auth import forms as form_auth
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.forms import ValidationError
from django.utils.translation import gettext, gettext_lazy as _


User = get_user_model()


class CustomUserCreationForm(form_auth.UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta(form_auth.UserCreationForm.Meta):
        model = User
        fields = ['email', 'name', 'password1', 'password2']


class UserChangeForm(form_auth.UserChangeForm):

    class Meta(form_auth.UserChangeForm.Meta):
        model = User
        fields = '__all__'


class UserCreationForm(CustomUserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
