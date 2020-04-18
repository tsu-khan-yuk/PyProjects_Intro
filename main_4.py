#####################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 17.04.2020
# -> task 1: Доделайте последнее задание из практики (Искусственный интеллект)
# -> task 2: Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
#   Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
# -> *task 3:  Написать алгоритм перехода через улицу. Ваш робот стоит на одной стороне улицы и должен попасть
#   не другую сторону по пешеходному переходу. Робот может шагать вперед, смотреть по сторонам и вперед.
#    Можно описать как угодно, хоть блок-схемой, хоть текстом, главное понятно. Что такое блок-схема
#   https://uk.wikipedia.org/wiki/%D0%91%D0%BB%D0%BE%D0%BA-%D1%81%D1%85%D0%B5%D0%BC%D0%B0
# -> *task 4: Ввести из консоли строку. Найти в строке самое длинное слово, в котором присутствуют подряд
#   две согласные буквы. Если в строке присутствует слово с тремя согласными буквами подряд - завершить выполнение.
#####################################################################################################################
options = ["1", "2", "3", "4", "all", "quit"]
while True:
    print("+--------------------------------+")
    print("|  Первое задание       |  1     |")
    print("|  Второе задание       |  2     |")
    print("|  Третье задание       |  3     |")
    print("|  Четвертое задание    |  4     |")
    print("|  Все по очереди       |  all   |")
    print("|  Завершение программы |  quit  |")
    print("+--------------------------------+")
    # task = input(">>> Введите режим работы: ")
    task = "1"

    if task == "quit":
        break

    check = True
    for i in options:
        if task == i:
            check = False
            break
    if check:
        print("\nНе понимаю о чем вы, попробойте еще раз)\n")
        continue

    if task == "1" or task == "all":

        # task 1:
        print("\n-> Задание 1:")
        # есть строка, нгадо поределить на что она похожа.
        # В1 - телефон (правило + и 12 цифр),
        # В2 - имейл (правило - @ по средине, имя не менее 3 букв, доменное имя буквы три буквы
        # В3 - имя фамилия (правило - два слова через пробел, каждое с большой буквы)
        st = input().split()
        for word in st:
            if len(word) == 13 and word.startswith('+') and word[1:].isdigit():
                print('Это телефоный номер\n')
            elif '@' in word:
                # должна быть @ по середине
                # должно быть три символа до и после
                # должна быть точка во втором слове
                tmp = word.split('@')
                flag = len(tmp[0]) >= 3 and len(tmp[1]) >= 3
                flag_1 = tmp[0].isalpha()
                flag_2 = tmp[1][tmp[1].find('.')].isalpha()
                flag_3 = len(tmp) == 2
                if tmp[0].isalpha() and tmp[1][tmp[1].find('.')].isalpha() and len(tmp) == 2 and flag:
                    if 0 < tmp[1].find('.') < 3:
                        print("Это имэйл\n")
            elif word[:1].isupper() and len(word) >= 2:
                print("Либо имя, либо фамилия")
            else:
                print("Не понимаючто это")

    if task == "2" or task == "all":
        # task 2:
        print("\n-> Задание 2:")

    if task == "3" or task == "all":
        # task 3:
        print("\n-> Задание 3:")

    if task == "4" or task == "all":
        # task 4:
        print("\n-> Задание 4:")
