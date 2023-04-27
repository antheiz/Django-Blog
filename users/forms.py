from django import forms

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import Profile

# User = get_user_model()


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


# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-500 file:text-white hover:file:bg-blue-600"
                }
            )
