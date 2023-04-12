from rest_framework import serializers

from .models import MovieOrder, RatingChoices, Movie


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


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='movie.title', read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(source='user.email', read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)