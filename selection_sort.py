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
        max_pos, i, j, j_max = 0, 0, 0, self.n - 1
        while i < j_max:
            min_pos = i
            j = max_pos = j_max
            while i <= j:
                if arr[min_pos] > arr[j]:
                    min_pos = j
                elif arr[max_pos] < arr[j]:
                    max_pos = j
                j -= 1
            if i != min_pos:
                arr[i], arr[min_pos] = arr[min_pos], arr[i]
                if i == max_pos:
                    max_pos = min_pos
            if j_max != max_pos:
                arr[j_max], arr[max_pos] = arr[max_pos], arr[j_max]
            i += 1
            j_max -= 1

    def sorts(self):
        self.mm_sort(self.sort_list, self.n)
