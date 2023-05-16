from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'


class BlogDetailView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
