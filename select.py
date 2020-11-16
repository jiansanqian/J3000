#-*-coding:utf-8-*8-
"""
select tcp服务
重点代码
私利分析
    1、所有的IO使用select监控
    2、每个io发生时今次那个处理，没有发生时即进入监控状态
    3、每个io不会长期阻塞服务端执行
"""
from socket import *
import os
from select import select

#创建套接字，作为关注的io
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#将关注的IO 放入监控列表
wlisthfiah .main(float (herror))