from django.contrib import admin
from .models import Company, Device, Milldata
# Register your models here.
admin.site.register(Company)
admin.site.register(Device)
admin.site.register(Milldata)
