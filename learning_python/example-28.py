#In [1]:
print(type('a'))

#In [2]:
class Point:
    pass

#In [3]:
point1 = Point()
print(type(point1))

#In [4]:
print(dir(point1))

#In [5]:
point1.x = 1.0
point1.y = 1.0

#In [6]:
print(dir(point1))

#In [8]:
class Point:
    def__init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
#In [9]:
point1 = Point(1.0, 1.0)
point2 = Point()
print(f'point1: ({point1.x}, ({point1.y})')
print(f'point2: ({point2.x}, ({point2.y})')

#In [10]:
from math import sqrt
print(sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2))

#In [11]:
from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def difference(self, point=None):
        if not point:
            point = Point()  # 原点を表すPointクラスのインスタンスを生成
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

#In [12]
point1 = Point(1.0, 1.0)
point2 = Point()
point3 = Point(5, 4)

print(point1.difference(point2))
print(point1.difference())
print(point3.difference(point1))
