from rest_framework import serializers

from .models import RatingChoices, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, allow_null=True)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, required=False, default=RatingChoices.G_OPTION
    )
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by = serializers.EmailField(read_only=True, source='user.email')

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
