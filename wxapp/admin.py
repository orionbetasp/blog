from django.contrib import admin
from .models import wxapp

class WxappAdmin(admin.ModelAdmin):
    list_display = ['name', 'data']

admin.site.register(wxapp, WxappAdmin)