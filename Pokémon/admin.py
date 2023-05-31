from django.contrib import admin
#importamos los modelos que queremos agregar al panel de administrador
from .models import pokémon_favorito

#agregamos los modelos o clases que creamos al panel de administrador
admin.site.register(pokémon_favorito)





