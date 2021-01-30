class Cat:
    def sing(self):
        print('meow')
class Dog:
    def sing(self):
        print('gav')

class Cow:
    def sing(self):
        print('muu')

#cat = Cat()
#dog = Dog()
#cat.sing()
#dog.sing()
chores = [Cat(), Cow(), Dog(), Cat(), Dog(), Dog()]
for i in chores:
    i.sing()