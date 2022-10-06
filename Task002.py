# Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

n = int(input("Введите число "))
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(pairs_mult(mylist))