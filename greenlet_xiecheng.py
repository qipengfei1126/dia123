"""
协程 第三方模块 greenlet

"""
from greenlet import greenlet

def test1():
    print("执行test1")
    gr2.switch()
    print("结束test1")

def test2():
    print("执行test1")
    gr1.switch()
    print("结束test2")

gr1=greenlet(test1)
gr2=greenlet(test2)

gr1.switch()
