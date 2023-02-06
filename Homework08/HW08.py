import random


def zadacha1():
    # Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
    
    group_count = 4
    
    marks = [0] * group_count
    
    for i in range(group_count):
        marks[i] = [random.randint(2, 5) for _ in range(random.randint(20, 30))]
        
        for row in marks:
            print(row)
            
    mark_max = 0
    group_max = 0
    
    for i in range(group_count):
        average_mark = 0
        students_count = len(marks[i])
    for j in range(len(marks[i])):
        average_mark += marks[i][j]
    average_mark /= students_count
    if average_mark > mark_max:
        mark_max = average_mark
        group_max = i + 1
    print(f'Максимальный средний балл у группы {group_max}')

def zadacha2():
    # Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

    rows = 4
    
    numbers = [0] * rows
    
    for i in range(rows):
       numbers[i] = [random.randint(1, 100) for _ in range(rows)]
        
    for row in numbers:
        print(row) 

    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += numbers[i][i]
    print(f'Сумма элементов главной диагонали равна {diagonal_sum}')

    for index in range(len(numbers)):
        sum_in_row = sum(numbers[index])
        if sum_in_row > diagonal_sum:
            print(f'{index + 1}. {row} = {sum_in_row}')

def zadacha3():
    # Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.

    month = [random.randint(18, 32) for _ in range(8)]

    max_temp = 0
    day_max_temp = 1
    min_temp = 1000
    day_min_temp = 1
    period = 3

    for day in month:
        temp_in_









zadacha2()    
