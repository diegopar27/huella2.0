from django.contrib import admin

from APP.Medico.models import medico


@admin.register(medico)
class medicoAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'Phone','gender','Specialization', 'Direction',)
    list_editable = ('Phone','gender','Specialization',)
    search_fields = ('Name', 'Cc',)