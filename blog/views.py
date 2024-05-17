from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView)

from system.views import tr_handler403
from .models import Post, Comment
from .forms import CommentForm


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'

    def get_queryset(self):
        return Post.objects.all().select_related('author')


class BlogDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = Post.objects.get(slug=self.kwargs['slug'])
        context["comments"] = post.comments.all()
        return context

    def get_success_url(self):
        return reverse("post_detail", kwargs={'slug': self.kwargs['slug']})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            msg = 'Комментарии могут оставлять\
                  только зарегестрированные пользователи'
            return tr_handler403(request, msg=msg)
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.cleaned_data['comment']
            cont_obj = Post.objects.get(slug=self.kwargs['slug'])
            Comment.objects.create(body=comment, author=request.user,
                                   content_object=cont_obj)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BlogCreateView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    slug_url_kwarg = 'slug'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
