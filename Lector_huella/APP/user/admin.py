from django.contrib import admin
from APP.user.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'email')
    search_fields = ('email',)