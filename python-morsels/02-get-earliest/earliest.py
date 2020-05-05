def get_earliest_first(date1, date2):
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')

    if y1 < y2:
        return date1
    elif y1 > y2 or m1 > m2:
        return date2
    elif m1 < m2 or d1 < d2:
        return date1
    return date2


def get_earliest_second(date1, date2):
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')
    da1 = (y1, m1, d1)
    da2 = (y2, m2, d2)
    if da1 > da2:
        return date2
    return date1


def get_earliest(*args):
    dates = {}
    for arg in args:
        m, d, y = arg.split('/')
        dates[arg] = (y, m, d)
    ear_key, ear_value = (None, None)
    for key, value in dates.items():
        if ear_value is None or value < ear_value:
            ear_key, ear_value = key, value
    return ear_key


print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))

