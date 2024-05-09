from django.utils import timezone
from django.db import models
from django.urls import reverse


def one_week_hence():
    hence = timezone.now() + timezone.timedelta(days=7)
    return hence


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True,
                             verbose_name='Название')

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания')
    due_date = models.DateTimeField(default=one_week_hence,
                                    verbose_name='Закончить к')
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE,
                                  verbose_name='Список дел')
    is_done = models.BooleanField(default=False, verbose_name='Сделано')

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
