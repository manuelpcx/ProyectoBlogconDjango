from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'create_at')
    list_filter = ('visible',)

# Register your models here.
admin.site.register(Page, PageAdmin)

title = 'Proyecto Blog'
subtitle = 'Panel de gestion'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
