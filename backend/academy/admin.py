from django.contrib import admin

from academy import models


admin.site.register(models.Academy)
admin.site.register(models.StudentInAcademy)
admin.site.register(models.Review)

