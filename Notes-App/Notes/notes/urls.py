from django.urls import path
from . import views
urlpatterns = [
       # path('list/', views.listView, name='ListNotes')
       path('list/', views.TeamNameView.as_view(), name="Superhero"),
       path('detail_view/<int:title_id>', views.DetailedView.as_view(), name="Detail-View"),
       path('create_blog/', views.CreateBlog.as_view(), name="Create-Blog-Page"),
       path('edit_blog/<int:title_id>', views.EditBlog.as_view(), name="Edit-Blog"),
       path('delete_blog/<int:title_id>', views.DeleteBlog.as_view(), name="Delete-Blog")
        ]
