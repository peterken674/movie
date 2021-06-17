from app.models import FavoriteGenre
from flask import render_template
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from . import main
from ..requests import get_movies, get_genres
from flask_login import login_required
from .. import db

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    title='Home | MOTD'


    return render_template('home.html', popular=popular_movies, title=title)

@main.route('/genres', methods=['GET', 'POST'])
@login_required
def genres():

    title = 'Genres | MOTD'
    genres = get_genres()

    if request.method == 'POST':
        FavoriteGenre.query.delete()
        db.session.commit()
        fav_genres = request.form.getlist('fav_genres')

        i=0
        while i < len(fav_genres):
            for genre in genres:
                if int(genre.id) == int(fav_genres[i]):
                    selected_genre = FavoriteGenre(genre_id=int(genre.id), name=genre.name)
                    db.session.add(selected_genre)
                    db.session.commit()
            i += 1
            

        return redirect(url_for('main.index'))


    return render_template('genres.html', title=title, genres = genres)
