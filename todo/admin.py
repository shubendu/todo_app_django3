from django.contrib import admin
from .models import Todo

# we are doing this only to read that created model field in admin
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo,TodoAdmin)