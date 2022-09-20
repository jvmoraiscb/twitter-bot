import movieDatabase as dataBase
import requests
import os

def imdbService(tweet, api):
    try:
        api.create_favorite(tweet.id)
    except:
        return 'Error: Already interact with this tweet!'

    try:
        title, type, result = dataBase.getFilmTitle(tweet.text)
        if result == 'error':
            api.update_status(status='Sorry, I couldnt understand your request, please do like the example:\n\nvascopuppy:imdb movie="movie_name"\n\nor\n\nvascopuppy:imdb series="series_name"', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            return 'Error: Invalid request!'

        id, result = dataBase.getID(titleName=title, type=type)
        if result == 'error':
            api.update_status(status='Sorry, ' + type + ' not found!', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            return 'Error: Movie/Series not found!'

        film = dataBase.getFilm(id)

        status = film.title + ' (' + film.year + ')\n' + film.genre + '\n' + 'imdbRating: ' + film.imdbRating + '\n\n' + film.plot

        request = requests.get(film.poster, stream=True)
        if request.status_code == 200:
            with open('temp.jpg', 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            api.update_status_with_media(filename='temp.jpg', status=status, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            os.remove('temp.jpg')
            #print('downloaded image!')
        else:
            #print("Error: unable to download image")
            api.update_status(status=status, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)

        return 'Ok!'
    except:
        api.update_status(status='Sorry, something went wrong!', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        return 'Error: unknow'

def helpService(tweet, api):
    try:
        api.create_favorite(tweet.id)
    except:
        return 'Error: Already interact with this tweet!'
        
    api.update_status(status='You can get information about a movie or series using the command:\n\n#vascopuppy:imdb movie="movie name"\n\nor\n\n#vascopuppy:imdb series="series name"', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    return 'Ok!'