import requests
from django.core.management.base import BaseCommand
from ...models import Movie


def get_movies():
    requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
    # requestHeaders = {
    #     "Accept": "application/json"
    # }
    r = requests.get(requestUrl, headers = {'Content-type':'application/json'})
    movie = r.json()
    return movie   

def seed_movie():
    for i in get_movies():
     movie= Movie(name=i['display_title']
        )
     movie.save()
     
     
class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_movie()
        print(("done"))