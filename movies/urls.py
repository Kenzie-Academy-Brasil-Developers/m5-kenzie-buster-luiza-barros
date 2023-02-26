from django.urls import path
from .views import MovieView, MovieDetailsView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailsView.as_view()),
]
