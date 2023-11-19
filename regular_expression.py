import re

text = ("Добрый вечер! Меня зовут Василий, моя электронная "
        "почта va-sya_1990@yandex.ru, моя рабочая почта "
        "Vasya@company-2020.com")


result = re.search(r"[\w\d-]+@[\w\-\d]+\.\w+", text, re.MULTILINE)
result2 = re.finditer(r"[\w\d-]+@[\w\-\d]+\.\w+", text, re.MULTILINE)

print(result)
print(result.string)
print(result.group(0))

print('--'*5, 're.finditer', '--'*5)
for item in result2:
    print(item.group(0))

print()

text2 = "03/29/2022"
p = re.sub(r"([0-3]\d)/(\d{2})/(\d{4})", r"\2/\1/\3", text2)
print(p)

result3 = re.search(r"([0-3]\d)/(\d{2})/(\d{4})", text2)
print("month", result3.group(1))
print("day", result3.group(2))
print("year", result3.group(3))