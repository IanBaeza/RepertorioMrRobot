from django.contrib import admin

# Register your models here.
from . models import Gabinete, Fuente, PlacaMadre, Ram, Procesador, TarjetaVideo, Almacenamiento, Computador

admin.site.register(Gabinete)
admin.site.register(Fuente)
admin.site.register(PlacaMadre)
admin.site.register(Ram)
admin.site.register(Procesador)
admin.site.register(TarjetaVideo)
admin.site.register(Almacenamiento)
admin.site.register(Computador)
