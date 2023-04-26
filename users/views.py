from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):
    title = "Register"

    if request.user.is_authenticated:
        return redirect("blog:index")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for <b>{username}</b>")
            return redirect("auth:login")

    else:
        form = UserRegisterForm()
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "users/login_register.html", context)


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    next_page = "blog:index"
    template_name = "users/login_register.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["title"] = "Login"
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("blog:index")

        return super().dispatch(request, *args, **kwargs)


@login_required(login_url="auth:login")
def profile(request):
    return render(request, "users/profile.html")
