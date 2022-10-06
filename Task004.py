# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
0
dec_num = int(input("Введите десятичное число: "))
result = []
x = list(str(dec_num))[::-1]
if dec_num == 0:
    print("Введите десятичное число отличное от нуля")
    exit
number = dec_num
def DecToBin(dec_num):
    
    while True:
        if dec_num != 0:
            if dec_num % 2 == 0:
                result.append(0)
                dec_num = dec_num // 2
            elif dec_num % 2:
                result.append(1)
                dec_num = dec_num // 2
        else:
            result.reverse()
            break
    return result
    

print(f"Число {number} в двоичной системе это {DecToBin(dec_num)}")