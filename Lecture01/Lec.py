# print('Hello world')

# Типы данных и переменная
# int, float, boolean, str, list, None
# Python - язык с динамической типизацией

# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'Hello world'
# print(s)
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# f = True
# print(f)
# list = ['1', '2', '3', 'hello', 1,2,3,4.5,True]
# print(list)

# Ввод и Ввод Данных
# print() - отвечает за вывод данных
# input() - отвечает за ввод данных с клавиатуры
# print('Введите а')
# a = int(input()) #float дробное число
# print('Введите b')
# b = int(input()) #float
# print(a + b)
# print(f'{a} + {b} = {a+b}')

# Арифметические операции
# +, -, *, /, %, //, **, (), сокращенные операции
# a = 1.33333
# b = 3
# c = round(a * b, 5)
# print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in
# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# Управляющие конструкции: if, if-else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
# else:
#    print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#    print('Ура, это же МАША!')
# elif username == 'Андрей':
#    print('Я так ждал Вас, Андрей')
# elif username == 'Крис':
#    print('Это же я)')
# else:
#    print('Привет, незнакомый ', username)

# Управляющие конструкции: while
# original = 23
# inverted = 0 # переводится как перевернутый
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print("Пожалуй хватит")
# print(inverted)

# Управляющие конструкции: for
# for i in range(1, 10):
#     print(i, end=' ')

# Немного о строках
# text = "съешь еще этих мягких французких булок"
# print(len(text))
# print("еще" in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace("еще", "ЕЩЕ"))
#
# for c in text:
#     print(c, end='')
# text = "Съешь Ещё этИх мягКих фрАнцузкИх булОк"

# print(text[0])
# print(text[1])
# print(text[len(text)-1])
# print(text[len(text)-5])
# print(text[:])
# print(text[2:5])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[0::6])
# text = text[2:9] + text[-5] + text[:2]

# def f(x):  # функция
#    if x == 1:
#        return "Целое"
#    if x == 2.3:
#        return 23
#    else:
#        return

# arg = 1
# print(f(arg))
# print(type(f(arg)))
