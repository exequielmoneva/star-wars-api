import requests
from django.shortcuts import render
from rest_framework.exceptions import NotFound, ParseError

from starwars_api.models import Rating


def index(request):
    """
    Main page of the web
    """
    return render(request, "starwars/index.html")


class CharacterAPIService:
    @classmethod
    def get_people(cls, id_):
        """
        :param id_: id of the character
        :return: Information of the character
        """
        response = requests.get('http://swapi.dev/api/people/' + str(id_))
        if response.status_code != 200:
            raise NotFound('Character not found')
        people = response.json()
        return people

    @classmethod
    def get_planet(cls, character):
        """
        :param character: id of the character
        :return: Planet of the character
        """
        try:
            response = requests.get(character.get('homeworld'))
            planets = response.json()
            return planets
        except Exception:
            return {}

    @classmethod
    def get_species(cls, character):
        """
        :param character: id of the character
        :return: Species of the character
        """
        try:
            response = requests.get(list(character.get('species'))[0])
            species = response.json()
            return species
        except Exception:
            return {}

    @classmethod
    def get_data_as_dictionary(
            cls, character, planet, species, average, maximum):
        """
        :param maximum: Top rating for character
        :param average: Average rating for character
        :param character: Information of the character
        :param planet: Planet of the character
        :param species: Species of the character
        :return: dictionary containing information about the character
        """
        return {
            'name': character.get('name'),
            'height': character.get('height'),
            'mass': character.get('mass'),
            'hair_color': character.get('hair_color'),
            'skin_color': character.get('skin_color'),
            'eye_color': character.get('eye_color'),
            'birth_year': character.get('birth_year'),
            'gender': character.get('gender'),
            'homeworld': {
                'name': planet.get('name'),
                'population': planet.get('population'),
                'known_species_count': len(planet.get('residents'))
            },
            'species_name': species.get('name'),
            'average_rating': average,
            'max_rating': maximum
        }

    @classmethod
    def avg_rating(cls, character_id):
        """
        :param character_id: Id of the character
        :return: Average rating based on stored ratings. Rounded to 2 decimals
        """
        try:
            ratings = Rating.objects.filter(
                character_id=character_id).values_list('rating', flat=True)
            return round(sum(ratings) / len(ratings), 2)
        except ZeroDivisionError:
            return 0
        except ValueError:
            return 0

    @classmethod
    def maximum_rating(cls, character_id):
        """
        :param character_id: Id of the character
        :return: Top rating based on stored ratings.
        """
        try:
            ratings = Rating.objects.filter(
                character_id=character_id).values_list('rating', flat=True)
            return round(max(ratings))
        except ZeroDivisionError:
            return 0
        except ValueError:
            return 0


class RatingAPIService:
    @classmethod
    def validate_rating(cls, rating):
        """
        :param rating: Rating given inside the POST body
        """
        if rating > 5 or rating < 1:
            raise ParseError('Rating value must be between 1 and 5')
