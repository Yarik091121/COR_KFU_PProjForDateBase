# Генераторы - хранят состояние и знают как перевести состояние на следующий уровень
def my_generator():
    print('Старт генератора')
    i = 1
    while True:
        print('Итерация генератора', i)
        i += 1
        yield i ** 2

for i in my_generator():
    print('В цикле', i)
    if i>10:
        break

my_generator2 = (i**2 for i in range(100))

print(my_generator2)
print(list(my_generator2))