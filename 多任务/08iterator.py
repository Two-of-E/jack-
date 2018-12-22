#具有迭代器，才可以进行for
import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self


    def __next__(self):
    #  防止越界
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num +=1

            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print(next(cla))

for name in classmate:
    print(name)
    time.sleep(1)


