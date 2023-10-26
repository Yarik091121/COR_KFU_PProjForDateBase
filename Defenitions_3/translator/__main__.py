from console import get_parameters, print_translation
from data import DICT, REVERS_DICT
from service import prepare_word, get_translation

'''from defenitions.translator import (
    get_parameters,
    print_translation,
    DICT,
    REVERS_DICT,
    prepare_word,
    get_translation
)'''

# Строки менее 80-ти символов!
# Ctrl + Alt + L = форматирование по стандарту PEP8
k = 0
while True:
    word, direction = get_parameters()              #Alt + Enter - импорт нужных функций
    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERS_DICT)
    print_translation(word, translation)
    k += 1
    if k == 2:
        break
