# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    list_len = len(origin_list)
    while list_len >= 0:
        for index, element in enumerate(origin_list):
            if (index < list_len-1):
                if (element > origin_list[index+1]):
                    origin_list[index] = origin_list[index+1]
                    origin_list[index+1] = element
        list_len -= 1

    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
a1 = (9, 5)
a2 = (2, 5)
a3 = (4, 9)
a4 = (12, 9)
def parallelogramm (a1, a2, a3, a4):
    points = [a1, a2, a3, a4]
    points.sort(key=lambda tup: tup[0], reverse=False)
    print(points)
    


parallelogramm(a1,a2,a3,a4)
