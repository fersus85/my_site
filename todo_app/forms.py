from django import forms
from .models import ToDoItem
from captcha.fields import CaptchaField


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


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
