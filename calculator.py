__author__ = 'srtoosnye'
# -*- coding: utf-8 -*-


class Expr(object):
    def __int__(self):
        pass
    def SetValue(self):
        self.__value = raw_input('请输入表达式:')
        self.__opt = []
        self.__num = []
    def GetSuffix(self):
        return self.__num
    def HandleString(self):
        def Greater(opt1,opt2):
            if opt1 in ['*','/'] and opt2 in ['+','-']:
                return True
            else:
                return False
        FirstNumPos = 0
        for i in range(len(self.__value)):
            c = self.__value[i]
            if c in ['+','-','*','/']:
                TempNum = self.__value[FirstNumPos:i]
                self.__num.append(TempNum)
                if self.__opt ==[]:
                    self.__opt.append(c)
                else:
                    while (len(self.__opt) > 0) and (not Greater(c,self.__opt[len(self.__opt)-1])):
                        self.__num.append(self.__opt.pop())
                    self.__opt.append(c)
                FirstNumPos = i + 1
            if i == len(self.__value) - 1:
                TempNum = self.__value[FirstNumPos:i+1]
                self.__num.append(TempNum)
        length = len(self.__opt)
        for i in range(length):
            self.__num.append(self.__opt.pop())


def calculate(suffix):
    container = []
    for i in range(len(suffix)):
        if suffix[i] == '+':
            temp = int(container.pop()) + int(container.pop())
        elif suffix[i] == '-':
            temp = - int(container.pop()) + int(container.pop())
        elif suffix[i] == '*':
            temp = int(container.pop()) * int(container.pop())
        elif suffix[i] == '/':
            temp1 = int(container.pop())
            temp2 = int(container.pop())
            temp = temp2 / temp1
        else:
            temp = int(suffix[i])
        container.append(temp)
    print container[0]


obj = Expr()
obj.SetValue()
obj.HandleString()
calculate(obj.GetSuffix())