from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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
from users.models import User


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
    slug_field = 'slug'


post_detail_view = PostDetailView.as_view()


class PostFormView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        try:
            instance.author = User.objects.get(username=self.request.user)
        except:
            instance.author = None

        instance.published = False

        instance.save()
        
        author_groups = [group.name for group in instance.author.groups.all()]
        author_posts = Post.objects.filter(author=instance.author).filter(published=True).count()

        if 'UsersGroup' in author_groups and author_posts > 5:
            user = User.objects.get(username=instance.author)
            try:
                user_group = Group.objects.get(name='WritersGroup')
            except:
                Group.objects.create(name='WritersGroup')
                user_group = Group.objects.get(name='WritersGroup')

            user.groups.add(user_group)
            user.save()
            author_groups = [group.name for group in instance.author.groups.all()]

        if 'WritersGroup' in author_groups:
            instance.published = True
            instance.save()

        instance = form.save()

        return HttpResponseRedirect(reverse('posts:main'))


post_form_view = PostFormView.as_view()


class ToAddFormView(CreateView):
    model = ToAdd
    template_name = 'posts/post_form.html'
    form_class = ToAddForm
    success_url = '/posts/'


to_add_form_view = ToAddFormView.as_view()
