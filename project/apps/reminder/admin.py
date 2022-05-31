from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Lembrete

@admin.register(Lembrete)
class Lembretes(ImportExportModelAdmin):
    list_display = ('id', 'title', 'message')
    list_display_links = ['id']
    search_fields = ('id', 'title', 'message')
    list_per_page = 20