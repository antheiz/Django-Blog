from django.shortcuts import render
from blog.models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# posts = [
#     {
#         "author": "Patrick",
#         "title": "First Blog",
#         "content": "This is first post on this blog!",
#         "category": "education",
#         "date_posted": "07 April 2023",
#     },
#     {
#         "author": "Spongebob",
#         "title": "Second Blog",
#         "content": "This is second post on this blog!",
#         "category": "technology",
#         "date_posted": "08 April 2023",
#     },
#     {
#         "author": "Patrick",
#         "title": "Third Blog",
#         "content": "This is third post on this blog!",
#         "category": "music",
#         "date_posted": "09 April 2023",
#     },
# ]


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["posts"] = Post.objects.all()[:4]
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "auth:login"
    model = Post
    fields = ["title", "content", "category"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = "auth:login"
    model = Post
    fields = ["title", "content", "category"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html")
