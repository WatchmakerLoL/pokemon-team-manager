from rest_framework.routers import DefaultRouter

from pokemon.views import PokemonViewset

router = DefaultRouter()
router.register(r'pokemons', PokemonViewset, basename='pokemons')

urlpatterns = router.urls