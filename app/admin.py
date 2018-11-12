from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Ligne_Creesp_Lib

@admin.register(Ligne_Creesp_Lib)
class PersonAdmin(ImportExportModelAdmin):
    pass
