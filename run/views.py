from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Year, Month
# Create your views here.


class RunListView(ListView):
    model = Month
    template_name = "run/run_home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["years"] = Year.objects.all()
        context["twfif"] = Month.objects.filter(year_id=1)
        context["tf_tot"] = Year.objects.get(id=1)
        context["twsix"] = Month.objects.filter(year_id=2)
        context["ts_tot"] = Year.objects.get(id=2)
        context["twsev"] = Month.objects.filter(year_id=3)
        context["tse_tot"] = Year.objects.get(id=3)
        return context
