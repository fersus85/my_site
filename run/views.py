from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Year, Month


# Create your views here.


class RunMontCreateView(LoginRequiredMixin, CreateView):
    model = Month
    fields = ('title', 'total', 'year')
    template_name = 'run/month_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RunYearCreateView(LoginRequiredMixin, CreateView):
    model = Year
    fields = ('title', 'total',)
    template_name = 'run/year_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RunListView(LoginRequiredMixin, ListView):
    model = Year
    template_name = "run/run_home.html"
    context_object_name = 'years'

    def get_queryset(self):
        cur_user = self.request.user
        return Year.objects.filter(owner=cur_user.id)

    def get_context_data(self):
        context = super().get_context_data()
        monthlies = [
            'Total',
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December',

        ]
        context["monthlies"] = monthlies
        return context


class RunDetailView(DetailView):
    model = Year
    template_name = "run/run_year_detail.html"


class RunYearListView(LoginRequiredMixin, ListView):
    model = Year
    template_name = "run/year_list.html"
    context_object_name = 'years'

    def get_queryset(self):
        cur_user = self.request.user
        return Year.objects.filter(owner=cur_user.id)


class RunYearDeleteView(UserPassesTestMixin, DeleteView):
    model = Year
    fields = ('title', 'total', 'year')
    template_name = 'run/delete_year.html'
    success_url = reverse_lazy('run_home')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class RunYearUpdateView(UserPassesTestMixin, UpdateView):
    model = Year
    fields = ('title', 'total',)
    template_name = 'run/edit_year.html'
    success_url = reverse_lazy('run_home')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class RunMonthListView(LoginRequiredMixin, ListView):
    model = Month
    template_name = "run/month_list.html"
    context_object_name = 'monthlies'

    def get_queryset(self):
        cur_user = self.request.user
        return Month.objects.filter(owner=cur_user.id)


class RunMonthUpdateView(UserPassesTestMixin, UpdateView):
    model = Month
    fields = ('title', 'total', 'year')
    template_name = 'run/edit_month.html'
    success_url = reverse_lazy('run_home')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
