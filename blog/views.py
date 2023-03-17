# blog/views.py
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"

# def post_list(request):
#     posts = Post.published.all()
#     # Pagination with 3 posts per page
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         # If page_number is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page_number is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'post_list.html', {'posts': posts})

# class PostListView(ListView):
#     """Alternative post list view"""
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = "post_list.html"


# def post_detail(request, id, year, month, day, post):#id
#     try:
#         # post = Post.published.get(id=id)
#         # post = get_object_or_404(Post,id=id, status=Post.Status.PUBLISHED)
#         post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED,slug=post,publish__year=year,publish__month=month,publish__day=day)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(request,'blog/post/details.html',{'post': post})