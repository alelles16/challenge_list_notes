from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Note
from notes.serializers import NoteSerializer


class ListNotes(APIView):

    def get(self, request):
        notes = Note.objects.all().order_by('-created_at').prefetch_related('categories')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
