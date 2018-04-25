# -*- coding: utf-8 -*-

"""
Queue: 队列，先进先出 FIFO, first-in first-out 。

Queue(): 创建一个空队列。不需要参数，返回一个空队列。
enqueue(item): 将元素 item 添加到队列的后端。需要参数 item，无返回。队列被改变。
dequeue(): 删除队列前端的元素。不需要参数，返回被删除的元素。队列被改变。
isEmpty(): 判断队列中的元素数量是否是空。不需要参数，返回一个布尔值。
size(): 返回队列中元素的个数。不需要参数，返回一个整数。

利用 python 内置的 list 创建 Queue，
规定 list 的第一个元素（左端）的位置是 Queue 的后端，
规定 list 的最后一个元素（右端）的位置是 Queue 的前端，
"""

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # 将 item 插入到 list 的第一个位置
        return self.items.insert(0, item)

    def dequeue(self):
        # 删除 list 的最后一个元素
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('a')
print(q.items) # ['a']
q.enqueue('x')
q.enqueue('y')
print(q.size()) # 3
print(q.dequeue()) # a
print(q.items) # ['y', 'x']

