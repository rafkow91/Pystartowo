"""pystartowo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from users.views import user_register_view
from core.settings import ADMIN_SITE
# fmt: off
# (Skip Black formatting in this section)
urlpatterns = [
    # NOTE: change the URL for Admin, for added security.
    # See #2 here: https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure
    path('tinymce/', include('tinymce.urls')),
    path(ADMIN_SITE, admin.site.urls),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('tags/', include('tags.urls')),
    path('register/', user_register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
# fmt: on

if settings.DEBUG:
    # Serve media files in development server.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
