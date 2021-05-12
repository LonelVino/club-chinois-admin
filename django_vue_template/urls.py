"""django_vue_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^$', TemplateView.as_view(template_name='index.html')),
  path('django_api', include('django_api.urls')),
  path('django_api/article', include('django_api.article.urls')),
  path('django_api/user', include('django_api.user.urls')),
  path('django_api/activity', include('django_api.activity.urls')),
]