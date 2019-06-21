from django.contrib import admin
from .models import Category, Keyword, News, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
admin.site.register(Category, CategoryAdmin)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category',]
admin.site.register(Keyword, KeywordAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'URL', 'keyword', 'date',]
admin.site.register(News, NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'user', 'keyword',]
admin.site.register(Comment, CommentAdmin)