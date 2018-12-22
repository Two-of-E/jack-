import time
import threading


def sing():
    for i in range(5): #  子线程
        print("----正在唱------")
        time.sleep(1)



def dance():
    for i in range(5): #  子线程
        print("----正在跳------")
        time.sleep(1)

# main函数里是主线程，各个函数执行子线程，子线程执行，主线程等待
def main():
    t1 = threading.Thread(target = sing)
    t2 = threading.Thread(target = dance)
    t1.start()
    t2.start()
    #主线程进行等待



if __name__ == "__main__":
    main()
