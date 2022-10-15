from django.contrib import admin

# Register your models here.
from APP.Persona.models import persona


@admin.register(persona)
class personaAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'Phone','gender', 'Direction',)
    list_editable = ('Phone','gender',)
    search_fields = ('Name', 'Cc',)
