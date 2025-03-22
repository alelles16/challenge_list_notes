from django import forms
from core.models import Note, Category

class NoteForm(forms.ModelForm):

    categories = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Categories separated by comma'}),
    )

    class Meta:
        model = Note
        fields = ['title', 'content', 'categories']

    def clean_categories(self):
        categories_str = self.cleaned_data.get('categories', '')
        category_names = [name.strip() for name in categories_str.split(',') if name.strip()]

        categories = [Category.objects.get_or_create(name=name)[0] for name in category_names]
        return categories

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        self.cleaned_data['categories'] and instance.categories.set(self.cleaned_data['categories'])
        return instance
