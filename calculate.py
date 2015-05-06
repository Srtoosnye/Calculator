__author__ = 'srtoosnye'
# -*- coding: utf-8 -*-
import sys


def calculate(postfix):
    container = []
    for i in range(len(postfix)):
        if postfix[i] == '+':
            temp = int(container.pop()) + int(container.pop())
        elif postfix[i] == '-':
            temp = - int(container.pop()) + int(container.pop())
        elif postfix[i] == '*':
            temp = int(container.pop()) * int(container.pop())
        elif postfix[i] == '/':
            temp1 = int(container.pop())
            temp2 = int(container.pop())
            try:
                temp = temp2 / temp1
            except ZeroDivisionError:
                print 'Zero division error!'
                sys.exit()
        else:
            temp = int(postfix[i])
        container.append(temp)
    print container[0]
    return container[0]
