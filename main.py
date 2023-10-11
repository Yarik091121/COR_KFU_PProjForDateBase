'''name = input("Введите имя: ")
print('Hello ' + name + '!')'''

name = input("Введите имя: ")
age = float(input("Введите  возраст: "))
is_working_now = input("Работает сейчас? (1 или 0) - ") == "1"
if is_working_now:
    workplace = input('Мксто рвботы: ')

print("Имя: " + name)
print("Возраст: " + str(age))
print("Работает сейчас: " + str(is_working_now))
if is_working_now:
    print("Место работы: " + workplace)

#Шаблонный тип
str_template = "Информация о пользователе: {0} - {1}"   #При прямом порядке можно цифры не писать
print(str_template.format(name, age))

print(name.upper())
print(name.lower())

print(name.find("а"))   #Поиск символа строки
print(name.replace('я', 'ан'))