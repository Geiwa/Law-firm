from django.contrib import admin
from .models import Contact



class ContactModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'name']
    list_display = ['name']

admin.site.register(Contact, ContactModelAdmin)

