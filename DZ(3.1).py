class Time:
    def __init__(self):
        self.time = int(input('Enter a number: '))


    def convertor(self):
        days = self.time // 86400
        hours = (self.time % 86400) // 3600
        minutes = (self.time % 3600) // 60
        seconds = (self.time % 60)
        print("Converted time:", days, "Дней,", hours, "Часов,", minutes, "Минут,", "и", seconds, "Секунд.")


time = Time()
time.convertor()