import random
def zadacha1():
    #Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
    # N может быть любой длины.
    # N = 132:132 + 132132 + 132132132 = 132264396
    n = input('Введите число: ')
    print(int(n*3) + int(n*2) + int(n)) 

def zadacha2():
    #Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
    # [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
    # [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
    numbers = [random.randint(0, 9) for _ in range(15)]
    print(numbers)
    num = int(input('Введите число: '))
    result = ''
    for element in numbers:
        result += str(element)
    print(result)

    if str(num) in result:
        print('Данное число есть')
    else:
        print('Совпадений не найдено')

def check_numbers(x, y):
    min_numbers = min(x, y)
    divider = 1
    for element in range(2, min_numbers+1):
        if x % element == 0 and y % element == 0:
            divider = element
            break
    return divider == 1

def zadacha3():
    #Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
    for y in range(1, 12):
        for x in range(1, y):
            if check_numbers(x, y):
                print(f'{x}/{y}', end=' ')  
        print()  

zadacha1()  
zadacha2()
zadacha3()  