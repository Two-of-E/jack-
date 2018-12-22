# 两个线程同时操作全局变量的问题--资源竞争
# 同步：互斥锁,避免死锁：添加超过时间
import time
import threading


g_num = 0
def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    
    print("--------in test1 g_num=%d-------" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release() 
    print("--------in test2 g_num=%d-------" % g_num)


# 创建没上锁的互斥锁
mutex = threading.Lock()

def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数时 传递什么参数进去
    # arg关键字可以向函数里传入参数（元组）
    t1 = threading.Thread(target = test1, args=(1000000,))
    t2 = threading.Thread(target = test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(4)
    print("--------in main Thread g_num=%d-------" % g_num)


if __name__ == "__main__":
    main()

