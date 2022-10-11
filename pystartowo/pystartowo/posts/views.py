from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import environ
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
    CreateView,
    FormView,
    ListView,
)
from .models import Post, ToAdd

env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env()


class PostListView(ListView):
    model = Post


post_list_view = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
    slug_field = "slug"

class PostToAdd(FormView):
    model = ToAdd


post_detail_view = PostDetailView.as_view()


def home(request):
    return render(request, "homepage.html")
