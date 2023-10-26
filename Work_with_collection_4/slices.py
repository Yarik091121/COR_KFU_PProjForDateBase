from functools import reduce


lst = [1, 2, 4]
print(lst[1:])

lst2 = [i for i in range(1, 11)]
print(lst2[1:8:2])
print(lst2[::-1])       #Reverse of list

lst3 = lst2     #Ссылаются на одну память
lst4 = lst2[:]  #Разные ячейки памяти
lst4_2 = [*lst2]
lst2.remove(8)
print('lst2 - ', lst2)
print('lst3 - ', lst3)
print('lst4 - ', lst4)


#       Списковые выражения
lst2_2 = [x*2 for x in lst2 if x<-5 or x>0]
print(lst2_2)


#       lambda function
def a(i):
    return 2*i

b = lambda x: x*2

print('LAMBDA FUNCTION:\na -', a(2), '\nb -', b(2))

lst4_1 = map(a, lst2)
lst4_2 = filter(lambda x: x<4, lst2)
print('lst4_1:', list(lst4_1))           #Ленивая функция, как и range - результат вызывается только когда он необходим
print(list(range(10)))
print('lst4_2:', list(lst4_2))

#lazy function sorted()
print(sorted([5, 2, 1, 6, 7, 2, 4]))
print(list(reversed(sorted([5, 2, 1, 6, 7, 2, 4]))))

test_dict = {"a": 5, "b":3, "d": 8, "c": -1}
print("What about sorted dict?")
print(test_dict)
print(dict(sorted(test_dict.items(), key=lambda x: x[0])))      #Sort by key
print(dict(sorted(test_dict.items(), key=lambda x: x[1])))      #Sort by value


print(reduce(lambda x, y: x + y, lst2))                         #Позволяет из списком извлекать агрегирующий элемент - сумму, макс/мин знач и т.д.
                                #x - накопленное значение, y - текущее значение
