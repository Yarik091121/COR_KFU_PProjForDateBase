lst1 = input().split()

lst2 = [i for i in lst1 if i.isdigit()]

# if len(lst2)<len(lst1):
#     print("В списке есть непонятные символы! -1")
# else:
#     print("Список чётных -", [i for i in lst1 if i % 2 == 0])
#     print("Список нечётных -", [i for i in lst1 if i % 2 == 1])
#     print("Список чисел <0 -", [i for i in lst1 if i<0])

try:
    lst1 = list(map(int, lst1))

    print("Список чётных -", list(filter(lambda x: x % 2 == 0, lst1)))
    print("Список нечётных -", list(filter(lambda x: x % 2 != 0, lst1)))
    b = lambda x: x < 0
    print("Список чисел <0 -", list(filter(b, lst1)))

except ValueError:
    print('-1')
