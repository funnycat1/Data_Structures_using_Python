# -*- coding: utf-8 -*-

"""
Deque: 双端队列，double-ended queue
元素可以添加到前端（front）或后端（rear），也可以从前后两端删除。

Deque(): 创建一个双端队列。不需要参数，返回一个空的双端队列。
addFront(item): 将 item 添加到队列前端。需要参数 item，无返回。
addRear(item): 将 item 添加到队列后端。需要参数 item，无返回。
removeFront(): 删除队列前端的元素。不需要参数，返回被删除的元素。
removeRear(): 删除队列后端的元素。不需要参数，返回被删除的元素。
isEmpty(): 判断队列中的元素数量是否为零。不需要参数，返回布尔值。
size(): 返回队列中的元素数量。不需要参数，返回整数。

利用 python 内置 list 创建 Deque，
list 的第一个元素位置是后端，rear
list 的最后一个元素位置是前端，front
"""

class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()
d.addFront(4) # [4]
d.addRear('x') # ['x', 4]
print(d.isEmpty()) # False
d.addFront('y')
print(d.items) # ['x', 4, 'y']
print(d.removeRear()) # x
print(d.items) # [4, 'y']
print(d.size()) # 2

