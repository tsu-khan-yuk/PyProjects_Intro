###########################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 12.04.2020
# -> task 1: Используя переменные a и b сформировать строку "First variable is [тут знаение переменной a],
#   second variable is [тут знаение переменной b]. Their sum is [тут их сумма]. Переменные получите с помощью input()
# -> task 2: Попросить ввести из консоли возраст пользователя.
#   если пользователь ничего не ввел (ввел пустую строку) - вывести “не понимаю”
#   если пользователю меньше 7 - вывести “где твои мама и папа?”
#   если пользователю меньше 18 - вывести “мы не продаем сигареты несовершеннолетним”
#   если пользователю больше 65 - вывести “вы в зоне риска”
#   в любом другом случае - вывести “оденьте маску!”
###########################################################################################################

print("Первое задание     | 1")
print("Второе задание     | 2")
print("Два задания разом  | 3")
task = int(input(">>> Введите номер задания: "))

if 1 <= task <= 3:
    # исправление: теперь программа может так же отображать два задания поочередно
    # и в коде нету дублирования
    if task == 1 or task == 3:

        # task 1:
        print("\n-> Задание 1:")
        a = float(input(">>> Введите значение а: "))        # исправление: теперь задание принимает только
        b = float(input(">>> Введите значение b: "))        # тип float для простоты работы программы
        print(f"First variable is {a},second variable is {b}.Their sum is {a + b}")

    if task == 2 or task == 3:

        # task 2:
        print("\n-> Задание 2:")
        age = input(">>> Введите свой возраст: ")
        if (age == "") or (not age.isdigit()):
            print("Не понимаю о чем вы(")
        else:
            age = int(age)
            if age <= 0:                    # исправление: теперь программа учитывает отрицательные значения
                print("Такого не бывает!")
            elif age < 7:
                print("Где твои мама и папа?")
            elif age < 18:
                print("Мы не продаем сигареты несовершеннолетним")
            elif age > 65:
                print("Вы в зоне риска")
            else:
                print("Оденьте маску!")

else:
    print("Нету такого варианта(")