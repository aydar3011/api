from django.shortcuts import render
from django.http import HttpResponse
from .models import films
import requests, json
# Create your views here.


def index(request):
    publicApiData = requests.get("https://ghibliapi.herokuapp.com/films").json()

    for row in publicApiData:
        result = films.objects.get(title__contains=row['title'])

        row['title_rus'] = result.title_rus
        row['description_rus'] = result.description_rus
        row['imdb'] = str(result.imdb)

    return HttpResponse(json.dumps(publicApiData, ensure_ascii=False, indent=4), content_type="application/json")
