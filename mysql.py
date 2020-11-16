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

#执行各种数据库的读写操作
# sql="select name,age from class1 where sex='m';"
# name=input("name:")
sql="select * from class1 where sex=%s and score>%s;"
cur.execute(sql,["m",85])
# cur.execute(sql)
# 迭代cur获取查询结果
for i in cur:
    print(i)


#关闭游标和数据库链接
cur.close()
db.close()

