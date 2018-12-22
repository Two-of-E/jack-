# 全局变量不改变指向的内存地址就不用加 global
import time
import threading


g_num = 100
g_nums = [11,22]
def test1():
    global g_num
    g_num += 1
    print("--------in test1 g_num=%d-------" % g_num)



def test2():
    print("--------in test2 g_num=%d-------" % g_num)



def test3(temp):
    temp.append(33)
    print("--------in test3 temp=%s-------" % str(temp))


def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数时 传递什么参数进去
    t1 = threading.Thread(target = test1)
    t2 = threading.Thread(target = test2)
    # arg关键字可以向函数里传入参数（元组）
    t3 = threading.Thread(target = test3, args=(g_nums,))
    
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    
    t3.start()
    time.sleep(1)
    print("--------in main Thread g_num=%d-------" % g_num)


if __name__ == "__main__":
    main()

