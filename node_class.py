# -*- coding: utf-8 -*-

"""
实现一个节点类 -- Node Class

节点有两个属性： data 和 next
data 是当前节点值； next 是下一个节点值

节点有四个方法： getDate, getNext, setData, setNext
getData: 返回当前节点值； getNext: 返回下一个节点值
setData: 设置当前节点值； setNext: 设置下一个节点值
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

"""
temp = Node(93)
print(temp.getData())  # 93
temp.setNext(17)
print(temp.getData())  # 93
print(temp.getNext())  # 17
temp.setNext(177)
print(temp.getData())  # 93
print(temp.getNext())  # 177
"""


