from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_patient', 'get_doctor', 'appointment_type',
                    'appointment_status', 'symptom', 'time', 'cancel')

    def get_patient(self, obj):
        return obj.patient.user.first_name
    get_patient.short_description = 'Patient'

    def get_doctor(self, obj):
        return obj.doctor.user.first_name
    get_doctor.short_description = 'Doctor'

    list_filter = ('doctor', 'appointment_status')
    search_fields = ('patient__user__first_name',
                     'doctor__user__first_name', 'time')
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_type == 'Online':
            email_subject = "Your appointment is running"
            email_body = render_to_string(
                'admin_email.html', {'user': obj.patient.user, 'doctor': obj.doctor})
            email = EmailMultiAlternatives(
                email_subject,
                '',
                to=[obj.patient.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


admin.site.register(Appointment, AppointmentAdmin)
