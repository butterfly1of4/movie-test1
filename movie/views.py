from django.shortcuts import render
from .models import Movie
import requests

# Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'movie/movie_list.html', {'movies': movies})


# From NYT website
def execute():
    requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
    requestHeaders = {
        "Accept": "application/json"
    }

    request = requests.get(requestUrl, headers=requestHeaders)
    return render(request.content)
#   print(request.content)

# if __name__ == "__main__":
#   execute()


# From Dev webiste: https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i
# def get_movies(request):
#     all_movies= {}
#     if 'name' in request.GET:
#         name=request.GET['name']
#         url='https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&order=by-opening-date&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a'
#         # url='https://api.nytimes.com/svc/movies/v2/reviews/article.json'
#         # url='https://api.nytimes.com/svc/movies/v2'
#         response= requests.get(url)
#         data=response.json()
#         movies= data['movies']

#         for i in movies:
#             movie_data=Movie(
#                 title= i['display_title'],
#                 description = i['headline'],
#                 year = i['opening_date'],
#                 summary =  i['summary_short'],
#                 image = i['src']
#             )
#             movie_data.save()
#             all_movies = Movie.objects.all().order_by('-id')
#     return render (request, 'movies/movie.html', {'all_movies': all_movies})
#     # https://api.nytimes.com/svc/movies/v2,
