import filecmp                      #Для сравнения файлов
from pathlib import Path

files_dir = Path("files")

result = filecmp.cmp(
    files_dir / 'file.txt',
    files_dir / 'file2.txt'
)                                   #Сравнивает 2 файла
print(result)

result2 = filecmp.cmpfiles(
    "files", "files2", ['file2.txt', 'file.txt', 'imposter_file.txt']
)                                   #Сравнивает 2 папки с файлами, и смотрит в них папки с именем в 3-м аргументе
match, mismatch, errors = result2       #[Совпадение, разница, ошибки]
#print(result2)
print(match, mismatch, errors)

'''import shutil                    #Для работы с консолью  (Shell Utilitis)
import os

#os.rmdir("files")                  #Не удалит папку с файлами внутри
#shutil.rmtree("files2")            #Удалит папку "files2"

#shutil.copytree('files', 'files2')  #Копирует папку 1 с названием во втором аргументе

print(shutil.disk_usage('.'))'''        #Показывает использование дискового пространства в байтах

import tempfile
import zipfile

with tempfile.NamedTemporaryFile(suffix = '.zip') as temp_file:     #Папка с временными файлами, удаляются автоматически системой
    print(temp_file.name)
    with zipfile.ZipFile(temp_file.name, 'w') as zipfile:
        zipfile.write(files_dir / 'file.txt', 'file.txt')
        zipfile.write(files_dir / 'file2.txt', 'file2.txt')