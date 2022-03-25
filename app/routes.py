from flask import render_template, request
from app import app
from app.models import Serials, Actors, Genres, Countries
from app.search import found_serials


def pos(value, min, max):
    position = str((value - min) / (max - min + 1))
    return position


@app.route("/", methods=['GET', 'POST'])
def main():
    
    series = Serials.query.all()
    series_s = []

    genres_list = Genres.query.all()
    actors_list = Actors.query.order_by(Actors.actor).all()
    countries_list = Countries.query.all()

    genres_s = []
    category_s = []
    status_s = []
    
    actors_id_s = []
    actors_s = []

    countries_s = []
   
    seasons_s_min = 1
    seasons_s_max = 8

    year_s_min = 1900
    year_s_max= 2020

    length_s_min = 20
    length_s_max = 360

    year_pos_min = "0"
    year_pos_max = "1"
    seasons_pos_min = "0"
    seasons_pos_max = "1"
    length_pos_min = "0"
    length_pos_max = "1"

    seriesAmount = 0
    daysNumber = 0
    period = "День"
    value = "День"

    if request.method == 'POST':
        action = request.form.get("action")
        if action == "search":
            genres_s = request.form.getlist("inputGenres")
            countries_s = request.form.getlist("inputCountry")
            category_s = request.form.getlist("inputCategory")
            status_s = request.form.getlist("inputStatus")

            actors_s = request.form.getlist("inputActor")
            #for id in actors_id_s:
             #   actors_s.append(actors_list[int(id)])

            seasons_s_min = request.form.get("inputSeason_min")
            seasons_s_max = request.form.get("inputSeason_max")

            seasons_s_min = int(seasons_s_min)
            seasons_s_max = int(seasons_s_max)

            seasons_pos_min = pos(seasons_s_min, 1, 32)
            seasons_pos_max = pos(seasons_s_max, 1, 32)

            year_s_min = request.form.get("inputDates_min")
            year_s_max = request.form.get("inputDates_max")

            year_s_min = int(year_s_min)
            year_s_max = int(year_s_max)

            year_pos_min = pos(year_s_min, 1969, 2020)
            year_pos_max = pos(year_s_max, 1969, 2020)

            length_s_min = request.form.get("inputTime_min")
            length_s_max = request.form.get("inputTime_max")

            length_s_min = int(length_s_min)
            length_s_max = int(length_s_max)

            length_pos_min = pos(length_s_min, 6, 110)
            length_pos_max = pos(length_s_max, 6, 110)

            seriesAmount = (request.form.get("willWatch"))  # Буду смотреть серий в (День/неделя/месяц)
            if seriesAmount:
                seriesAmount = int(seriesAmount)
            daysNumber = (request.form.get("wantToWatch"))  # Хочу посмотреть сериал за (ден/неделя/месяц)
            if daysNumber:
                daysNumber = int(daysNumber)

            period = request.form.get("inputDaysNumber")  # Выпадающее меню (ден/неделя/месяц)
            value = request.form.get("inputDaysNumber2")  # Выпадающее меню (ден/неделя/месяц)


    series_s, times = found_serials(genres_s, actors_s, countries_s, category_s, status_s,
                                    seasons_s_min, seasons_s_max, year_s_min, year_s_max,length_s_min, length_s_max,
                                    seriesAmount, daysNumber, period, value)

    return render_template("main.html", series = series_s, genres = genres_list, actors = actors_list, countries = countries_list,
                           actors_s = actors_s, genres_s = genres_s, countries_s = countries_s, time = times, value = value, period = period,
                           year_pos_min = year_pos_min, year_pos_max = year_pos_max,
                           seasons_pos_min = seasons_pos_min, seasons_pos_max = seasons_pos_max,
                           length_pos_min = length_pos_min, length_pos_max = length_pos_max, seriesAmount = seriesAmount, daysNumber = daysNumber,
                           category_s = category_s, s = "Сериалы", m = "Мультсериалы", a = "Аниме", status_s = status_s, f = "Завершен", c = "Выходит")


@app.route("/info/<id>", methods=['GET', 'POST'])
def info(id):
    ser = Serials.query.filter_by(id=id).first()
    return render_template("info_page.html", ser=ser)
