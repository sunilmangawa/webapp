# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
# from django.views.generic.base import TemplateView # new

urlpatterns = [
path("admin/", admin.site.urls),
path("accounts/", include("accounts.urls")), # new
path("accounts/", include("django.contrib.auth.urls")), # new
# path("", TemplateView.as_view(template_name="home.html"), name="home"), # new
path("", include("pages.urls")), # new
path("blog/", include("blog.urls")), # new , namespace='blog'
path('milldata/', include('milldata.urls')),#new
]
