import random

print("Игра началась!")
print("Камень, Ножницы, Бумага")
aa = random.randint(1, 3)
if aa == 1:
    a = "Камень"
elif aa == 2:
    a = "Ножницы"
else:
    a = "Бумага"
print("1 Камень")
print("2 Ножницы")
print("3 Бумага")
try:
    n = int(input("Написат номер: "))
    if n == 1:
        print("")
        print("Ваш выбор: Камень")
        print("Выбор соперника: " + str(a))
        print("")
        if aa == 1:
            print("Ничья:")
        elif aa == 2:
            print("Вы победили!")
        else:
            print("Комп победил \n Вы проиграли!")
            print("")
    elif n == 2:
        print("")
        print("Ваш выбор: Ножницы")
        print("Выбор соперника: " + str(a))
        print("")
        if aa == 1:
            print("Победа соперника\n Вы проиграли!")
        elif aa == 2:
            print("Ничья")
        else:
            print("Вы победили!")
            print("")
    elif n == 3:
        print("")
        print("Ваш выбор: бумага")
        print("Выбор соперника " + str(a))
        print("")
        if aa == 1:
            print("Вы победили!")
        elif aa == 2:
            print("Комп победил\n Вы проиграли!")
        else:
            print("Ничья")
        print("")
    else:
        print("Пишите только числа: 1/2/3!")
except ValueError:
    print("ОШИБКА: записывать только числа!")
