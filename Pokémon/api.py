#En este archivo crearemos el ViewSet, que junto con los serializers nos permiten crear API's

#importamos el modelo Project
from .models import pokémon_favorito
#importamos viewsets y permissions
from rest_framework import viewsets, permissions
#importamos el modelo del serializer
from .serializers import PokémonSerializers

#creamos el ViewSet del modelo Project, el cuál heredará lo que ponemos dentro del parámetro
class PokémonViewSet (viewsets.ModelViewSet) :
    #ponemos las consultas que se podrán hacer
    
    #hacemos que el conjunto de datos contenga todos los datos de la tabla Project
    queryset = pokémon_favorito.objects.all()
    #ponemos en una lista quienes tendrán permisos (en este caso AllowAny significa que todos tendrán permiso)
    permission_classes = [permissions.AllowAny]
    #ponemos desde qué serializer convertirá los datos
    serializer_class = PokémonSerializers
