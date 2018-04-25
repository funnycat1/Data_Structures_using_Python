# -*- coding: utf-8 -*-

"""
利用节点类 node_class 实现一个有序不重复的列表 -- OrderedList
有序是指元素由小到大排列。

OrderedList(): 创造一个新的空有序列表。不需要参数，返回空有序列表。
add(item):  将 item 添加到列表中并保留他的序号。
remove(item): 从列表中删除 item 。需要参数 item，改变列表，无返回。
search(item): 判断 item 是否在列表里。需要参数 item，返回一个布尔值。
isEmpty(): 判断列表里的元素数量是否为零。不需要参数，返回一个布尔值。
size(): 返回列表里元素的数量。不需要参数，返回一个整数。
index(item): 返回 item 在列表里的位置。需要参数 item，返回 item 位置索引。
pop(): 删除并返回列表最后一个元素。不需要参数，返回列表最后一个元素。
pop(index): 删除并返回列表位置索引 index 上的元素。需要参数位置索引 index，返回该位置上的元素 item。
"""

from node_class import Node

class OrderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                fount = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == Node:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
