from ctypes import *  # 调用c时用到
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary("./lib02_gil.so")


#创建一个子线程，调用c语言的函数
t = Thread(target=lib.DeadLoop)
t.start()

#主线程
while True:
    pass

