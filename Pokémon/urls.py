#en cada app creamos este archivo e importamos el módulo path
from django.urls import include, path
#además importamos las funciones que usará cada app
from Pokémon.views import bulbasaur, hello, pikachu, charmander, chikorita, chimchar, piplup, squirtle,treecko
#from . import views

from rest_framework import routers
from .api import PokémonViewSet

# Crea un enrutador
router = routers.DefaultRouter()
router.register('api/pokémon', PokémonViewSet)



urlpatterns = [
    #cuando el usuario visite la página se mostrará la función hello
    path('', hello),
    #enlaces a cada pokémon
    path('pikachu/', pikachu),
    path('bulbasaur/', bulbasaur),
    path('charmander/', charmander),
    path('chikorita/', chikorita),
    path('chimchar/', chimchar),
    path('piplup/', piplup),
    path('squirtle/', squirtle),
    path('treecko/', treecko),
    
   # Incluye las URLs del enrutador en las URLs principales
    path('api/', include(router.urls)),
]



