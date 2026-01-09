from django.contrib import admin
from .models import Ticket, DetalleTicket

class DetalleTicketInline(admin.TabularInline):
    model = DetalleTicket
    extra = 0

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cajero', 'cliente', 'total')
    list_filter = ('fecha', 'cajero')
    search_fields = ('id',)
    inlines = [DetalleTicketInline]
