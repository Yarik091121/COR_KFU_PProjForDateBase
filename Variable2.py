lst = [1, 2, 3]   #Список
lst.append(4)
lst.remove(3)

print(lst)

print(lst[0])
print(lst[-1])

#lst_console = input("Введите список чисел через пробел: ")
#numbers = lst_console.split(' ')
#print(numbers)


tup = (1, 2, 3)     #tuple - кортеж, аналог неизменяемого списка
#Обычно для указания некоторых настроек и других задач

#Словари
eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

print(eng_rus_dict)
print(eng_rus_dict['cat'])
eng_rus_dict['cat'] = 'Кошка'
print(eng_rus_dict['cat'])

print("car" in eng_rus_dict)
print(eng_rus_dict.values())
print("кот" in eng_rus_dict.values())

print(eng_rus_dict.keys())
print(eng_rus_dict.items())

print(eng_rus_dict.get("brother", '(увы, нет перевода((( )'))
print(eng_rus_dict.get("cat", '(увы, нет перевода((( )'))


#Множества
set_from_lst = set(lst)
set_example = {1, 2, 3}
print(set_from_lst)
print(set_example)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
print(set_example.union({6, 7, 8, 9}))      #union - объединение множеств

print()
print(len(lst))
print(len(eng_rus_dict))