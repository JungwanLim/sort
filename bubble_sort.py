import time
from baseclass_sort import BaseSorts


class BubbleSort(BaseSorts):
    def bubble_sort(self, arr, size):
        sorted = False
        for i in range(1, size):
            if sorted:
                break
            sorted = True
            for j in range(size - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    sorted = False
                    
    def sorts(self):
        self.bubble_sort(self.sort_list, self.n)


if __name__ == '__main__':
    b_sort = BubbleSort()
    b_sort.fill_list(10000)
    t1 = time.time()
    b_sort.sorts()
    t2 = time.time()
    print(abs(t2 - t1))
    print(b_sort.sort_list[:10])
    print(b_sort.sort_list[b_sort.n - 10:])
          
    t1 = time.time()
    b_sort.sorts()
    t2 = time.time()
    print(abs(t2 - t1))
    print(b_sort.sort_list[:10])
    print(b_sort.sort_list[b_sort.n - 10:])
