# @Time :2022/9/28 17:17
# @Author : Jerry Y
# @File  : SQLAlchmey.py
# @Info  :

'''
数据库链接方式：
    python2:    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    python3:    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

1. 字段类型
类型名	        python中类型	            说明
Integer	        int	                    普通整数，一般是32位
SmallInteger	int	                    取值范围小的整数，一般是16位
BigInteger	    int或long	            不限制精度的整数
Float	        float	                浮点数
Numeric	        decimal.Decimal	        普通整数，一般是32位
String	        str	                    变长字符串
Text	        str	                    变长字符串，对较长或不限长度的字符串做了优化
Unicode	        unicode	                变长Unicode字符串
UnicodeText	    unicode	变               长Unicode字符串，对较长或不限长度的字符串做了优化
Boolean	        bool	                布尔值
Date	        datetime.date	        时间
Time	        datetime.datetime	    日期和时间
LargeBinary	    str	                    二进制文件

2. 常用的SQLAlchemy字段选项
选项名	            说明
primary_key	        如果为True，代表表的主键
unique	            如果为True，代表这列不允许出现重复的值
index	            如果为True，为这列创建索引，提高查询效率
nullable	        如果为True，允许有空值，如果为False，不允许有空值
default	            为这列定义默认值

3. 常用的SQLAlchemy关系选项
选项名	        说明
backref	        在关系的另一模型中添加反向引用
primary join	明确指定两个模型之间使用的联结条件
uselist	        如果为False，不使用列表，而使用标量值
order_by	    指定关系中记录的排序方式
secondary	    指定多对多关系中，另外一个关系表的名字
secondary join	在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件
'''

from sqlalchemy import create_engine, Column, Integer, String, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:jerry123@127.0.0.1:3306/py3_sqlalchemy')
print(engine)

# 创建SQLORM基类
Base = declarative_base()


class User(Base):
    # 对应MySQL中数据表的名字
    __tablename__ = 'users'

    # 创建字段
    id = Column(Integer, primary_key=True)  # users表中的id字段（主键）
    username = Column(String(64), nullable=False, index=True)  # users表中的username字段（有索引）
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)

    # 为调试方便，定义以下__repr__,可以不定义
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)




# # 执行下列代码，创建userinfo表（所有表结构）
# Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类

# 创建session对象
session = DBSession()  # 创建数据库会话（链接）的实例对象

'''------增------'''
# # 创建新的User对象
# new_user = User(id='2', username='python_teacher2', password='123456', email="123456@qq.com")
# new_user1 = User(id='3', username='python_teacher3', password='123123', email="123123@qq.com")
# new_user2 = User(id='4', username='python_teacher4', password='123321', email="123321@qq.com")
# # 添加到session
# session.add_all([new_user, new_user1, new_user2])     # 增加一条数据使用.add(),增加多条数据使用.add_all()
# # 提交保存到数据库
# session.commit()

'''------查------'''
# 获取所有数据
obj = session.query(User).all()
print(obj)   # 是一个User类对象的列表

for temp in obj:
    print("-"*20)
    print(temp.id)
    print(temp.username)
    print(temp.password)
    print(temp.email)

# 按条件查询数据
obj = session.query(User).filter(User.id == 1).one()  # 查询结果为实例对象
print("id=1的数据：")
print(obj.id)
print(obj.username)
print(obj.password)
print(obj.email)
print("-" * 20)

obj = session.query(User).filter(User.id == 4).one()  # 查询结果为实例对象
print("id=5的数据：")
print(obj.id)
print(obj.username)
print(obj.password)
print(obj.email)
print("-" * 20)

# 返回数据的第一行
obj = session.query(User).first()  # 查询结果为实例对象
print("第一条数据：")
print(obj.id)
print(obj.username)
print(obj.password)
print(obj.email)
print("-" * 20)

# 查询id>1的所有名字
obj = session.query(User.username).filter(User.id > 1).all()  # 查询结果是以对象为元素的列表
print("id>1的所有名字：")
for temp in obj:
    print(temp.username)  # 此处只有username字段内容，因为查询中只制定查询username字段。
print("-" * 20)

# 通过索引查询取数
obj = session.query(User.username).all()[1:4]  # 通过索引取出的数据是以元组为元素的列表
print("username索引为1-4的名字：")
for temp in obj:
    print(temp[0])
print("-" * 20)

# 排序 order_by
obj = session.query(User).order_by(User.id).all()  # 是一个User类对象的列表
print("所有数据按id升序排序")
for temp in obj:
    print(temp.id)
    print(temp.username)
    print(temp.password)
    print(temp.email)
    print("-" * 20)

obj = session.query(User).order_by(-User.id).all()  # 是一个User类对象的列表
print("所有数据按id降序排序")
for temp in obj:
    print(temp.id)
    print(temp.username)
    print(temp.password)
    print(temp.email)
    print("-" * 20)

# 非连续范围
obj = session.query(User.username).filter(User.id.in_([1, 3])).all()
print("非连续范围：")
for temp in obj:
    print(temp.username)
print("-" * 20)

# 模糊查询like\%\_
obj = session.query(User.username).filter(User.email.like('%6%')).all()
print("邮箱包含6的用户名：")
for temp in obj:
    print(temp.username)
print("-" * 20)

obj = session.query(User.username).filter(User.password.like('%3__')).all()
print("密码倒数第三位数是3的用户名：")
for temp in obj:
    print(temp.username)
print("-" * 20)

# 查询数量count()
count = session.query(User.username).filter(User.id > 1).count()
print("id>1的数据数量：")
print(count)
print("-" * 20)

# 逻辑与查询and_(需要导入）
obj = session.query(User.username).filter(and_(User.id > 1, User.password.like('%6'))).all()
print("id>1且密码以6结尾的用户名：")
for temp in obj:
    print(temp.username)
print("-" * 20)

# 逻辑或查询or_(需要导入）
obj = session.query(User.username).filter(or_(User.password.like('%6'), User.email.like('%6%'))).all()
print("密码以6结尾或邮箱包含6的用户名：")
for temp in obj:
    print(temp.username)
print("-" * 20)

# 逻辑非查询not_(需要导入）
obj = session.query(User.username).filter(not_(User.password.like('%6'))).all()
print("密码不以6结尾的用户名：")
for temp in obj:
    print(temp.username)
print("-" * 20)

# '''------改------'''
# # 方法一
# user = session.query(User).filter(User.id == 1).one()
# user.username = 'python_teacher1'
# session.commit()
#
# # 方法二
# user = session.query(User).filter(User.id == 1).update({'username':'python_teacher'})
# session.commit()

# '''------删------'''
# user = session.query(User).filter(User.id == 1).one()
# session.delete(user)        # 不能对查询的列表使用delete删除
# session.commit()




# 关闭会话
session.close()
