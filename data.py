__author__ = 'srtoosnye'
import MySQLdb


def link_to_mysql():
    return MySQLdb.connect(host='localhost', user='root', passwd='123456', db='calculator')


def create_table(cursor):
    try:
        cursor.execute("CREATE TABLE expression(equation char(30) PRIMARY KEY, result int(10))")
        cursor.execute("INSERT INTO expression(equation, result) VALUES('1*2+3', 5)")
        cursor.execute("INSERT INTO expression(equation, result) VALUES('1+2+3', 6)")
        cursor.execute("INSERT INTO expression(equation, result) VALUES('1+2*3', 7)")
        print 'New table is created..'
    except:
        print 'Table exists..'


def is_used_data(cursor, expr):
    cursor.execute("SELECT result FROM expression WHERE equation = '%s'" % expr)
    try:
        temp = cursor.fetchone()[0]
        print 'Data exists..'
        print temp
        return 1
    except:
        cursor.execute("INSERT INTO expression(equation) VALUES('%s')" % expr)
        print 'New data is created..'
        return 0


def store_result(cursor, result, expr):
    sql = "UPDATE expression SET result = '%s' WHERE equation = '%s'" % (result, expr)
    cursor.execute(sql)