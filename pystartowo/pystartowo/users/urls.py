from django.urls import path

from .views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_counter_view,
    user_list_view,
    user_register_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~count", view=user_counter_view, name="counter"),
    path("", view=user_list_view, name="list"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("register/", view=user_register_view, name="register"),
]
