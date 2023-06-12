from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    queryset = Post.objects.all().order_by('-date')

    def get_queryset(self):
        return Post.objects.all().select_related('author')


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
