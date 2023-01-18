def zadacha1():
#Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи
#6 –> 1 1 2 3 5 8

    N= int(input("Введите число: "))
    count = N
    num_first = 1
    num_second = 1
    data = open("fibonacci.txt", mode= "w", encoding = "utf-8")
    for _ in range(count):
        data.write(str(num_first) + "\n")
        num_first, num_second = num_second, num_first + num_second
    data.close()

def zadacha2():
#В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
#а –> абрикос, авокадо, апельсин, айва.

    data= open("fruits.txt", encoding= "utf-8")
    fruits_list= data.readlines()[0].split(" ")
    data.close()
    print(fruits_list)
    letter = str(input("Введите букву: "))
    for fruit in fruits_list:
        if fruit[0] == letter:
            print(fruit)

def zadacha3():
#Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

    phrase_dictionary = \
        {
            "привет" : "добрый день",
            "как тебя зовут?" : "меня зовут Мини-Ботик",
            "как дела?" : "спасибо, все супер!"
        }
    start_dialogue = True
    while start_dialogue:
        phrase = input("Я: ")
        phrase = phrase.lower()
        if phrase in phrase_dictionary.keys():
            print(f"Бот: {phrase_dictionary[phrase]}")
        else:
            print("Бот: Я тебя не понимаю, скажи что-то другое")
        if phrase == "пока":
            start_dialogue = False


zadacha1()
zadacha2()  
zadacha3()       