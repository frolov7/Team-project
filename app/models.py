from app import db

class Serials(db.Model):
    __tablename__ = "Serials"
    id = db.Column(db.Integer, primary_key = True)
    rus_title = db.Column(db.String)
    title = db.Column(db.String)
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    length = db.Column(db.Integer)
    year = db.Column(db.Integer)
    genre = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    actors = db.Column(db.String)
    finished = db.Column(db.Integer)
    country = db.Column(db.String)
    status = db.Column(db.String)
    studio = db.Column(db.String)
    short_description = db.Column(db.String)
    category = db.Column(db.String)

    def __init__(self, rus_title, title, seasons, episodes, length, year, genre, description, rating, actors, finished,
                 country, status, studio, short_description, category):
        self.rus_title = rus_title
        self.title = title
        self.seasons = seasons
        self.episodes = episodes
        self.length = length
        self.year = year
        self.genre = genre
        self.description = description
        self.rating = rating
        self.actors = actors
        self.finished = finished
        self.country = country
        self.status = status
        self.studio = studio
        self.short_description = short_description
        self.category = category

    def __repr__(self):
        return '<Series {}>'.format(self.id)

    
class Actors(db.Model):
    __tablename__ = "Actors"
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.String)

    def __init__(self, actor):
        self.actor = actor

    def __repr__(self):
        return '{}'.format(self.actor)


class Genres(db.Model):
    __tablename__ = "Genres"
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return '{}'.format(self.genre)


class Countries(db.Model):
    __tablename__ = "Countries"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.Integer)

    def __init__(self, country):
        self.country = country

    def __repr__(self):
        return '{}'.format(self.country)
