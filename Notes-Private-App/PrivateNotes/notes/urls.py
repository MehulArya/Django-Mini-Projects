from django.urls import path
from . import views
urlpatterns=[
        path('list/', views.ListView.as_view(), name='Note-List'),
        path('create_blog/', views.CreateNote.as_view(), name='Create-Blog'),
        path('read_blog/<int:title_id>', views.ReadNote.as_view(), name='Read-Blog'),
        ]
