__author__ = 'srtoosnye'
import MySQLdb
import random


def link_to_database():
    db = MySQLdb.connect(host='localhost',
                         user='root',
                         passwd='123456',
                         db='calculator')
    return db


def choose_expr(cursor):
    sql = 'SELECT COUNT(*) FROM expression'
    cursor.execute(sql)
    c = cursor.fetchone()[0]
    return random.randint(1, c)


def get_expr(cursor, num):
    sql = "SELECT equation FROM expression WHERE id = '%s'" % num
    cursor.execute(sql)
    expr = cursor.fetchone()[0]
    print expr, '=',
    return expr


def store_result(cursor, result, num):
    sql = "UPDATE expression SET result = '%s' WHERE id = '%s'" % (result, num)
    cursor.execute(sql)