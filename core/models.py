from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Note(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    categories = models.ManyToManyField('Category', related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
