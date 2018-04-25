# -*- coding: utf-8 -*-

"""
实现一个无序不包含重复元素的列表 -- UnorderList

无序列表有一组节点构成。

List(): 创建一个空列表。不需要参数，返回一个空列表。
add(item): 将 item 添加到列表。需要参数 item，无返回。假设一开始 item 不在列表里。
remove(item): 将 item 从列表里删除。需要参数 item，改变列表，无返回。假设一开始 item 已经在列表里。
search(item): 判断 item 是否在列表里。需要参数 item，返回一个布尔值。
isEmpty(): 判断列表里的元素数量是否为零。不需要参数，返回一个布尔值。
size(): 返回列表里元素的数量。不需要参数，返回一个整数。

借助节点类 -- node_class.py 中的 Node()
"""

from node_class import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp # 列表头是一个节点对象

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head
        # 当 current == None 时，append() 等同 add()
        if current == None:
            return self.add(item)

        while current.getNext() != None:
           current = current.getNext()

        temp.setNext(current.getNext())
        current.setNext(temp)



mylist = UnorderedList()

# mylist.append(2)
#
# print("Length of mylist is %d." % mylist.size())

primes = [2, 3, 5, 7, 11, 13]

for i in primes:
    mylist.add(i)

print("length of mylist is %d." % mylist.size())

i = 0
temp = mylist.head
while i < mylist.size():
    print("%dth element in mylist is %d." % (i+1, temp.getData()))
    temp = temp.getNext()
    i = i + 1

mylist.append(19)
print("\nAfter mylist.append(19), length of mylist is %d." % mylist.size())

i = 0
temp = mylist.head

# while i < mylist.size():
while temp != None:
    print("%dth element in mylist is %d." % (i+1, temp.getData()))
    temp = temp.getNext()
    i = i + 1
