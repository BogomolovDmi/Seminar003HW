# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
from heapq import nsmallest

def get_real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    if min(nums) == 0.0:
        print(nsmallest(2,nums)[-1])
        print(max(nums))
        return max(nums) - nsmallest(2,nums)[-1]
        exit
    print(min(nums))
    print(max(nums))
    return max(nums) - min(nums)

n = int(input("Введите число "))
frst = 1
last = 10
mynums = get_real_nums(n, frst, last)

print (mynums)
print(find_diff(mynums))

# Проведя около 50 тестов программа меня обыграла, я выставил условие, 
# чтобы в расчёт бралось второе наименьшее значение дробной части
# Проблема в том, что если мы будем брать больше 5 чисел и тд, шанс на выпадение двух целых чисел остается
# И в этом случае ноль будет взят в обработку как второе наименьшее число. 
# А как выставить условие, чтобы ноль вообще не брался я не знаю =)