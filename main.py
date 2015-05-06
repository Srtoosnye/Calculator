__author__ = 'srtoosnye'
# -*- coding: utf-8 -*-
from Expr import Expr
from calculate import calculate
import data
import sys

conn = data.link_to_mysql()
cursor = conn.cursor()
data.create_table(cursor)
expr = raw_input('请输入表达式：')
if data.is_used_data(cursor, expr):
    sys.exit()

s = Expr(expr)
s.check_value()
s.opt_value()

data.store_result(cursor, calculate(s.get_postfix()), expr)
conn.commit()
conn.close()