
__author__ = 'Ratnikov Alex'
import math


# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print("Enter integer unsigned number")
a = input()
len = len(a)
max = a[0]
while len > 0:
    if a[len-1] > max:
        max = a[len-1]
    len = len - 1
print("Maximum is:%s" % max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

#normal
# print("enter variable a")
# a = int(input())
# print("enter variable b")
# b = int(input())
# a=a+b
# b=a-b
# a=a-b
# print("magic! a=%s, b=%s" % (a, b))

#tuple
print("enter variable a")
a = input()
print("enter variable b")
b = input()
t = (a, b)
b = t[0]
a = t[1]
print("magic! a=%s, b=%s" % (a, b))


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
print("enter a of ax² + bx + c = 0")
a = int(input())
print("enter b of ax² + bx + c = 0")
b = int(input())
print("enter c of ax² + bx + c = 0")
c = int(input())

d = b**2 - 4 * a * c

if d < 0:
    print("cannot be solved!")
elif d == 0:
    print("x=", -b/(2*a))
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1=%s, x2=%s" % (x1, x2))
