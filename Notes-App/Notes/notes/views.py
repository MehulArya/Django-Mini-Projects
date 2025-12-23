from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from django.views import generic, View
from notes.forms import BasicForm
# Create your views here.

#def listView(request):
#    sh_team = Note.objects.all()
#    ctx = { 'team' : sh_team }
#    return render(request, 'notes/list.html', ctx)

class TeamNameView(generic.ListView):
    model = Note
    template_name = "notes/list.html"
    context_object_name = 'team'

class DetailedView(View):
    def get(self,request,title_id):
       # title_info = Note.objects.get(id=title_id)
        title_object = get_object_or_404(Note, id=title_id)
        ctx = { 'title_info' : title_object }
        return render(request, "notes/detail_view.html", ctx)

class CreateBlog(View):
    def get(self, request):
        forms = BasicForm()
        ctx = { 'form' : forms }
        return render(request, "notes/create_blog.html", ctx)
    def post(self, request):
        forms = BasicForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("Superhero")
        return render(request, "notes/create_blog.html", { 'form' : forms })

class EditBlog(View):
    def get(self, request, title_id):
        note = get_object_or_404(Note, id=title_id)
        form = BasicForm(instance=note)
        ctx = { 'edit_form' : form }
        return render(request, "notes/edit_blog.html", ctx)
    def post(self, request, title_id):
        note = get_object_or_404(Note, id=title_id)
        form = BasicForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect("Superhero")
        return render(request, "notes/edit_blog.html", { "form" : form })

class DeleteBlog(View):
    def get(self, request, title_id):
        note = get_object_or_404(Note, id=title_id)
        ctx = { 'note' : note }
        return render(request, "notes/delete_blog.html", ctx)
    def post(self, request, title_id):
        note = get_object_or_404(Note, id=title_id)
        note.delete()
        return redirect("Superhero")
