from django.contrib import admin

# Register your models here.

from APP.Enfermera.models import enfermera


@admin.register(enfermera)
class enfermeraAdmin(admin.ModelAdmin):
    list_display = ('datos', 'Professional_card', 'Specialization',)