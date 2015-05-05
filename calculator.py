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

            def dis_tip(self):
                print self.__tip
                sys.exit()

        def is_bracket_match(ss):
            bracket = []
            for ch in ss:
                if ch == '(':
                    bracket.append(ch)
                elif ch == ')':
                    bracket.pop()
            if bracket:
                return False
            else:
                return True

        try:
            list1 = ['+', '-', '*', '/']
            list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            value = '+' + self.__value + '+'
            for i in range(1, len(self.__value)+1):
                if self.__value[i-1] == '(':
                    if not (value[i-1] in list1 + ['('] and value[i+1] in list2 + ['(']):
                        raise MyException()
                elif self.__value[i-1] == ')':
                    if not (value[i-1] in list2 + [')'] and value[i+1] in list1 + [')']):
                        raise MyException()
                elif self.__value[i-1] in list1:
                    if not (value[i-1] in list2 and value[i+1] in list2 or
                            value[i-1] == ')' and value[i+1] in list2 or
                            value[i-1] in list2 and value[i+1] == '(' or
                            value[i-1] == ')' and value[i+1] == '('):
                        raise MyException()
            if not is_bracket_match(value):
                raise MyException()

        except MyException as e:
            e.dis_tip()

    def opt_value(self):
        def greater(opt1, opt2):
            if opt1 in ['*', '/'] and opt2 in ['+', '-'] or opt2 == '(':
                return True
            else:
                return False

        def get_bracket(ss):
            if ss[0] == '(':
                for ch in ss:
                    if ch != '(':
                        return ss[0:ss.index(ch)]
            elif ss[len(ss)-1] == ')':
                for ch in ss:
                    if ch == ')':
                        return ss[ss.index(ch):len(ss)]
            else:
                return ''

        self.__value += '+'
        first_num_pos = 0
        for i in range(len(self.__value)):
            c = self.__value[i]
            if c in ['+', '-', '*', '/']:
                temp_s = self.__value[first_num_pos:i]
                temp_bracket = get_bracket(temp_s)
                temp_num = temp_s.replace(temp_bracket, '')
                self.__num.append(temp_num)
                if temp_bracket:
                    if temp_bracket[0] == '(':
                        for j in temp_bracket:
                            self.__opt.append(j)
                    else:
                        for j in temp_bracket:
                            while self.__opt[len(self.__opt)-1] != '(':
                                self.__num.append(self.__opt.pop())
                            self.__opt.pop()
                    self.__opt.append(c)
                else:
                    if (not self.__opt) or self.__opt[len(self.__opt)-1] == '(':
                        self.__opt.append(c)
                    else:
                        while (len(self.__opt) > 0) and (not greater(c, self.__opt[len(self.__opt)-1])):
                            self.__num.append(self.__opt.pop())
                        self.__opt.append(c)
                first_num_pos = i + 1
            if i == len(self.__value) - 1:
                self.__opt.pop()
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