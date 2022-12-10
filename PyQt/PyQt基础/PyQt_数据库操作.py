# @Time :2022/11/3 14:14
# @Author : Jerry Y
# @File  : PyQt_数据库操作.py
# @Info  :

'''
1、数据库驱动类型
PyQt中，QSqlDatabase类用于连接数据库，可以使用数据库驱动与不同的数据库进行交互，一个QSqlDatabase实例代表一次数据库连接。
    可用数据库驱动类型如下：
        QDB2        IBM DB2驱动程序
        QMYSQL      MySQL驱动程序
        QOCI        Oracle调用接口驱动程序
        QODBC       ODBC驱动程序（包括MS SQL Server）
        QPSQL       PostgreSQL驱动程序
        QSQLITE     SQLite3驱动程序
        QSQLITE2    SQLite2驱动程序

2、QSqlDatabase常用方法:
    addDataBase:设置连接数据库的数据库驱动类型
    setDatabaseName：设置所连接的数据库名称
    setHostName：设置数据库所在的主机名称
    setUserName：指定连接的用户名
    setPassword：设置连接对象的密码
    commit：提交事务，如果执行成功返回True。
    rollback：回滚数据库事务
    close：关闭数据库连接

'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # app = QCoreApplication(sys.argv)
    #
    # db = QSqlDatabase.addDatabase('QMYSQL') # 没有驱动文件qsqlmysql.dll
    #
    # db.setHostName('localhost')
    # db.setPort(3306)
    # db.setDatabaseName('mysql')
    # db.setUserName('root')
    # db.setPassword('jerry123')
    # if db.open():
    #     print("open DB success.")
    # sys.exit(app.exec_())

    app = QCoreApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("/home/user/test.db")
    if db.open():
        print("open DB success.")
    sys.exit(app.exec_())
