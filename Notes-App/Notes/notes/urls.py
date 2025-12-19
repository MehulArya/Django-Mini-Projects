from django.urls import path
from . import views
urlpatterns = [
       # path('list/', views.listView, name='ListNotes')
       path('list/', views.TeamNameView.as_view(), name="Superhero"),
       path('detail_view/<int:title_id>', views.DetailedView.as_view(), name="Detail-View")
        ]
