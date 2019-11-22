import gevent
from gevent import monkey
monkey.patch_all()# 该剧执行在导入socket前
from socket import  *
def handle(c):
    while True:
        data =c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
#创建套接字

s =socket()

s.bind(('0.0.0.0',8888))
s.listen(5)
while True:
    c,addr = s.accept()
    print("connect from:",addr)
    # handle(c)
    gevent.spawn(handle,c)