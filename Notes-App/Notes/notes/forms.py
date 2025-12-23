from django import forms
from notes.models import Note
class BasicForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

