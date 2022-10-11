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
from .forms import PostForm, ToAddForm

env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env()


class PostListView(ListView):
    model = Post
    # paginate_by = 2


post_list_view = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
    slug_field = "slug"


post_detail_view = PostDetailView.as_view()
class PostFormView(CreateView):
    model = Post
    template_name = "posts/post_form.html"
    form_class = PostForm


post_form_view = PostFormView.as_view()


class ToAddFormView(CreateView):
    model = ToAdd
    template_name = "posts/post_form.html"
    fields = ['title', 'content', 'from_module', 'email']

to_add_form_view = ToAddFormView.as_view()


def home(request):
    return render(request, "homepage.html")
