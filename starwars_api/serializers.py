from rest_framework import serializers

from starwars_api.models import Rating


class DataSerializer(serializers.Serializer):
    """
    Serialize the information from the post body
    """
    rating = serializers.FloatField()
    character_id = serializers.IntegerField()

    def create(self, validated_data):
        instance = Rating()
        instance.rating = validated_data.get('rating')
        instance.character_id = validated_data.get('character_id')
        instance.save()
        return instance
