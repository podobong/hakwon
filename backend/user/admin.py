from django.contrib import admin

from user import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date_joined')
    list_display_links = ('phone', )

admin.site.register(models.Student)
admin.site.register(models.Parent)
admin.site.register(models.Teacher)

