# try:
#     print("hello world")            #SyntaxError - нельзя отловить, т.к. возникает до запуска программы
# except SyntaxError:
#     print("Was SynErr")
import random


# dct = {"a": 1}
# print(dct.get('b'))         #None
# #print(dct['b'])             #KeyError
# try:
#     print(dct['b'])
# except KeyError as e:
#     print("This Is KeYErrOr", e)
#
# try:
#     n1 = int(input())
#     n2 = int(input())
#     print(n1/n2)
# except (ZeroDivisionError, ValueError) as e:
#     print("Input uncorrect dannu", e)
# except BaseException as e:
#     print("Except: ", e)
#     print(type(e))


#                       СВОЁ ИСКЛЮЧЕНИЕ
class AppException(Exception):
    pass


class MyException(AppException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def my_func():
    if random.random()>0.5:
        raise MyException("test")

for i in range(10):
    print(i)
    try:
        my_func()
    except MyException:
        ... #1 specific app exception
    except AppException:
        ... #2 other app exception
    except BaseException:
        ... #3 python exception