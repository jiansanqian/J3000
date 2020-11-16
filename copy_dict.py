#-*-coding:utf-8-*8-
"""
创建数据表 dict 使用utf8
创建表 word 分为三个字段
id  word mean
将dict.txt中的所有单词存入到该数据表中
"""

import pymysql


def get_word(line):

    list_line=line.split(" ",1)
    word=list_line[0]
    mean=list_line[1].strip()
    return word,mean

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='1111',
                   database='dict',
                   charset='utf8'
)

cur = db.cursor()
try:
    f=open('dict.txt','r')
    n=0
    while True:
        line=f.readline()
        if not line:
            break
        wd,mn=get_word(line)
        n+=1
        # print(n,wd,mn)
        sql="insert into words (id,word,mean)value(%s,%s,%s);"
        cur.execute(sql,[n,wd,mn])
    f.close()
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

cur.close()
db.close()