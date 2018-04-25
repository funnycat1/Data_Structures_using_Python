# -*- coding: utf-8 -*-

"""
利用 Stack 判断输入的由 () 括号组成的字符串是否平衡。

例如：
输入字符串 "()()(())"，返回 True
输入字符串 "()()(())))"，返回 False
"""
from stack_class import Stack

def parentheses_check(symbol_string):
    """
    :param symbol_string: 输入字符串
    :return: 平衡--True，不平衡--False
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parentheses_check('(())(())()')) # True
print(parentheses_check('(((()(((()')) # False