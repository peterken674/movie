from sqlalchemy.orm import backref, lazyload
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    subscribed = db.Column(db.Boolean)
    password_hash = db.Column(db.String(255))

    genres = db.relationship('FavoriteGenre', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,movie_id,title,overview,poster,vote_average,vote_count, backdrop_path, genres):
        self.movie_id =movie_id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.backdrop_path= backdrop_path
        self.genres = genres

class Genre:
    '''
    Class to define genres.
    '''

    def __init__(self,id,name):
        self.id = id
        self.name = name

class FavoriteGenre(db.Model):

    __tablename__ = 'favorite_genres'

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer)
    name = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Trailer:
    '''
    Class to store trailer details.
    '''
    def __init__(self, id, key, name, site, trailer_type):
        self.id = id
        self.link = 'https://www.youtube.com/watch?v=' + key
        self.name = name
        self.site = site
        self.type = trailer_type