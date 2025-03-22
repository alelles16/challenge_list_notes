from rest_framework import serializers
from core.models import Note, Category


class NoteSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'categories', 'created_at']
