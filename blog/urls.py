from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
]
