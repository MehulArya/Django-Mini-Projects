from django.shortcuts import render, get_object_or_404
from notes.models import Note
from django.views import generic, View
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
