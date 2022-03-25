def get_days(period):
    days = 0
    if period == "День" or period == "Дней":
        days = 1
    elif period == "Неделю" or period == "Недель":
        days = 7
    elif period == "Месяц" or period == "Месяцев":
        days = 30
    return days


def make_time(years, months, weeks, days):
    d = " дней "
    if (days % 100) in range(11, 15):
        d = " дней "
    elif (days % 10) in range(2, 5):
        d = " дня "
    elif (days % 10) == 1:
        d = " день "

    w = " недель "
    if (weeks % 10) in range(2, 5):
        w = " недели "
    elif (weeks % 10) == 1:
        w = " неделю "

    m = " месяцев "
    if (months % 100) in range(11, 15):
        m = " месяцев "
    elif (months % 10) in range(2, 5):
        m = " месяца "
    elif (months % 10) == 1:
        m = " месяц "

    y = " лет "
    if (years % 100) in range(11, 15):
        y = " лет "
    elif (years % 10) in range(2, 5):
        y = " года "
    elif (years % 10) == 1:
        y = " год "

    time = ""

    if years:
        time += str(years) + y
    if months:
        time += str(months) + m
    if weeks:
        time += str(weeks) + w
    if days:
        time += str(days) + d

    return time
