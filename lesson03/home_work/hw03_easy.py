# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    fractional_part = str(number).split(".")
    fra_str = str(fractional_part[1])
    decision = fra_str[ndigits]
    fra_str = fra_str[0:ndigits]
    part = (int(fra_str) / (10 ** len(fra_str))) + (1 / (10 ** len(fra_str)))

    if int(decision) >= 5:
        if (len(fra_str) == len(str(int(fra_str)+1))):
            num = int(fractional_part[0]) + part
            return num

        elif (len(str(int(fra_str)+1)) == len(fra_str)+1):
            num = int(fractional_part[0]) + part
            return num
    else:
        return fra_str


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) % 2 != 0:
        return False

    part_size = int(len(str(ticket_number)) / 2)
    first_part = list(str(ticket_number)[0:part_size])
    second_part = list(str(ticket_number)[part_size:])
    def sum(part):
        sum = 0
        for i in part:
            sum += int(i)
        return sum

    if sum(first_part) == sum(second_part):
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
