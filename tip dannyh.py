

import random


def random_number():
    number = [0, 0, 0, 0]
    digit1 = random.randint(1, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)
    digit4 = random.randint(1, 9)
    if digit1 != digit2 and digit1 != digit3 and digit1 != digit4 and digit2 != digit3 and digit2 != digit4 and digit3 != digit4:

        number[0] = digit1
        number[1] = digit2
        number[2] = digit3
        number[3] = digit4
        print(number)
        return number
    else:
        random_number()


def user_number():
    user_input = input("Please enter 4 digits number to play ")
    usernumber = [0, 0, 0, 0]
    if len(user_input) == 4 and user_input.isdigit():

        usernumber[0] = user_input[0]
        usernumber[1] = user_input[1]
        usernumber[2] = user_input[2]
        usernumber[3] = user_input[3]
        print(usernumber)
        return usernumber

    else:
        print("****Please enter valid 4 digits number*****")
        user_number()


random_number()
user_number()