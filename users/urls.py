from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views


app_name = "users"
urlpatterns = [
    path("profile/", user_views.profile, name="profile"),
    path("register/", user_views.register_user, name="register"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="blog:index"), name="logout"
    ),
]
