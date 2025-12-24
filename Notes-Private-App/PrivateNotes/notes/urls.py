from django.urls import path
from . import views
urlpatterns=[
        path('list/', views.ListView.as_view(), name='Note-List'),
        path('create_blog/', views.CreateNote.as_view(), name='Create-Blog'),
        path('read_blog/<int:title_id>', views.ReadNote.as_view(), name='Read-Blog'),
        path('update_blog/<int:title_id>', views.UpdateNote.as_view(), name="Update-Blog"),
        path('delete_blog/<int:title_id>', views.DeleteNote.as_view(), name="Delete-Blog")
        ]
