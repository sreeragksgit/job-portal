from django.contrib import admin

# Register your models here.
from employer.models import EmployerProfile,Jobs
admin.site.register(EmployerProfile)
admin.site.register(Jobs)