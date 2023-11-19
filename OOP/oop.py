import random


class Animal():
    _count = 0                                  # Типо protected чтоб извне к ней не обратились
    force = 1
    def __init__(self, name, weight, color):
        self.__name = name                      # __ <=> Переменная теперь приватная, извне доступа нет
        self.weight = weight
        self.color = color
        self.fullness = 0
        Animal._count += 1

    def eat(self, fullness=1):
        print(f"{self.__name} поел!")
        self.fullness += fullness

    def __str__(self):                      #Чтоб возвращало не ссылку на объект (экземпляр класса), а это сообщение
        return f'Животное {self.__name}'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name=name

    def say(self):
        print(f'{self.__name} говорит!')

    @staticmethod
    def get_count():             #статический метод - без создания объекта
        return Cat._count

    def __add__(self, other):
        if self.force>other.force:
            winner_name = self.get_name()
        elif self.force<other.force:
            winner_name = other.get_name()
        else:
            selected = random.choice([self, other])
            winner_name = selected.get_name()
        print('win', winner_name)


class Cat(Animal):                  #Класс CAT наследуется от класса ANIMAL
    force = 2
    def __str__(self):                                  # Чтоб возвращало не ссылку на объект (экземпляр класса), а это сообщение
        return f'Кот {self.get_name()   } (this is __str__ def)'

    def say(self):
        print(f'{self.get_name()}: мяу!')

    def mur(self):
        print(f'{self.get_name()}: мур!')



vasya = Cat("Вася", 5, "black")
barsik = Cat("Барсик", 8, "ginger")

#print(vasya.name,'-', vasya.color)
#print(barsik.name, '-', barsik.color, ' -- ', barsik.fullness)
barsik.eat()
barsik.eat(5)
print(barsik.get_name(), barsik.fullness)

print()
print(barsik)

print(vasya)
vasya.set_name("Вася великолепный")
print(vasya)

vasya._Animal__name="Вася"                  #А тут как нарушить инкапсуляционное соглашение :)   _class(father_class) + private_value
#print(vasya.get_name())

print(Cat.get_count())


parrot = Animal("Popugai", 3.2, "red")
print(parrot)

vasya.say()                         #Полиморфизм - изменяем поведение с учётом особенностей текущего класса,
vasya.mur()                         # но его использовние никак не меняется - ничего нового не добавляется
parrot.say()
print()

print('--'*8, 'Who is win?', '--'*8)
print(vasya + barsik)
print('--'*8, 'Who is win?', '--'*8)
print(parrot + vasya)

print()


class Device():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
class Phone(Device):
    def __init__(self, name):
        self.name=name
    def make_a_call(self, phone_number):
        print("Звоним на", phone_number)
    def take_a_photo(self):                             #Полиморфизм
        print(f"{self.name} фотография!")


class PhotoCamera(Device):
    def take_video(self):
        print("Записывает видео")
    def take_a_photo(self):                             #Полиморфизм
        print(f"{self.name} фотография!")

objs = [Phone("samsung"), PhotoCamera("canon")]

for obj in objs:
    obj.take_a_photo()