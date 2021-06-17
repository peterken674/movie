from flask import render_template
from . import main
from ..requests import get_movies, configure_request

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    title='Home | MOTD'

    return render_template('home.html', popular=popular_movies, title=title)

@main.route('/genres')
def genres():

    title= 'Genres| MOTD'

    return render_template('genres.html', title=title)
