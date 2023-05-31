#en este archivo crearemos los serializers, los cuales junto con el ViewSet creado en api.py nos permitirán crear API's

#importamos el módulo serializers
from rest_framework import serializers
#importamos el modelo Project
from .models import pokémon_favorito

#DESDE ESTE ARCHIVO, DJANGO SABRÁ QUE RESPONDER CUANDO SE HAGA UNA PETICIÓN POST, GET, Put y Delete

#creamos la clase que nos permita convertir el modelo en datos que puedan ser consultados
class PokémonSerializers(serializers.ModelSerializer) :
    class Meta :
        #en model ponemos el nombre de la app
        model = pokémon_favorito
        #ahora ponemos los campos que serán consultados dentro de una tupla. Los mismos serán los que tenemos dentro de la clase Pokémon_favorito en el archivo models.py. También podemos verlos en las migraciones de la app Pokémon
        fields = ('pokémon', 'opinión')
        
       
