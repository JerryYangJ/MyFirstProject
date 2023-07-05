# @Time :2022/9/28 17:17
# @Author : Jerry Y
# @File  : SQLAlchmey.py
# @Info  :


from sqlalchemy import create_engine, Column, Integer, String, and_, or_, not_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://root:jerry123@127.0.0.1:3306/py3_sqlalchemy')

# 创建SQLORM基类
Base = declarative_base()


class Parent(Base):
    # 对应MySQL中数据表的名字
    __tablename__ = 'parent_table'

    # 创建字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    # 可以通过parent_table表查child_table,数据库中不会创建children字段,只是建立联系
    # 参数backref相当于给类Child类添加了一个属性，在查询的时候可以通过Child.parents属性获取child_table表关联的所有parent_table表
    childrens = relationship('Child', backref='parents')


class Child(Base):
    __tablename__ = 'child_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    parent_id = Column(Integer, ForeignKey('parent_table.id'))


# # 执行下列代码，创建userinfo表（所有表结构）
# Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类

# 创建session对象
session = DBSession()  # 创建数据库会话（链接）的实例对象

# 使用试了对象的相关方法操作数据库
# # 1，添加数据
# p = Parent(name="曹操")
# c1 = Child(name="曹丕", age=10, parents=p)
# c2 = Child(name="曹植", age=11, parents=p)
# c3 = Child(name="曹彰", age=12, parents=p)
# c4 = Child(name="曹昂", age=13, parents=p)
# c5 = Child(name="曹冲", age=14, parents=p)
#
# session.add_all([p, c1, c2, c3, c4, c5])
# session.commit()

# 2.查询数据
obj = session.query(Parent).filter(Parent.id == 1).one()
print(obj.childrens)
# 通过对象属性children,查出找个对象的所有关联age的字段值
for temp in obj.childrens:
    print(temp.name, temp.age)

obj = session.query(Child).filter(Child.id == 2).one()
# 打印对象中的关联属性
print(obj.parents.name)
print("-"*20)

# 内关联查询Parent.id == Child.parent_id的结果
obj = session.query(Parent).join(Child).filter(Parent.id == Child.parent_id).all()  # 结果是Parentd对象列表
for temp in obj:
    print(type(temp))
    print(temp.name)
print("-"*20)

# 内关联查询Parent.id == Child.parent_id的结果
obj = session.query(Child).join(Parent).filter(Parent.id == Child.parent_id).all()  # 结果是Child对象列表
for temp in obj:
    print(type(temp))
    print(temp.name, temp.age)
print("-"*20)

# 内关联查询Parent.id == Child.parent_id的结果
obj = session.query(Parent, Child).join(Child).filter(Parent.id == Child.parent_id).all()   # 结果是（Parent, Child)对象元组为元素是列表
for temp1, temp2 in obj:
    print(temp1.name, temp2.name, temp2.age)
print("-"*20)

# 关闭会话
session.close()
