#coding: utf-8
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
list = [random.randint(-10, 10) for _ in range(10)]
list2 = []

# Почему решение с лямбдой не работает?:
# list2 = list(map(lambda x: x ** 2 , list))

print(list)
for el in list[:]:
    list2.append(el ** 2)

print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_1=["apple", "banana", "kiwi", "watermelon", "cherry", "pomegranate"]
fruits_2=["pear", "banana", "grapes", "watermelon", "pineapple"]
only_both_fruits = [el for el in fruits_2 if el in fruits_1]
print(only_both_fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list3 = [random.randint(-10, 10) for _ in range(10)]
print(list3)
list4 = []
for el in list3:
    if ((el % 3 == 0) and (el > 0) and (el % 4 != 0)):
        list4.append(el)
print(list4)