from django.contrib import admin
from .models import Computer


class ComputerAdmin(admin.ModelAdmin):
    search_fields = ["name", "mac_address", "ip_address", "employee_abbrev"]
    list_display = ["employee_abbrev", "name", "mac_address", "ip_address", "updated_at"]


admin.site.register(Computer, ComputerAdmin)
