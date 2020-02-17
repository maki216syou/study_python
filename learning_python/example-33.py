class Foo:
    def hello(self):
        print('Hello from Foo')
    def some_method(self):
        local_var = 'local var in hello method'
        print('local namespace:', dir())
        print('global namespace:', globals().keys())

#In [2]
foo = Foo()
foo.some_method()

#In [3]:
class Foo:
    def hello(self):
        print('Hello from Foo')
    def some_method(self):
        print('self namespace:', dir(self))
        print('Foo namespace:', dir(Foo))
        self.hello()

#In [4]:
foo = Foo()
foo.some_value = 'some value'
foo.some_method()

#In [5]
class Foo:
    def hello(self):
        print('Hello from Foo')
    def hello_goodbye(self):
        self.hello()
        print('Goodbye from Foo')
    def show_attr(self):
        print(f'{self.__class__}: {dir(self)}')

class Bar(Foo):
    def hello(self):
        print('Hello from Bar')
    def goodbye(self):
        print('Goodbye from Bar')

#In [6]
foo = Foo()
foo.show_attr()
bar = Bar()
bar.show_attr()

#In [7]:
foo.hello()
bar.hello()

#In [8]:
foo.hello_goodbye()
bar.hello_goodbye()

#In [9]:
class Foo:
    def __init__(self,name):
        self.name = name #_nameはプライベート
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def show_attr(self):
        print(dir(self))

#In [10]
foo = Foo('deep insider')
print(foo.get_name()) # Fooクラスが用意したメソッドを使ってデータを取得
foo.set_name('atmarkit') # Fooクラスが用意したメソッドを使ってデータを書き換え
print(foo._name) # だが、　このようにして直接アクセスもできてしまう

#In [12]:
class Foo:
    def __init__(self, name):
        self.__name = name#__nameはプライベート
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def show_attr(self):
        print(dir(self))

#In [13]
foo = Foo('deep insider')
print(foo.get_name()) # Fooクラスが用意したメソッドを使ってデータを取得
foo.set_name('atmarket') # Fooクラスが用意したメソッドを使ってデータを書き換え
print(foo.__name) # エラーとなる

#In [14]
foo.show_attr()

#In [15]
class Foo:
    def __init__(self):
        self.__mynum = 0
    def get_num(self):
        return self.__mynum
    def set_num(self, new_value):
        if 0 < new_value < 101:
            self.__mynum = new_value
        else:
            raise ValueError('value out of range(0-100)')
    mynum = property(get_num, set_num)

#In [16]:
foo = Foo()
foo.mynum = 50# mynumをインタフェースとして__mynumの値を変更
print(foo.mynum)# mynumをインタフェースとして__mynumの値を取得
foo.mynum = 101# 範囲外なのでエラーとなる