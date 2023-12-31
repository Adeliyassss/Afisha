from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data= DirectorSerializer(directors, many=True).data
    return Response(data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Director is not found"})
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie, many=True).data
    return Response(data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Movie is not found"})
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Review is not found"})
    data = ReviewSerializer(review).data
    return Response(data=data)