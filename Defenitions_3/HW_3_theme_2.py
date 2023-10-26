def decorator(func):
    def wrap(*args, **kwargs):
        if kwargs and args:
            print("Input before function:", args, '\n', kwargs)
        elif args:
            print("Input before function:", args)
        else:
            print("Input before function:", kwargs)

        z = func(*args, **kwargs)
        print("Output after function: ", z)
    return wrap


@decorator
def sortin_h_lst(*agrs):
    lst = []
    for _ in agrs:
        lst.append(_)
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j]>lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst




#sortin_h_lst(25, 13, 5454, 78, 135, 0.22)

'''dct = {
    "tar": 32,
    "tatar": 128,
    "key": 45
}

def pr(**kwargs):
    print(kwargs)

pr(ll=546, fgj=475)'''