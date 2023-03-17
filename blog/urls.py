# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView #, post_list, post_detail, PostListView

# app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("post/<slug>/", BlogDetailView.as_view(), name="post_detail"), # new
    # path("post/<slug>/", BlogDetailView.as_view(), name="post_detail"), # new
    # path("post/list/",post_list, name="post_list"),
    # path('post/id:<int:id>/', post_detail, name="details"),
    # path("<slug:post>/<int:year>/<int:month>/<int:day>/", post_detail, name="details"),
    # path('posts', PostListView.as_view(), name='post_list'),

]
