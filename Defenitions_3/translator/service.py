def get_translation(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return None

def prepare_word(word):
    return word.lower().strip()

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