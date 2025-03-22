from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Note
from notes.forms import NoteForm
from notes.serializers import NoteSerializer


def note_view(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            form.cleaned_data = {}
            return render(request, 'notes/note_list.html', {'form': form})
    form = NoteForm()
    form.cleaned_data = {}
    return render(request, 'notes/note_list.html', {'form': form})

class ListNotes(APIView):

    def get(self, request):
        notes = Note.objects.all().order_by('-created_at').prefetch_related('categories')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
