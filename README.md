# movie-test1
superuser: butterfly1of4 pw: movieadmin1
new decouple package:
https://pypi.org/project/python-decouple/

https://developer.nytimes.com/docs/movie-reviews-api/1/overview
nytt SECRET_KEY=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a



# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# http://docs.python-requests.org/en/master/user/install/

import requests

def execute():
  requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&order=by-opening-date&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)

  print request.content

if __name__ == "__main__":
  execute()
