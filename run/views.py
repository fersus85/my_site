from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Year, Month


# Create your views here.


class RunMontCreateView(LoginRequiredMixin, CreateView):
    model = Month
    fields = ('title', 'total', 'year')
    template_name = 'run/month_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RunYearCreateView(LoginRequiredMixin, CreateView):
    model = Year
    fields = ('title', 'total',)
    template_name = 'run/year_create.html'

    # success_url = 'run_home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RunListView(LoginRequiredMixin, ListView):
    model = Year
    template_name = "run/run_home.html"
    context_object_name = 'years'

    def get_queryset(self):
        cur_user = self.request.user
        return Year.objects.filter(owner=cur_user.id)

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.author == self.request.user

    def get_context_data(self):
        context = super().get_context_data()
        monthlies = [
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
            'Total',
        ]
        context["monthlies"] = monthlies
        return context
