

class Vector():
    def __init__(self, *args):
        self.__args = []
        for i in range(len(args)):
            self.__args+= [args[i]]

    def __str__(self):
        return f'{self.__args}'

    def _get_args(self):
        return [self.__args[i] for i in range(len(self.__args))]

    def __add__(self, other):
        if len(self.__args) == len(other.__args):
            dis_vec = [self._get_args()[i] + other._get_args()[i] for i in range(len(self.__args))]
            return Vector(*dis_vec)
        else:
            return print("Векторы разной длины!")

    def __sub__(self, other):
        if len(self.__args) == len(other.__args):
            dis_vec = [self._get_args()[i] - other._get_args()[i] for i in range(len(self.__args))]
            return Vector(*dis_vec)
        else:
            return print("Векторы разной длины!")

    def __mul__(self, other):
        return Vector(*[i*other for i in self.__args])

class Vector2():
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def __add__(self, other):
        x = self.get_x()+other.get_x()
        y = self.get_y()+other.get_y()
        return Vector2(x, y)

    def __sub__(self, other):
        x = self.get_x()-other.get_x()
        y = self.get_y()-other.get_y()
        return Vector2(x, y)

    def __mul__(self, other):
        x, y = self.get_x()*other, self.get_y()*other
        return Vector2(x, y)

    def __str__(self):
        return f'({self.__x}, {self.__y})'

if __name__ == '__main__':
    a = Vector2(9, 30)
    b = Vector2(8, 12)
    c = a+b-b*2
    print('a = ', a)
    print('b = ', b)
    print('a+b = ', a+b)
    print('a-b = ', a-b)
    print('a*2 = ', a*2)
    print('c = ', c)

    t1 = Vector(2, 5, 4, 2)
    t2 = Vector(1, 8, 5, 2)
    print('t1 =', t1)
    print('t2 =', t2)
    #print(t1.get_args())
    print(t1+t2)
    print(t1-t2)
    print(t1*10)