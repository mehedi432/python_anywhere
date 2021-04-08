from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=610)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=13)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
