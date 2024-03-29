import urllib.request, json

from flask.globals import session
from .models import Movie, Genre, Trailer, FavoriteGenre

api_key=None
base_url=None
genres_url=None
trailer_url=None
genre_movies_url=None

def configure_request(app):
    global api_key, base_url, genres_url, trailer_url, genre_movies_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    genres_url = app.config['GENRES_URL']
    trailer_url = app.config['TRAILERS_URL']
    genre_movies_url = app.config['GENRE_MOVIES_URL']

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        movie_id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        backdrop_path = movie_item.get('backdrop_path')
        genres = movie_item.get('genre_ids')
        trailers_list = get_trailer(movie_id)


        for trailer in trailers_list:
            if trailer.site == 'YouTube':
                trailer_url = trailer.link
                break

        if poster:
            movie_object = Movie(movie_id,title,overview,poster,vote_average,vote_count, backdrop_path, genres, trailer_url)
            movie_results.append(movie_object)

    return movie_results

def get_genres():
    get_genres_url = genres_url.format(api_key)
    with urllib.request.urlopen(get_genres_url) as url:
        get_genres_data = url.read()
        get_genres_response = json.loads(get_genres_data)
        
        genres_results = None
        
        if get_genres_response['genres']:
            genres_results_list = get_genres_response['genres']
            genres_results = process_genres_results(genres_results_list)
        
    return genres_results

def process_genres_results(genres_results_list):
    genres_results = []
    for genre_item in genres_results_list:
        id = genre_item.get('id')
        name = genre_item.get('name')
        genre_object = Genre(id,name)
        genres_results.append(genre_object)
    return genres_results

# Trailer request.
def get_trailer(movie_id):
    get_trailer_url = trailer_url.format(movie_id, api_key)

    with urllib.request.urlopen(get_trailer_url) as url:
        get_trailer_data = url.read()
        get_trailers_response = json.loads(get_trailer_data)

        trailer_results = None

        if get_trailers_response['results']:
            trailer_results_list = get_trailers_response['results']
            trailer_results = process_trailer_results(trailer_results_list)

    return trailer_results

def process_trailer_results(trailer_results_list):
    trailer_results = []

    for trailer in trailer_results_list:
        id = trailer.get('id')
        key = trailer.get('key')
        name = trailer.get('name')
        site = trailer.get('site')
        trailer_type = trailer.get('type')

        trailer_obj = Trailer(id, key, name, site, trailer_type)
        trailer_results.append(trailer_obj)

    return trailer_results


def get_genre_movies(id):
    get_genre_movies_url = genre_movies_url.format(api_key,id)
    with urllib.request.urlopen(get_genre_movies_url) as url:
        genre_movies_data = url.read()
        genre_movies_response = json.loads(genre_movies_data)

        genre_movies_results = None

        if genre_movies_response['results']:
            genre_movies_list = genre_movies_response['results']
            genre_movies_results = process_results(genre_movies_list)
            
    return genre_movies_results

def get_favorite_movies():
    fav_genres = FavoriteGenre.query.all()

    fav_movies_list = []
    for genre in fav_genres:
        genre_movies = get_genre_movies(genre.genre_id)
        fav_movies_list = fav_movies_list.extend(genre_movies)

    return fav_movies_list

    