#Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
#5 -> 2, 4
#8 -> 2, 4, 6, 8

N = int(input("Введите число "))
count = 2
number = 2
while count <= N:
    print(number)
    count += 2
    number += 2