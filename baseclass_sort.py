from abc import *
import random


class BaseSorts(metaclass=ABCMeta):
    n = 0
    sort_list = []
    temp_list = []

    def print_list(self, arr, sort_name):
        print(sort_name, 'Data 개수 : {}'.format(self.n) )
        if self.n <= 30:
            print(arr)
        else:
            print(arr[:10])
            print(arr[self.n - 10:])

    def copy_list(self, dst, src):
        for x in range(self.n):
            dst[x] = src[x]

    def fill_list(self, n):
        if self.n > 0:
            self.sort_list.clear()
            self.temp_list.clear()
        BaseSorts.n = n
        for x in range(n):
            self.sort_list.append(random.randrange(1, n * 2))
        for x in self.sort_list:
            self.temp_list.append(x)

    @abstractmethod
    def sorts(self):
        pass
