from django.urls import path
from . import views
urlpatterns = [
        path('root/', views.root , name="Root"),
        path('inherit/', views.block, name="Block")
        ]
