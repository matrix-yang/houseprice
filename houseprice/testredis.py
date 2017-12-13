# -*- coding:UTF-8 -*-
import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)

def clearAll():
    while r.scard('nexturl'):
        print("nexturl remove--->", r.spop("nexturl"))

    while r.scard('preurl'):
        print("preurl remove--->", r.spop("preurl"))

    while r.scard('snexturl'):
        print("snexturl remove--->", r.spop("snexturl"))

    while r.scard('spreurl'):
        print("spreurl remove--->", r.spop("spreurl"))