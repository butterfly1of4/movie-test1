def full_list(request):
    all_movies= Movie.objects.all()
    if 'display_title' in request.GET:
        display_title=request.GET['display_title']
        url='https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&order=by-opening-date&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a'

        response= requests.get(url)
        data=response.json()
        movies= data['movies']

        for i in movies:
            movie_data=Movie(
                display_title= i['display_title'],
                byline = i['byline'],
                opening_date = i['opening_date'],
                headline = i['headline'],
                summary_short =  i['summary_short'],
                url= i['url'],
                image = i['src']
            )
            movie_data.save()
            all_movies = Movie.objects.all().order_by('-id')
    return render (request, 'movies.html', {'all_movies': all_movies})

# From NYT website
# def execute():
#     requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
#     requestHeaders = {
#         "Accept": "application/json"
#     }

#     request = requests.get(requestUrl, headers=requestHeaders)
#     return render(request.content)
#     print(request.content)

# if __name__ == "__main__":
#   execute(request)

# original
# def full_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'movie/full_list.html', {'movies': movies})


# def full_list(request):
#     movies = Movie.objects.all()
#     if request.method == 'GET':
#             requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
#     requestHeaders = {
#         "Accept": "application/json"
#     }
#     request = requests.get(requestUrl, headers=requestHeaders)
#     print(request.content)
#     return render(request.content, 'movie/full_list.html', {'moives':movies})

# if __name__ == "__main__":
#     full_list(request)
#     request = requests.get(requestUrl, headers=requestHeaders)
        # r = requests.get('https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a')
        # requestHeaders = {
        #     "Accept":"application/json"
        #     }
        
        # if r.status_code == 200:
        #     data = r.json()
        #     return Response(data)
        # else:
        #     return('try again')




# From Dev webiste: https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i
# def get_movies(request):
    all_movies= {}
    if 'name' in request.GET:
        name=request.GET['name']
        url='https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&order=by-opening-date&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a'
#         # url='https://api.nytimes.com/svc/movies/v2/reviews/article.json'
#         # url='https://api.nytimes.com/svc/movies/v2'
        response= requests.get(url)
        data=response.json()
        movies= data['movies']

        for i in movies:
            movie_data=Movie(
                title= i['display_title'],
                description = i['headline'],
                year = i['opening_date'],
                summary =  i['summary_short'],
                image = i['src']
            )
            movie_data.save()
            all_movies = Movie.objects.all().order_by('-id')
    return render (request, 'movies/movie.html', {'all_movies': all_movies})
#     # https://api.nytimes.com/svc/movies/v2,