# 进程共享一份代码，每个进程都需要相同的资源
# 进程和线程对比：
#   app的多开是一个进程，里面的多任务是线程。一个进程里至少有一个主线程
# 线程对资源进行分配，可以在不同的进程里调用不同的线程，然后提高效率
# 进程间通信，队列：数据的特性，FIFO。空间复杂度换时间
# 解耦：让不同的进程分别进行下载数据和数据处理

import multiprocessing as mul


def down_from_web(q):
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11,22,33,44]
    
    #向队列中写入数据
    for temp in data:
        q.put(temp)
    print("---下载器已经下载完数据并且存入到队列中---")
        
def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break
    print(waitting_analysis_data)

def main():
    # 创建一个人队列
    q = mul.Queue()

    p1 = mul.Process(target=down_from_web, args=(q,))
    p2 = mul.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()



if __name__ == "__main__":
    main()
