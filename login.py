#-*-coding:utf-8-*8-
import pymysql
def zhuce():
    


db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='1111',
                   database='dict',
                   charset='utf8'
)

cur = db.cursor()






cur.close()
db.close()