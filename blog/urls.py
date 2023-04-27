from django.urls import path
from blog import views
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="about"),
]
