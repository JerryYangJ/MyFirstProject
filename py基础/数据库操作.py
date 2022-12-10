"""
    1.连接对象
        （1）获取连接对象
            connect()函数：
                dsn：    数据源名称，给出该参数表示数据依赖
                user：   用户名
                password:   用户密码
                host:   主机名
                database:   数据库名称
        (2)连接对象的方法
            Connect()函数返回连接对象。使用的方法：
                close():    关闭数据库连接
                commit():   提交事务
                rollback(): 回滚事务
                cursor():   获取游标对象，操作数据库，如执行DML操作，调用存储过程等

    2.游标对象
        cursor()方法：获取游标对象，属性如下：
            description:    数据库列类型和值的描述信息
            rowcount:   回返结果的行数统计信息，如SELECT、UPDATE、CALLPROC等

        游标对象的方法：
            callproc(procname,[,parameters])   调用存储过程，需要数据库支持
            close()     关闭当前游标
            execute(operation[,parameters])     执行数据库操作，SQL语句或者数据库命令
            executemany(operation,seq_of_params)    用于批量操作，如批量更新
            fetchone()      获取查询结果集中的吓一条记录

"""

import cx_Oracle


# 使用cx_Oracle模块连接Oracle数据库
def main1():
    # 建立连接
    conn = cx_Oracle.connect('BISADMIN', 'BISADMIN', '192.168.14.37:1521/rftestdb')

    # 创建游标
    cursor = conn.cursor()

    # 执行SQL==>  select * from IQC_INSPECTION_SLTM t
    sql_str = input('请输入SQL语句：')
    cursor.execute(sql_str)

    # 获取数据
    data = cursor.fetchmany(3)  # fetchone(), fetchmany(), fetchall()
    print(
        '工厂' + '\t' + '\t' + '\t' + '单号' + '\t' + '\t' + '\t' + '常规' + '\t' + '\t' + '\t' + '数字1' + '\t' + '\t' + '\t' + '数字2' + '\t' + '\t' + '\t' + '姓名' + '\t' + '\t' + '\t' + '日期' + '\t' + '\t' + '\t' + '常规')
    for i in data:
        print(i)

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main1()
