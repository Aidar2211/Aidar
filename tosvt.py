import random

print("Игра началась!")
print("Камень, Ножницы, Бумага")
computer = random.randint(1, 3)
if computer == 1:
    a = "Камень"
elif computer == 2:
    a = "Ножницы"
else:
    a = "Бумага"
print("1 Камень")
print("2 Ножницы")
print("3 Бумага")


def game():
    try:
        n = int(input("Написать номер: "))
        if n == 1:
            print("")
            print("Ваш выбор: Камень")
            print("Выбор соперника: " + str(a))
            print("")
            if computer == 1:
                print("Ничья:")
            elif computer == 2:
                print("Вы победили!")
            else:
                print("Комп победил \n Вы проиграли!")
                print("")
        elif n == 2:
            print("")
            print("Ваш выбор: Ножницы")
            print("Выбор соперника: " + str(a))
            print("")
            if computer == 1:
                print("Победа соперника\n Вы проиграли!")
            elif computer == 2:
                print("Ничья")
            else:
                print("Вы победили!")
                print("")
        elif n == 3:
            print("")
            print("Ваш выбор: бумага")
            print("Выбор соперника " + str(a))
            print("")
            if computer == 1:
                print("Вы победили!")
            elif computer == 2:
                print("Комп победил\n Вы проиграли!")
            else:
                print("Ничья")
            print("")
        else:
            print("Пишите только числа: 1/2/3!")
    except ValueError:
        print("ОШИБКА: записывать только числа!")

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        game()


game()
