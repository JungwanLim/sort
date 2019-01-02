import time
from baseclass_sort import BaseSorts
from bubble_sort import BubbleSort


class SelectionSort(BaseSorts):
    def s_sort(self, arr, size):
        for i in range(size - 1):
            pos = i
            for j in range(i + 1, size):
                if arr[pos] > arr[j]:
                    pos = j
            if i != pos:
                arr[i], arr[pos] = arr[pos], arr[i]

    def sorts(self):
        self.s_sort(self.sort_list, self.n)


class MinMaxSort(BaseSorts):
    def mm_sort(self, arr, size):
        min_pos, first, max_pos, last = 0, 0, 0, size - 1
        while first < last:
            min_pos = max_pos = first
            for j in range(first, last + 1):
                if arr[min_pos] > arr[j]:
                    min_pos = j
                elif arr[max_pos] < arr[j]:
                    max_pos = j
            arr[first], arr[min_pos] = arr[min_pos], arr[first]
            if first == max_pos:
                max_pos = min_pos
            arr[last], arr[max_pos] = arr[max_pos], arr[last]
            first += 1
            last -= 1

    def sorts(self):
        self.mm_sort(self.sort_list, self.n)
