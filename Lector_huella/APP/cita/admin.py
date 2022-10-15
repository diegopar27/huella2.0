from django.contrib import admin
from APP.cita.models import Cita
# Register your models here.


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('doctors', 'patient', 'date_and_time',)
    list_editable = ('date_and_time',)
    search_fields = ('patient',)