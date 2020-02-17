#In [2]:
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        pass #とりあえず何もしない

#In [3]:
mystack = MyStack()
mystack.push(0) # スタックに[0]をプッシュ　（リストの末尾に[0]を追加）
mystack.push(1) # スタックに[1]をプッシュ　（リストの末尾に[1]を追加
mystack.push(2) # スタックに[2]をプッシュ　（リストの末尾に[2]を追加)
print(mystack.stack) # MyStackクラスのインスタンスのインスタンス変数の値を表示

#In [4]:
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        result = self.stack[-1] #　末尾の要素を変数に取り出す
        del self.stack[-1] #　リストから要素を削除する
        return result # リスト末尾から取り出したデータを返送する

#In [5]
mystack = MyStack()
mystack.push(0)
mystack.push(1)
print(mystack.pop())
print(mystack.pop())

#In [7]:
#print(mystack.pop())

#In [8]:
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop

#In [9]
mystack = MyStack()
mystack.push(0)
print(mystack.pop())
print(mystack.pop())

#In [10]
class MyQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        result = self.queue[0]
        del self.queue[0]
        return result

#In [11]
myq = MyQueue()
myq.enqueue(0)
myq.enqueue(1)
print(myq.dequeue())
print(myq.dequeue())
print(myq.dequeue())

#In [12]:
mystack = MyStack()
print(str(mystack))
print(repr(mystack))

#In [13]:
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

#In [14]:
mystack = MyStack(1, 2, [3, 4])
print(mystack.stack)

#In [15]:
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'

#In [16]:
mystack = MyStack(1, 2, [3, 4])
print(repr(mystack))
print(mystack)

#In [17]
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)

#In [18]:
mystack = MyStack(1,2,[3,4])
print(repr(mystack))
print(mystack)
#In [19]:
mystack = MyStack()
print(str(mystack))
print(repr(mystack))

#In [20]:
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.styack) +')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)

#In [21]
mystack = MyStack(1,2,[3,4])
for item in mystack:
    print(item)

#In [22]
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return self.stack[key]

# In [22]
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)
    def __getitem__(self, key):
        return self.stack[key]

#In [23]
mystack = MyStack(1,2, [3, 4])
print(mystack[0])
print(mystack[0:2]) #スライスできるか？