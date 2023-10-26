def find_max(*args):
    if len(args)==0:
        a = "Max искать не из чего, грустно :("
        return a
    m = args[0]
    for i in range(1, len(args)):
        if m<args[i]:
            m = args[i]
    return m

print(find_max())