from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Movie
from .permissions import IsSuperUserOrReadOnly
from .serializers import MovieOrderSerializer, MovieSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        movies = Movie.objects.all().order_by('id')
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = get_object_or_404(Movie, id=movie_id)

        serializer.save(user=request.user, movie=movie)

        return Response(serializer.data, status.HTTP_201_CREATED)
