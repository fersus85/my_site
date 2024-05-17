from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(label='Комментарий',
                              widget=forms.TextInput, required=False)
