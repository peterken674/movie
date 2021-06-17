from flask import render_template
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from . import main
from ..requests import get_movies, get_genres

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    title='Home | MOTD'

    return render_template('home.html', popular=popular_movies, title=title)

@main.route('/genres', methods=['GET', 'POST'])
def genres():

    title = 'Genres| MOTD'
    genres = get_genres()

    if request.method == 'POST':
        fav_genres = request.form.getlist('fav_genres')
        print(fav_genres)

        return redirect(url_for('main.index'))


    return render_template('genres.html', title=title, genres = genres)
