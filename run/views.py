from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    )

from .models import Year


class RunYearCreateView(UserPassesTestMixin, CreateView):
    model = Year
    fields = '__all__'
    template_name = 'run/year_create.html'

    def test_func(self):
        return self.request.user.is_staff


class RunListView(ListView):
    model = Year
    template_name = "run/run_home.html"
    context_object_name = 'years'


class RunYearListView(UserPassesTestMixin, ListView):
    model = Year
    template_name = "run/year_list.html"
    context_object_name = 'years'

    def test_func(self):
        return self.request.user.is_staff


class RunDelView(UserPassesTestMixin, DeleteView):
    model = Year
    fields = ('year', 'total',)
    template_name = 'run/delete_year.html'
    success_url = reverse_lazy('run_home')

    def test_func(self):
        return self.request.user.is_staff


class RunUpdateView(UserPassesTestMixin, UpdateView):
    model = Year
    fields = '__all__'
    template_name = 'run/edit_year.html'
    success_url = reverse_lazy('run_home')

    def test_func(self):
        return self.request.user.is_staff
