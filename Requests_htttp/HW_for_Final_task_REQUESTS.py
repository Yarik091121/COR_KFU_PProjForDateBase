import requests
import socket
from pprint import pprint
from bs4 import BeautifulSoup



def main1():

    host_name = socket.gethostname()

    ip_address = socket.gethostbyname(host_name)

    print(f"You local (input) IP is {ip_address}")  # Computer IP

    response = requests.get("https://icanhazip.com/").text
    print("You internet (output) IP is", response)

    IP = input("Please, input you IP:\n")
    # IP = '24.48.0.1'

    response2 = requests.post(f"http://ip-api.com/json/{IP}")
    # print(response2.status_code)
    try:
        print("Country - ", response2.json()['country'])
        print("Region  - ", response2.json()['regionName'])
        print("City    - ", response2.json()['city'][:-1])
    except KeyError:
        print(response2.json()['status'], '\n', response2.json()['message'])

def main2():
    response = requests.get('https://yandex.ru/pogoda/')


    tree = BeautifulSoup(response.text, 'html.parser')
    print(tree.select('.link_theme_normal'))
    print(tree.select('.temp__value_with-unit'))

    class WeatherInfo:
        def __init__(self, day: str, date: str, temp_day: str, temp_night: str):
            self.day = day
            self.date = date
            self.temp_day = temp_day
            self.temp_night = temp_night

        def __str__(self):
            return f' "{self.day}","{self.date}", "{self.temp_day}" ,"{self.temp_night}".'

    infos = []
    index = 0
    for item in tree.select('.link_theme_normal'):
        day = item.select_one('.forecast-briefly__name').text
        date = item.select_one('.forecast-briefly__date').text
        temp_day = tree.find_all('div', {"class": "temp forecast-briefly__temp forecast-briefly__temp_day"})[index].text
        temp_night = tree.find_all('div', {"class": "temp forecast-briefly__temp forecast-briefly__temp_night"})[
            index].text
        infos.append(WeatherInfo(day, date, temp_day, temp_night))
        index += 1

    for info in infos[1:8]:
        print(info)

def main3():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.933 YaBrowser/23.9.3.933 Yowser/2.5 Safari/537.36"
    }

    url = 'https://yandex.ru/pogoda/kazan?lat=55.791855&lon=49.125229'
    resp = requests.get(url, headers)

    print(resp.text)


if __name__=='__main__':
    #main1()
    #main2()
    main3()