CELCIUS = "C";
FARENHEIT = "F";

def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    c_to_f = int((value * 9 / 5) + 32)
    f_to_c = int((value - 32) * 5 / 9)
    to_scale = to_scale.upper()

    if to_scale == CELCIUS:
        return f'Конвертация градусов Цельсия в Фарингейта: {c_to_f} {FARENHEIT}'
    elif to_scale == FARENHEIT:
        return f'Конвертация градусов Фарингейта в Цельсия: {f_to_c} {CELCIUS}'
    else:
        return f'Иная система счисления: {value} {to_scale}'

print(convert_temperature(10, "f"))
print(convert_temperature(10, "C"))
print(convert_temperature(10, "A"))
