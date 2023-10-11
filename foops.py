lst2 = [ i+1 for i in range(10)]
eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

'''for item in lst2:
    print(item)

print('-'*50)
print(range(10))
print(list(range(10)))
for i in range(10):
    if i%2==0:
        continue
    print(i)

cats = ["Барсик", "Мурзик", "Василий"]
print(list(enumerate(cats)))        #Возвращает пары индекс/значение
for idx, cat in enumerate(cats):
    print(f"{idx}. {cat}")

print(list(reversed(cats)))         #Фун-ия итератор развёртывания
print(list(sorted(cats)))           #Фун-ия итератор сортировки'''


print('а - ', ord('а'))
symbol_number = ord("а")
while symbol_number <= ord("я"):
    print(symbol_number, chr(symbol_number))
    symbol_number +=1 
