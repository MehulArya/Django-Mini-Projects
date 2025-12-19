from django.urls import path
from . import views
urlpatterns = [
        path('guess/', views.process_number, name='process_number'),
        ]
