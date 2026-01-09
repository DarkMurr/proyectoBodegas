from django.contrib import admin
from .models import Empleado, Administrador, Cajero, Auxiliar


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'puesto', 'correo', 'bodega', 'activo')
    list_filter = ('puesto', 'activo', 'bodega')
    search_fields = ('nombre', 'apellido', 'correo')
    ordering = ('nombre',)


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'nivel_acceso')


@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'turno')


@admin.register(Auxiliar)
class AuxiliarAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'area')

