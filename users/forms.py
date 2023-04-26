from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"

        for _, field in self.fields.items():
            field.help_text = None
            # field.widget.attrs.update({"placeholder": field.label})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email / Username",
        widget=forms.TextInput(
            attrs={"autofocus": "true", "placeholder": "Username or Email"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
