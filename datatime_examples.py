import datetime

#print(datetime.date.today())
#print(datetime.date.today().strftime('%d.%m.%Y'))

#print(datetime.datetime.today().strftime('%d %b %Y \n %H:%M:%S'))

a = datetime.datetime(2022, 9, 27, 12, 34)
print(a.date())
print(a.time())
print(a.strftime('%d.%m.%Y \n %H:%M:%S'))

b = datetime.datetime.strptime("27.09.2022 10:34:00", "%d.%m.%Y %H:%M:%S")
print('Дата из strptime ', b)


c = a + datetime.timedelta(hours=1, minutes=30)
print('a = ', a, '\nc = ', c)