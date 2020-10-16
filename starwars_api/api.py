from rest_framework.response import Response

from starwars_api.views import CharacterAPIService, RatingAPIService
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework import status
from starwars_api.models import Rating


class RatingAPI(APIView):
    def post(self, request, **kwargs):
        """
        :param request: Request and body of the post
        :param kwargs: URL parameters
        :return: Response with id of character and given rating
        """
        req = request.data
        id_ = kwargs.get('character_id')
        req['character_id'] = id_
        RatingAPIService.validate_rating(req.get('rating'))
        serializer = DataSerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterAPI(APIView):
    def get(self, request, **kwargs):
        """
        :param request:
        :param kwargs:
        :return:
        """

        id_ = kwargs.get('character_id')
        character = CharacterAPIService.get_people(id_)
        planet = CharacterAPIService.get_planet(character)
        species = CharacterAPIService.get_species(character)
        return Response(
            CharacterAPIService.get_data_as_dictionary(
                character, planet, species,
                CharacterAPIService.avg_rating(id_),
                CharacterAPIService.maximum_rating(id_)),
            status=status.HTTP_200_OK
        )
