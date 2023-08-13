from django.contrib import admin
from .models import EnergyOutlook
from import_export.admin import ImportExportModelAdmin
from django.utils import timezone
import datetime



@admin.register(EnergyOutlook)
class EnergyOutlookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title', 'published', 'sector', 'country')
    list_filter = ('sector', 'country')
    search_fields = ('title', 'sector', 'country')

    