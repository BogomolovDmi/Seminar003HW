# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = int(input("Введите число "))
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))