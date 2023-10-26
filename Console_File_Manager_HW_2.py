import os
from pathlib import Path
from pathlib import PurePath
import shutil
pat0 = os.getcwd()              #Чтоб не вылетало за папку старта, для своей же безопасности
pat = os.getcwd()
ls = [0]
print("If you need to out - input \'out\'")
while ls[0]!='out':
    ls = input().split()
    if ls[0] == 'out':
        print("End of program")
        break
    if ls[0] not in ('pwd', 'cd', 'touch', 'cat', 'ls', 'rm'):
        print("Incorrect command, please, try again!")
        continue

    '''if sys.argv[1]=='pwd':              #Вывод путя до файла
        print(pat)
    elif sys.argv[1]=='ls':             #Вывод списка файлов
        for i in os.listdir():
            print(i, end='\t')
    elif sys.argv[1]=='cd':
        if len(sys.argv)>2:
            dir_name = sys.argv[2]'''
    if ls[0]=='pwd':              #Выводит текущий путь
        print(pat)
    elif ls[0]=='ls':             #Выводит список файлов
        for i in os.listdir(pat):
            print(i, end='\t')
        print()
    elif ls[0]=='cd':
        if len(ls)==1:
            if not PurePath(pat).match(pat0):            #Проверка соответствует ли путь шаблону (заранее установленные пределы)
                pat = PurePath(pat).parent
            print(pat)

        elif len(ls)>1:
            if Path(os.path.join(pat, ls[1])).exists():  # Если файл существует, то мы заходим тудым-с
                pat = os.path.join(pat, ls[1])
                print(pat)
            else:  # Если файла не существует
                b = input(f"Create file {ls[1]}? (y/n) ")
                if b == 'y' or b == 'Y':
                    pat = os.path.join(pat, ls[1])
                    os.mkdir(pat)
                    print(pat)
    elif ls[0]=='touch':
        if len(ls)==1:
            print("You didn't enter the name of file")
        elif Path(os.path.join(pat, ls[1])).exists():
            print("This file already exists!")
        else:
            os.mkdir(os.path.join(pat, ls[1]))
            #print(pat)
    elif ls[0]=='cat':
        if len(ls)==1:
            print("You didn't enter the file name")
        elif not Path(os.path.join(pat, ls[1])).exists():
            print("There's no such file")
        else:
            with open(os.path.join(pat, ls[1]), 'r') as file:
                for line in file:
                    print(line.strip())
    elif ls[0]=='rm':
        if len(ls)==1:
            print("You didn't enter the file name")
        elif not Path(os.path.join(pat, ls[1])).exists():
            print("There's no such file")
        else:
            b2 = input(f"Are you sure you want to delete this file - {ls[1]}? (y/n) ") == ('y' or 'Y')
            if b2:
                shutil.rmtree(os.path.join(pat, ls[1]))
