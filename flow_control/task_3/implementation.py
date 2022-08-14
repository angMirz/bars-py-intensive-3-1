month_31 = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
month_28_29 = 'февраль'
month_30 = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
date = [31, 30, 29, 28]

def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
def transformation_month_to_date(month):
    if month.lower() in month_31:
        return date[0]
    elif month.lower() in month_30:
        return date[1]
    elif month.lower() in month_28_29:
        return f'{date[2]},{date[3]}'
    else:
        return 0

print(transformation_month_to_date('март'))
print(transformation_month_to_date('июнь'))
print(transformation_month_to_date('февраль'))
print(transformation_month_to_date('якобыдябрь'))
