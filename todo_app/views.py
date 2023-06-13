from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView

from config.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from .forms import ContactForm
from .models import ToDoList, ToDoItem
from run.models import Year
# from read.models import
from django.db.models import Sum


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject}', message,
                          from_email, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Error subject')
            return redirect('success')
    else:
        return HttpResponse('invalid request')
    return render(request, "todo_app/feedback.html", {'form': form})


def success_view(request):
    return render(request, "todo_app/success.html",)



class MainPage(ListView):
    model = Year
    template_name = "todo_app/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        total = Year.objects.aggregate(Sum('total'))
        context["total"] = 'Run: ' + str(total['total__sum']) + ' ' + 'km'
        return context


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/main_todo.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(LoginRequiredMixin, CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context


class ItemCreate(LoginRequiredMixin, CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "is_done",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDelete(LoginRequiredMixin, DeleteView):
    model = ToDoList
    success_url = reverse_lazy("index")


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
