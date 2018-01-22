import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits_1=["apple", "banana", "kiwi", "watermelon", "cherry", "pomegranate"]
for i in range(len(fruits_1)):
    print("{}. {:>10}".format(i + 1, fruits_1[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
fruits_2=["pear", "banana", "grapes", "watermelon", "pineapple"]
for i in fruits_2:
    for j in fruits_1:
        if i == j:
            fruits_1.remove(j)

print(fruits_1)
print(fruits_2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
digits = [1, 3, 5, 4, 6, 7, 9, 7, 6, 3, 0, 10, 4, 2]
new_digits = []
print(digits)
for digit in digits:
    if digit % 2 == 0:
        new_digits.append(digit/4)
    else:
        new_digits.append(digit * 2)

print(new_digits)