from django.contrib import admin
from core.models import Note, Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title",)


admin.site.register(Note, NoteAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)
