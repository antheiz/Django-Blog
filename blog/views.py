from django.shortcuts import render
from blog.models import Post

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


def about(request):
    return render(request, "blog/about.html")
