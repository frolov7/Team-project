from app import db
from app.models import Serials, Actors, Genres, Countries

series = Serials.query.all()

genres_list = []
actors_list = []
countries_list = []

for serial in series:
    genres = serial.genre.split(" | ")
    actors = serial.actors.split(" | ")
    countries = serial.country.split(" | ")

    for genre in genres:
        if genre not in genres_list:
            genres_list.append(genre)

    for actor in actors:
        if actor not in actors_list:
            actors_list.append(actor)

    for country in countries:
        if country not in countries_list:
            countries_list.append(country)

for i in range(len(actors_list)):
    new = Actors(actor = actors_list[i])
    db.session.add(new)
try:
    db.session.commit()
except:
    db.session.rollback()
    print("Ошибка")

for i in range(len(genres_list)):
    new = Genres(genre = genres_list[i])
    db.session.add(new)
try:
    db.session.commit()
except:
    db.session.rollback()
    print("Ошибка")

for i in range(len(countries_list)):
    new = Countries(country = countries_list[i])
    db.session.add(new)
try:
    db.session.commit()
except:
    db.session.rollback()
    print("Ошибка")

db.session.close()