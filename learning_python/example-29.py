#In [1]:
class Point:
    pass

#In [2]:
point1 = Point()
point1.x = 1.0
point1.y = 1.0

#In [3]:
point1.hello = lambda x: print('Hello', str(x))
point1.hello('world')

point2 = Point()
#point2.hello('world') #エラー: Pointクラスの定義ではhelloメソッドはない

#In [4]:
class MyClass:
    count = 0 # クラス変数countの定義

#In [5]:
print(MyClass.count)

#In [6]:
instance = MyClass()
print(instance.count)

#In [7]:
instance.count = 100
print(instance.count)
print(MyClass.count)

#In [8]:
class MyClass:
    count = 0

    def __init__(self):
        self.count += 1
        print(f'you made {MyClass.count} instance(s)')

#In [9]:
instance1 = MyClass()
instance2 = MyClass()

#In [10]:
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

#In [11]:
instance1 = MyClass()
instance2 = MyClass()

#In [12]:
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod # クラスメソッドの定義
    def get_count(cls):
        print(cls.count) #クラスの変数には[cls.クラス変数]としてアクセス

#In [13]:
MyClass.get_count()

#In [14]:
instance1 = MyClass()
instance2 = MyClass()
instance2.get_count()

#In [15]: 
class Myclass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

#In [16]:
MyClass.another_get_count()
instance1 = MyClass()
instance1.another_get_count()
instance1.get_count()

#In [17]:
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

    @staticmethod
    def static_get_count():
        print('count:', MyClass.count)

#In [18]:
MyClass.static_get_count()
instance = MyClass()
instance/static_get_count()
