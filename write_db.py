#-*-coding:utf-8-*8-
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='1111',
                     database='stu',
                     charset='utf8')
#生成游标对象，操作数据库，执行sql语句
cur =db.cursor()

#执行各种数据库的写操作
try:
    #执行增删改等语句
   sql="insert into class1 (name,age,score) values ('Dave',13,79);"
   # sql = "update class1 set sex='m' where name='Emma';"
   cur.execute(sql)
   db.commit()
except Exception as e:
    db.rollback()#事务回滚
    print(e)


#关闭游标和数据库链接
cur.close()
db.close()