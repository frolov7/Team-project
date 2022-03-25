from sqlalchemy import desc
from app.models import Serials
from app.time import get_days, make_time
from math import ceil


def matches(parameters, serial):
    for p in parameters:
        if p not in serial:
            return False
    return True


def includes(parameters, serial):
    if (not parameters) or (serial in parameters):
        return True
    else:
        return False


def found_serials(genres_s, actors_s, countries_s, category_s, status_s, seasons_s_min, seasons_s_max, year_s_min,
                  year_s_max, length_s_min, length_s_max, seriesAmount, daysNumber, period, value):

    serials = Serials.query.filter(Serials.seasons <= seasons_s_max, Serials.seasons >= seasons_s_min,
                                    Serials.year <= year_s_max, Serials.year >= year_s_min, Serials.length <= length_s_max,
                                    Serials.length >= length_s_min).order_by(desc(Serials.rating)).all()
    
    found_serials = []
    times = {}

    period = get_days(period)
    value = get_days(value)

    if daysNumber:
        max_time = daysNumber * value
    else:
        max_time = 0

    for serial in serials:
        genres = serial.genre.split(" | ")
        actors = serial.actors.split(" | ")
        countries = serial.country.split(" | ")

        years = 0
        months = 0
        weeks = 0
        days = 0
        if seriesAmount:
            episodes = int(serial.episodes)
            days = ceil((episodes * period) / seriesAmount)

        if matches(genres_s, genres) and matches(actors_s, actors) and matches(countries_s, countries) and \
                (not max_time or (max_time and 0 < days <= max_time)) and includes(status_s, serial.status) and \
                    includes(category_s, serial.category):
            found_serials.append(serial)


            if days > 365:
                years = days // 365
                days = days % 365
            if days >= 30:
                months = days // 30
                days = days % 30
            if days >= 7:
                weeks = days // 7
                days = days % 7
            time = make_time(years, months, weeks, days)
            if time == "":
                times[serial] = "-"
            else:
                times[serial] = time
        
    return found_serials, times
