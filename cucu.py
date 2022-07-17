# import math
#               Глава 2. Типы данных
# for _ in (0, 1, 2, 3, 4, 5):
#     print('Hello')

#                Пример куска кода:
# radio = 5
# vieja_area = 1
# pi = math.pi
# e = 0.0000001
# nueva_area = pi * radio * radio
# if abs(nueva_area - vieja_area) < e:
#     print('las areas han converdigo')


#                          целочисенные типы данных

#1) Десятичное число:  14600926
#                      14600926
# Двоичное: 0b11011100101    записывается с префиксом 0b
#            1765
# Восьмеричное: 0o3642764263245 записывается с префиксом 0o
#               262392604325
# Шестнадцатеричное: 0xDECADE  записывается с префиксом 0x
#                    14600926


#                 Арифметические операции:
# x+y сложение
# x-y вычитание
# x * y умножение
# x/y  делит
# x // y делит, при этом усекает дробную часть
# x % y  возвращает модуль(остаток) от деления
# x ** y возведение в степень
# -x  изменяет знак числа, если число не нуль
# +x ничего не делает
# abs(x) возвращает абсолютное значение x
# divmod(x, y) возвращает частное и остаток от деления
# pow(x, y)  возведение в степень
# pow(x, y, z) более быстрая альтернатива (x ** y) % z
# round(x, n) округление


# def equal_float(a, b):
#     return abs(a - b) <= sys.float_info.epsilon
# import math
#                1 метод
# def extract_from_tag(tag, line):
#     opener = "<" + tag + ">"
#     closer = "</" + tag + ">"
#     try:
#         i = line.index(opener)
#         start = i + len(opener)
#         j = line.index(closer, start)
#         return line[start:j]
#     except ValueError:
#         return None

# s = '=' * 5
# print(s)
# =====
# s*=10
# print(s)
# ==================================================
#   опреатор * обеспечивает возможность дублирования строки


#                2 метод
# def extract_from_tag(tag, line):
#     opener = "<" + tag + ">"
#     closer = "</" + tag + ">"
#     i = line.find(opener)
#     if i != -1:
#         start = i + len(opener)
#         j = line.find(closer, start)
#         if j != -1:
#             return line[start:j]
#     return None


#  фрагменты поясняющие действие метода str.partition()
# 1
# result = s.rpartition('/')
#  2
# i = s.find('/')
# if i == -1:
#     result = s, '', ''
# else:
#     result = s[:i], s[i], s[i + 1:]

#  1 и 2 не эквивалентны, так как фрагмент 2 создает новую переменную i

#  метод str.endwith()(и str.startwith()) может использовать с единственным строковыи аргументом,
# например s.startwith('From:'), или с кортежом строк str.endwith() и str.lower() для вывода имени файла, если он
#  является файлом изображения в формате JPEG:
# if filename.lower().endwith(('.jpg', '.jpeg')):
#     print(filename, 'is a JPEG image')

#  пример преобразования бенгальских цифр в английские:
# table = ''.maketrans('\N{bengali digit zero}'
#     '\N{bengali digit one}\N{bengali digit two}'
#     '\N{bengali digit three}\N{bengali digit four}'
#     '\N{bengali digit five}\N{bengali digit six}'
#     '\N{bengali digit seven}\N{bengali digit eight}'
#     '\N{bengali digit nine}', '0123456789')
# print('20749'.translate(table))                                # выведет: 20749
# print('\N{bengali digit two}07\N{bengali digit four}'
#       '\N{bengali digit nine}'.translate(table))                # выведет: 20749


# Форматирование строк с помощью метода str.format()
# я ебал, буду разбирать примеры и задачи









