from django.contrib import admin
from .models import Patient
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'mobile_no', 'image')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    search_fields = ('user__first_name', 'user__last_name', 'mobile_no')
    list_filter = ('user__is_active',)
    list_per_page = 10


admin.site.register(Patient, PatientAdmin)
