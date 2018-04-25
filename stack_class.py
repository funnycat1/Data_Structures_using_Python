# -*- coding: utf-8 -*-

"""
Stack: 栈，先进后出 LIFO, last-in first-out 。

Stack(): 不需要参数，返回一个空栈。
push(item): 将新元素 item 添加到栈顶。需要参数 item，无返回。
pop(): 删除栈顶的元素。不需要参数，返回被删除的元素。栈被改变。
peek(): 返回栈顶的元素，但不删除它。不需要参数。不改变栈。
isEmpty(): 判断栈中元素的数量是否是空。不需要参数，返回一个布尔值
size(): 返回栈中元素的数量。不需要参数，返回一个整数。

利用 python 内置的 list 创建一个 Stack，规定 list 的最后一个元素视为栈顶 (最右边的元素)。
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1] # self.items[-1] 一样的

    def size(self):
        return len(self.items)

"""
s = Stack()
s.push('x') # ['x']
s.push('y') # ['x', 'y']
s.push('z') # ['x', 'y', 'z']
print(s.peek()) # z
s.pop() # ['x', 'y']
print(s.items) # ['x', 'y']
"""