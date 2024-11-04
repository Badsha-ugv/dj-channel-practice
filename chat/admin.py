from django.contrib import admin

# Register your models here.
from .models import Message, Group

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'group')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')