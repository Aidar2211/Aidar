while True:
    try:

        a = float(input("введите 1 чилсо,: "))
        num = input("выберите какой знак будете использовать +, -, /, *, :")
        b = float(input("введите 2 число: "))

        if num == "+":
            c = a + b
            print(c)
        elif num == "-":
            c = a - b
            print(c)
        elif num == "/":
            c = a / b
            print(c)
        elif num == "*":
            c = a * b
            print(c)
        else:
            print("введен неправельный знак")

        d = input("Если хотите продолжить калькулятор нажмите Enter,"
                  "Но если хотите выйти напишите exit: ")
        if d == "exit":
            break

    except ValueError:
        a = float(input("введите 1 чилсо!!!!!!, :"))
        num = input("выберите знак +, -, /, *,: ")
        b = float(input("введите 2 число!!!!,: "))

        if num == "+":
            c = a + b
            print(c)
        elif num == "-":
            c = a - b
            print(c)
        elif num == "/":
            c = a / b
            print(c)
        elif num == "*":
            c = a * b
            print(c)
        else:
            print("введен неправельный знак")

        d = input("Если хотите продолжить калькулятор нажмите Enter,"
                  "Но если хотите выйти напишите exit: ")
        if d == "exit":
            break
