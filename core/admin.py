from django.contrib import admin
from . import models

admin.site.site_header = 'HS App Manager'
admin.site.index_title = 'Administration'

@admin.register(models.App)
class AppAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'link', 'logo_url']

    