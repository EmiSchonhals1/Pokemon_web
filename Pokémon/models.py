from django.db import models


class pokémon_favorito (models.Model) :
    #este campo u objeto de la tabla guardará en un string (CharField) los nombres de los pokémon favoritos de cada persona
    name = models.CharField(max_length=50)
    #este objeto guardará en un string largo sin máximo de caracteres(TextField) la opinión de cada usuario de por qué le gusta ese pokémon, pero será opcional
    opinion = models.TextField()
    
    #función que nos permite ver en Django admin los nombres de los objetos de la clase pokémon_favorito
    def __str__(self):
        return self.name #devuelve los valores almacenados en la variable name



