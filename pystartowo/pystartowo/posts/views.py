import re
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import environ

env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env()


class PostListView(LoginRequiredMixin):
    pass


def home(request):
    # print(env('SECRET_KEY'))
    # print(env('DEBUG'))
    return render(request, 'homepage.html')