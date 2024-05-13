from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from read.models import Book, Year


class HomeListView(ListView):
    model = Year
    template_name = "read/read_home.html"
    context_object_name = 'years'


class YearListView(ListView):
    model = Book
    template_name = "read/read_year.html"
    context_object_name = 'books'

    def get_queryset(self):
        books_by_year = Book.objects.filter(year_id=self.kwargs["year_id"])
        return books_by_year.select_related('year')

    def get_context_data(self):
        context = super().get_context_data()
        context["year"] = Year.objects.get(id=self.kwargs["year_id"])
        return context


class YearCreateView(UserPassesTestMixin, CreateView):
    model = Year
    fields = ('title',)
    template_name = "read/read_create.html"

    def test_func(self):
        return self.request.user.is_staff


class BookCreateView(UserPassesTestMixin, CreateView):
    model = Book
    fields = '__all__'
    template_name = "read/book_create.html"

    def test_func(self):
        return self.request.user.is_staff


class BookDeleteView(UserPassesTestMixin, DeleteView):
    model = Book
    fields = '__all__'
    template_name = 'read/delete_book.html'
    success_url = reverse_lazy('read_app:year_list')

    def test_func(self):
        return self.request.user.is_staff


class BookUpdView(UserPassesTestMixin, UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'read/upd_book.html'
    success_url = reverse_lazy('read_app:year_list')
    context_object_name = 'book'

    def test_func(self):
        return self.request.user.is_staff


class YearEditListView(ListView):
    model = Year
    fields = '__all__'
    template_name = 'read/year_list.html'
    context_object_name = 'years'


class YearDeleteView(UserPassesTestMixin, DeleteView):
    model = Year
    fields = '__all__'
    template_name = 'read/delete_year.html'
    success_url = reverse_lazy('read_app:read_home')

    def test_func(self):
        return self.request.user.is_staff


class YearEditView(UserPassesTestMixin, ListView):
    model = Book
    fields = '__all__'
    template_name = 'read/edit_year.html'
    success_url = reverse_lazy('read_app:read_home')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self):
        context = super().get_context_data()
        context['year'] = Year.objects.get(id=self.kwargs['pk'])
        context["books"] = Book.objects.filter(year_id=self.kwargs["pk"])
        return context
