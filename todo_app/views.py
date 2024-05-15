from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import ToDoList, ToDoItem


class MainListView(ListView):
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
        context['title'] = 'Списки дел'
        return context


class ListCreate(UserPassesTestMixin, CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Новый список дел"
        return context

    def test_func(self):
        return self.request.user.is_staff


class ItemCreate(UserPassesTestMixin, CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        owner = self.request.user.id
        initial_data['owner'] = owner
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Добавить дело"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

    def test_func(self):
        return self.request.user.is_staff


class ItemUpdate(UserPassesTestMixin, UpdateView):
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
        context["title"] = "Изменить дело"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

    def test_func(self):
        return self.request.user.is_staff


class ListDelete(UserPassesTestMixin, DeleteView):
    model = ToDoList
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление списка'
        return context

    def test_func(self):
        return self.request.user.is_staff


class ItemDelete(UserPassesTestMixin, DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context

    def test_func(self):
        return self.request.user.is_staff
