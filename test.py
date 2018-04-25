# -*- coding: utf-8 -*-

from node_class import Node


a = Node(13)

b = a

c = b

print(a.getData())
print(a.getNext())

print(b.getData())
print(b.getNext())

print(c.getData())
print(c.getNext())

c.setNext(17)

print("\n c.setNext(17) :\n")

print(a.getData())
print(a.getNext())

print(b.getData())
print(b.getNext())

print(c.getData())
print(c.getNext())