import time
from baseclass_sort import BaseSorts
from bubble_sort import BubbleSort
from selection_sort import SelectionSort, MinMaxSort


# half swap sort
class HalfSwapInsertionSort(BaseSorts):
    def half_swap_sort(self, arr, size):
        for i in range(1, size):
            j = i
            value = arr[j]
            while j > 0:
                if value < arr[j - 1]:
                    arr[j] = arr[j - 1]
                else:
                    break
                j -= 1
            arr[j] = value

    def sorts(self):
        self.half_swap_sort(self.sort_list, self.n)


class FullSwapInsertionSort(BaseSorts):
    def full_swap_sort(self, arr, size):
        for i in range(1, size):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break

    def sorts(self):
        self.full_swap_sort(self.sort_list, self.n)


class ShellSort(BaseSorts):
    def insertion_sort(self, arr, size, n, h):
        for i in range(n + h, size, h):
            j = i
            value = arr[j]
            while j > n:
                if value < arr[j - h]:
                    arr[j] = arr[j - h]
                else:
                    break
                j -= h
            arr[j] = value

    def shell_sort(self, arr, size):
        h = self.n // 3 + 1
        while h > 1:
            for i in range(h):
                self.insertion_sort(arr, size, i, h)
            h = h // 3 + 1
        self.insertion_sort(arr, size, 0, 1)

    def sorts(self):
        self.shell_sort(self.sort_list, self.n)


class SystemSort(BaseSorts):
    def sorts(self):
        BaseSorts.sort_list.sort()


def main(sort_type, s):
    print('{:=^60}'.format(s))
    sort_type.print_list(BaseSorts.sort_list, '<before sort>')

    t1 = time.time()
    sort_type.sorts()
    t2 = time.time()

    print()
    sort_type.print_list(BaseSorts.sort_list, '<after sort>')
    print('{}time = %.3f'.format(s) % abs(t2 - t1))

    sort_type.copy_list(BaseSorts.sort_list, BaseSorts.temp_list)
    print()


"""
if __name__ == "__main__":
    s_sort = SelectionSort()
    m_sort = MinMaxSort()
    b_sort = BubbleSort()
    h_sort = HalfSwapInsertionSort()
    f_sort = FullSwapInsertionSort()
    sh_sort = ShellSort()
    sys_sort = SystemSort()

    s_sort.fill_list(5000)
    main(b_sort, ' Bubble sort ')
    main(s_sort, ' Selection sort ')
    main(m_sort, ' Min_max sort ')
    main(h_sort, ' Insertion sort - half swap ')
    main(f_sort, ' Insertion sort - full swap ')
    s_sort.fill_list(300000)
    main(sh_sort, ' Shell sort ')
    main(sys_sort, ' System sort ')
"""


"""
if __name__ == "__main__":
    sort_fun = [BubbleSort(), SelectionSort(), MinMaxSort(), HalfSwapInsertionSort(), FullSwapInsertionSort()]
    sort_name = [' Bubble sort ', ' Selection sort ', ' Min_max sort ', ' Insertion sort - half swap ',
                 ' Insertion sort - full swap ']
    sort_fun[0].fill_list(5000)

    for x in range(len(sort_fun)):
        main(sort_fun[x], sort_name[x])

    sh_sort = ShellSort()
    sys_sort = SystemSort()

    sh_sort.fill_list(100000)
    main(sh_sort, ' Shell sort ')
    main(sys_sort, ' System sort ')
"""


if __name__ == "__main__":
    sort_functions = {' Bubble sort ': BubbleSort(),  ' Selection sort ': SelectionSort(), ' Min_max sort ': MinMaxSort(),
                      ' Insertion sort - half swap ': HalfSwapInsertionSort(),
                      ' Insertion sort - full swap ': FullSwapInsertionSort(),
                      ' Shell sort ': ShellSort(), ' System sort ': SystemSort()}

    for key, value in sort_functions.items():
        if key == ' Bubble sort ':
            value.fill_list(5000)
        elif key == ' Shell sort ':
            value.fill_list(200000)
        main(value, key)

"""
    sort_name = list(sort_functions.keys())
    sort_func = list(sort_functions.values())

    for x in range(len(sort_func)):
        if x == 0:
            sort_func[x].fill_list(5000)
        elif x == 5:
            sort_func[x].fill_list(200000)
        main(sort_func[x], sort_name[x])
"""
