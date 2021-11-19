from django.contrib import admin

# Register your models here.
from library_api.models import User, Zone, Tour


class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "name", "last_name", "email", "birthday", "genre", "type")


class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
                    "descripcion", "pais", "zonaSalida", "zonaLlegada")


admin.site.register(User, UserAdmin)
admin.site.register(Zone)
admin.site.register(Tour, TourAdmin)
