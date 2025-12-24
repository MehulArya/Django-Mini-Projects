from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View      
from notes.models import Note
from notes.forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListView(LoginRequiredMixin, generic.ListView):
    model = Note
    template_name = "notes/list.html"
    context_object_name = "note_object"
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class ReadNote(LoginRequiredMixin, View):
    def get(self, request, title_id):
        read_object = get_object_or_404(Note, id=title_id, owner=request.user)
        ctx = {'read_object' : read_object}
        return render(request, "notes/read.html", ctx)

class CreateNote(LoginRequiredMixin, View):
    def get(self, request):
        form = NoteForm()
        ctx = { 'form' : form }
        return render(request, "notes/create_blog.html", ctx)
    def post(self, request):
        form = NoteForm(request.POST)

        if form.is_valid:
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("Note-List")
        return render(request, "notes/create_blog.html", ctx)

class UpdateNote(LoginRequiredMixin, View):
    def get(self, request, title_id):
        note = get_object_or_404(Note, id=title_id, owner=request.user)
        form = NoteForm(instance=note)
        ctx = { 'form' : form,'note_object' : note }
        return render(request, "notes/update.html", ctx)
    def post(self, request, title_id):
        note = get_object_or_404(Note, id=title_id, owner=request.user) #IDOR Vulnerability (Insecure Direct Object Reference)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("Note-List")
        return render(request, "notes/update.html")

class DeleteNote(LoginRequiredMixin, View):
    def get(self, request, title_id):
        note = get_object_or_404(Note, id=title_id, owner=request.user)
        ctx = { "note_object" : note }
        return render(request, "notes/delete.html", ctx)
    def post(self, request, title_id):
        note = get_object_or_404(Note, id=title_id, owner=request.user)
        note.delete()
        return redirect("Note-List")
