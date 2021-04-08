from django.contrib import admin
from .models import Article, Category


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Categories"
