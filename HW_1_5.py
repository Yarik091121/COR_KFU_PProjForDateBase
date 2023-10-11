count = True
memory_dict = {"+": [], "-": [], "/": [], "*": []}
while count:
    a = input()
    b = input()
    sign = input()

    if sign not in {'+', '-', '/', '*'}:
        print("Неопознанный знак, попробуйте ещё раз")
    elif sign == '+':
        c = float(a)+float(b)
    elif sign == '-':
        c = float(a)-float(b)
    elif sign == '/':
        if(float(b)==0):
            print("На 0 делить нельзя, введите другие значения!")
            continue
        else:
            c = float(a)/float(b)
    else:
        c = float(a)*float(b)

    memory_dict[sign] += [f'{a}{sign}{b}={c:.5}']

    for key, val in memory_dict.items():
        print(f"{key} {val}")

    count = input("Хотите ли ввести ещё операции? (1 - yes, 0 - no) ") == "1"