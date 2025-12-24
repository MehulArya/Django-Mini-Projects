from django.shortcuts import render
from django.views import generic
from notes.models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListView(LoginRequiredMixin ,generic.ListView):
    model = Note
    template_name = "notes/list.html"
    context_object_name = "note_object"
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
