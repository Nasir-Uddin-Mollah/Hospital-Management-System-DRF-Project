from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'problem')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone')
    list_filter = ('problem',)
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
