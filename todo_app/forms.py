from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ToDoItem


class AddItem(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ToDoItem
        fields = [
            "todo_list",
            "title",
            "description",
            "due_date",
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
