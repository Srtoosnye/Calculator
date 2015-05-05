__author__ = 'srtoosnye'
# -*- coding: utf-8 -*-
import Expr
import calculate

s = Expr.Expr()
s.check_value()
s.opt_value()
calculate.calculate(s.get_postfix())
