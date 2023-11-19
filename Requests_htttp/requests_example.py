import requests
from pprint import pprint       #Чтоб красиво словарь печатать


response = requests.get('https://python.org')

print(response.status_code)
text = 'Python'
print(text in response.text)

response2 = requests.post(
    "https://postman-echo.com/post",
    data = {                            #Данные которые передаём
        'a': 'test',
        'b': 2
    }
)
print(response2.status_code)
pprint(response2.json())                 #json - формат передачи данных, функция для его раскодирования в тип dict


