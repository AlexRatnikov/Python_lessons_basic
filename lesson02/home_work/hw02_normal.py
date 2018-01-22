import math
import datetime
import locale
import random
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

digits = [1, 3, 5, 4, 6, 7, 9, -7, 6, 3, 0, 10, 4, 2, 9.9999, math.pi, -math.e]
new_digits = []
print(digits)
for digit in digits:
    if digit > 0:
        d = math.sqrt(digit)
        if  (d == round(d)):
            new_digits.append(d)
print(new_digits)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
locale.setlocale(locale.LC_ALL, "ru_RU")
days = {
   1: "первое",
    2: "второе",
    22: "двадцать второе",
    23: "двадцать третье",
    24: "двадцать четвертое",
    25: "двадцать пятое",
    27: "двадцать седьмое",
    31: "тридцать первое"

}
date_ru = datetime.date(day=1, month=1, year=2018).strftime('%d %B %Y')
int_day = int(date_ru[0:2])
date_ru = date_ru.replace(date_ru[0:2], str(days[int_day]), 1)
print(date_ru + " года")


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
random_digits = []
n = 10
for d in range(n):
    random_digits.append(random.randint(1, 10))
print(random_digits)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


print("*"*30)
# Лист из задания
# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# Random list из предыдущего задания
lst = random_digits
print(lst)
a = list(set(lst))
print(a)
b = lst
for i in lst:
    if lst.count(i) > 1:
        while b.count(i) > 0:
            b.remove(i)
print(b)
