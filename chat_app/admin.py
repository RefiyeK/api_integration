from django.contrib import admin
from .models import Chat 

# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)