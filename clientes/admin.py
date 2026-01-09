from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'es_asociado', 'activo', 'fecha_registro')
    list_filter = ('es_asociado', 'activo')
    search_fields = ('nombre', 'correo', 'telefono')

