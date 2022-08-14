import datetime

DAYS_IN_MONTHS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
LAST_MONTH_INDEX = 12;

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    some_date = datetime.datetime.strptime(some_date, '%Y-%m-%d');
    [day, month, year] = [some_date.day, some_date.month, some_date.year]
    daysCount = DAYS_IN_MONTHS[month]
    day += 1

    if (day > daysCount):
        if month == LAST_MONTH_INDEX:
            year += 1
            month = 1
            day = 1

            return datetime.date(year, month, day)

        month += 1
        day = 1

    return datetime.date(year, month, day)

print(get_next_date('2022-03-01'))
print(get_next_date('2022-01-31'))
print(get_next_date('2022-12-31'))
