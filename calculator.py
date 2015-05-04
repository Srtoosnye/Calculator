__author__ = 'srtoosnye'
# -*- coding: utf-8 -*-
import sys


class Expr(object):
    def __init__(self):
        self.__value = raw_input('请输入表达式：')
        self.__opt = []
        self.__num = []

    def check_value(self):
        class MyException(Exception):
            def __init__(self):
                self.__tip = 'Please check your format.'

            def disp_tip(self):
                print self.__tip
        try:
            list1 = ['+', '-', '*', '/', '(']
            list2 = ['+', '-', '*', '/', ')']
            list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            list4 = ['+', '-', '*', '/']
            value = '+' + self.__value + '+'
            for i in range(1, len(self.__value)+1):
                if self.__value[i-1] == '(':
                    if not (value[i-1] in list1 and value[i+1] in list3):
                        raise MyException()
                elif self.__value[i-1] == ')':
                    if not (value[i-1] in list3 and value[i+1] in list2):
                        raise MyException()
                elif self.__value[i-1] in list4:
                    if not (value[i-1] in list3 and value[i+1] in list3 or
                            value[i-1] == ')' and value[i+1] == '('):
                        raise MyException()
        except MyException as e:
            e.disp_tip()
            sys.exit()

    def opt_value(self):
        def greater(opt1, opt2):
            if opt1 in ['*', '/'] and opt2 in ['+', '-']:
                return True
            else:
                return False
        first_num_pos = 0
        for i in range(len(self.__value)):
            c = self.__value[i]
            if c in ['+', '-', '*', '/']:
                temp_num = self.__value[first_num_pos:i]
                self.__num.append(temp_num)
                if not self.__opt:
                    self.__opt.append(c)
                else:
                    while (len(self.__opt) > 0) and (not greater(c, self.__opt[len(self.__opt)-1])):
                        self.__num.append(self.__opt.pop())
                    self.__opt.append(c)
                first_num_pos = i + 1
            if i == len(self.__value) - 1:
                temp_num = self.__value[first_num_pos:i+1]
                self.__num.append(temp_num)
        length = len(self.__opt)
        for i in range(length):
            self.__num.append(self.__opt.pop())

    def get_postfix(self):
        return self.__num


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
            temp = temp2 / temp1
        else:
            temp = int(postfix[i])
        container.append(temp)
    print container[0]


s = Expr()
s.check_value()
s.opt_value()
calculate(s.get_postfix())