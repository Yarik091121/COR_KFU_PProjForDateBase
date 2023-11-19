import requests
import bs4

search = 'requests'
response = requests.get(f"https://pypi.org/search/?q={search}&0=") #{search} - типо так осуществляется поиск по сайту
print(response.status_code)

tree = bs4.BeautifulSoup(response.text, 'html.parser')        #(текст ответа с html кодом,  'тут что будем разбирать')
#print(tree)
#tree.select('.package-snippet')     #. - условное обозначение класса
for item in tree.select('.package-snippet'):        #item - html
    name_tag = item.select_one('.package-snippet__name')            #.select_one - потому что в верхнем пакете только один такой класс, такое имя
    name = name_tag.text                                            # pull (тянуть) name - вытягиваем имя из оставшегося куска кода
    version = item.select_one('.package-snippet__version').text     #Вытянули версию
    link = item.attrs['href']      #attrs - словарь с атрибутами, которые могут быть у тега         ||   ссылка получается относительная
    print(name, version, f"https://pypi.org{link}")


print(tree.select_one("#content").text[:10])                 #Извлекаем информацию по id => #<id>

print(tree.select("img"))           #Если хотим вытащить все изображения на сайте, в нашем случае img
                                    # А выдало список с картинками :(

# a = input().split()
# s = [int(i) for i in a]
# print(s)
# # for index, i in enumerate(s):
# #     if i>0:
# #         s[index]=i%3
#
# # j=0
# # while j<len(s):
# #     if s[j]<0:
# #         s.remove(s[j])
# #         continue
# #     j+=1
#
# s = [i%3 for i in s if i>=0]
#
# print(s)