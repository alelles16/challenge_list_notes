from django.urls import path
from notes.views import (ListNotes, note_view)

urlpatterns = [
    path('api/', ListNotes.as_view(), name='list'),
    path('', note_view)
]
