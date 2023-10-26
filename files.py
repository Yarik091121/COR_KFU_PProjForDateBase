import os                       #Отвечает за работу с операционкой
from os import path
from pathlib import Path        #Класс, с помощью которого можно создать объект дл яработы с путями
#file = open("foops.py")
#for line in file:
#    print(line.strip())
#file.close()

''''#Менеджер контекста
with open('Variable2.py') as f:
    for lines in f:
        print(lines.strip())'''

# 'x' - открывает на запись, но выдаст исключение, если файла не существовало ранее
#with open('file.txt', 'a+') as file:               #а+ - модификатор на дозапись       rb - бинар формат,    x-открывает без исключения
#    file.write("123")
#    file.seek(0)    #Для перехода в начало файла
#    print(file.read())

cur_path = os.getcwd()                              #Путь до текущей папки
#files_dir = os.path.join(cur_path, 'files')        #join - т.к. слэши в разн направлениях '/' - Linux or Wind-s - '\'
files_dir = Path(cur_path)/"files"
print(cur_path)
print(files_dir)
try:
    #os.mkdir(files_dir)            #Создать папку по указанному пути
    files_dir.mkdir()
except FileExistsError:             #Если папка уже существует
    pass

#file_path = os.path.join(files_dir, 'file.txt')
file_path = files_dir/'file.txt'
with open(file_path, 'a+') as f:            #with file_path.open('a+')  # -дозапись
    f.write('77254654')

#os.remove('name_file')                             #Удаляет файл
#print(os.path.exists("file.txt"))                  #Существует ли файл
print(Path("file.txt").exists())

print('Path to file:\n', file_path)                     #Полный путь до файла вкл сам файл
f_name = path.basename(file_path)
print("File name:\n", path.basename(file_path))         #Название файла
print("Dir name:\n", path.dirname(file_path))           #Название папки
print(path.splitext(f_name))                            #Тип файла (расширение)


print(path.abspath(path.join('..', 'Users', 'user')))           #'..' - чтоб обращаться к папкам на уровень выше


#Переменные окружения
print(os.environ.get(
    "TEST",             #Переменные окружения, обычно капсом
    "default value for environment variable"
    ))