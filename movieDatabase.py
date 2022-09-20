import twitterBotKeys as twitterBot
import requests
import json

class Film:
    def __init__(self, title, year, genre, plot, imdbRating, poster):
        self.title = title
        self.year = year
        self.genre = genre
        self.plot = plot
        self.imdbRating = imdbRating
        self.poster = poster

def getID(titleName, type):
    url = "https://movie-database-alternative.p.rapidapi.com/"
    
    querystring = {"s":titleName,"r":"json","page":"1", "type":type}

    headers = {
        "X-RapidAPI-Key": twitterBot.rapidapi_key,
        "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)

    try:
        id = json_data['Search'][0]['imdbID']
        return id, 'ok'
    except:
        return -1, 'error'

def getFilm(id):
    url = "https://movie-database-alternative.p.rapidapi.com/"
    
    querystring = {"r":"json","i":id}

    headers = {
        "X-RapidAPI-Key": twitterBot.rapidapi_key,
        "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
    }

    querystring = {"r":"json","i":id}

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)

    newFilm = Film (title=json_data['Title'],
                    year=json_data['Year'],
                    genre=json_data['Genre'],
                    plot=json_data['Plot'],
                    imdbRating=json_data['imdbRating'],
                    poster=json_data['Poster']
                   )
    return newFilm

def getFilmTitle(string):
    film_title = ""
    type = ""

    a = string.find('movie="')
    b = string.find('movie="', a+7)
    
    c = string.find('series="')
    d = string.find('series="', c+8)

    if a != -1 and b == -1 and c == -1 and d == -1:
        x = a + 7
        type = 'movie'
    elif a == -1 and b == -1 and c != -1 and d == -1:
        x = c + 8
        type = 'series'
    else:
        return any, any, 'error'


    y = string.find('"', x)
    if y == -1:
        return any, any, 'error'

    i = x
    while i < y:
        film_title += string[i]
        i += 1

    return film_title, type, 'ok'
