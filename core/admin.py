from django.contrib import admin

# Register your models here.
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'data_criacao')
    list_filter = ('titulo', 'usuario',)


admin.site.register(Evento, EventoAdmin)
