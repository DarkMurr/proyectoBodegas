from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'metodo', 'monto', 'estado', 'fecha')
    list_filter = ('metodo', 'estado', 'fecha')
    search_fields = ('referencia',)
    ordering = ('-fecha',)
