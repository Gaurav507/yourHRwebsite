from django.contrib import admin
from .models import jobProvider, jobSeeker, jobDesc
# Register your models here.

admin.site.register(jobProvider)
admin.site.register(jobSeeker)
admin.site.register(jobDesc)
