from django.urls import path
from . import views

app_name = "index"
urlpatterns = [
    path("", views.index, name="index"),
    path("contribute/", views.contribute, name="contribute"),
    path("movie/<int:movieid>/", views.movie, name="movie")
]