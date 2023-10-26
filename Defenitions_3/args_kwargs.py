from defenitions.translator.data import DICT
from defenitions.translator.service import get_translation


def test(a, b, *args, is_test=True, **kwargs):          # ВАЖНА ПОСЛЕДоВАТЕЛЬНОСТЬ ЭЛЕМЕНТОВ!
    print("Простые аргументы:", a, b)
    print("args", args)
    print("is test", is_test)
    print("kwargs", kwargs)

test(1, 2, 3, 4, 5,
     is_test=False,
     messsage = 'вышел зайка погулять'
     )


def get_word_translation(*args, **kwargs):          #*args - tuples,  **kwargs - dictionary
    print(args)
    print(kwargs)
    local_dict = dict(**DICT, **kwargs)
    lst = [1, 2, 3]
    test_lst = [*args, *lst]
    print(test_lst)
    results = []
    for arg in args:
        results.append(get_translation(arg, local_dict))
    return results

print(get_word_translation('son', 'mother', 'son', 'clock', clock='часы', key='ключ'))