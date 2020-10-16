from django.urls import path

from starwars_api.api import RatingAPI, CharacterAPI
from .views import index

urlpatterns = [
    path("", index, name="home"),
    path(r"character/<int:character_id>",
         CharacterAPI.as_view(), name="get"),
    path(r'character/<int:character_id>/rating',
         RatingAPI.as_view(), name='post')
]