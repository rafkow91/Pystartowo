from django.urls import path
from django.views.generic import TemplateView

from .views import (
    home,
    post_list_view,
    post_detail_view,
    to_add_form_view,
)

app_name = 'posts'
urlpatterns = [
    path('', TemplateView.as_view(template_name='posts/post_main.html'), name='main'),
    path('<slug:slug>', post_detail_view, name='detail'),
    path('~to_add', to_add_form_view, name='to_add'),
    path('', home, name='add'),
    path('~list', post_list_view, name='list'),
]
