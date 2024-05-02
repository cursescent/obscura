from django.http import HttpResponse
from random import sample
from django.template import loader
from .source_tools import get_source_json
from .models import Movie, Review
from .forms import MovieForm

def index(request):
    movies = Movie.objects.order_by("movieid")
    movie_sample_indices = sample(range(len(movies)), 5) if len(movies) > 5 else [i for i in range(len(movies))]
    movie_sample = [movies[i] for i in movie_sample_indices]
    template = loader.get_template("index/index.html")
    context = {
        "movie_count": len(movies),
        "movie_sample": movie_sample,
    }
    return HttpResponse(template.render(context, request))

def contribute(request):
    if request.method == "POST":
        form_data = MovieForm(request.POST)
        template = loader.get_template("index/contribute.html")
        context = {
            "status": "success",
            "form": form_data,
        }
        if form_data.is_valid():
            new_id = Movie.objects.order_by("-movieid")[0].movieid + 1 if len(Movie.objects.all()) > 0 else 0
            movie = Movie(
                movieid = new_id,
                title = form_data.cleaned_data["title"],
                year = form_data.cleaned_data["year"],
                genres = form_data.cleaned_data["genres"],
                duration = form_data.cleaned_data["duration"],
                director = form_data.cleaned_data["director"],
                writer = form_data.cleaned_data["writer"],
                producer = form_data.cleaned_data["producer"],
                starring = form_data.cleaned_data["starring"],
                sources = get_source_json(form_data.cleaned_data["sources"])
            )
            movie.save()
        else:
            context["status"] = "failure"
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("index/contribute.html")
        context = {
            "status": "none",
            "form": MovieForm(),
        }
        return HttpResponse(template.render(context, request))

def movie(request, movieid):
    template = loader.get_template("index/movie.html")
    context = {
        "movie": Movie.objects.filter(movieid=movieid)[0],
        "reviews": Review.objects.filter(movieid=movieid),
    }
    return HttpResponse(template.render(context, request))
