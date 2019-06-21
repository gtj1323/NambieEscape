from django.contrib import admin
from .models import Calendar

# Register your models here.
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'content', 'date', 'term', 'user', 'user_id')
admin.site.register(Calendar, CalendarAdmin)