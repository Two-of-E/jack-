import time

def sing():
    for i in range(5):
        print("----正在唱------")
        time.sleep(1)



def dance():
    for i in range(5):
        print("----正在跳------")
        time.sleep(1)


def main():
    sing()
    dance()



    t1 = threading.Thread(target = sing)
    main()
