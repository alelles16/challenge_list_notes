from django import forms
from core.models import Note, Category

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'content', 'categories')
