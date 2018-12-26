import random
import time

def data_copy(dst, src):
    for x in range(len(src)):
        dst[x] = src[x]

def fill_list(arr, size):
    print('Data 생성 중....')
    for x in range(size):
        arr.append(random.randrange(1, size * 2))

def print_list(arr, size, msg):
    print(msg)
    if size <= 20:
        print(arr)
    else:
        print(arr[:10])
        print(arr[size-10:])
        
def bubble_sort(arr, size):
    for i in range(size - 1):
        for j in range(i + 1, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def bubble_sort1(arr, size):
    sorted = False
    for i in range(1, size):
        if sorted:
            break
        sorted = True
        for j in range(size - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False

# 선택 정렬
def selection_sort(arr, size):
    for i in range(size - 1, 0, -1):
        pos = i
        for j in range(i - 1, -1, -1):
            if arr[pos] < arr[j]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]

# Duplex selection sort(이중 선택 정렬)
def minmax_sort(arr, size):
    j_max = size - 1
    max_pos, i, j = 0, 0, 0
    while i < j_max:
        min_pos = i
        j = max_pos = j_max
        while i <= j:
            if arr[min_pos] > arr[j]:
                min_pos = j
            elif arr[max_pos] < arr[j]:
                max_pos = j
            j -= 1
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        if i == max_pos:
            max_pos = min_pos
        arr[j_max], arr[max_pos] = arr[max_pos], arr[j_max]
        i += 1
        j_max -= 1

# half swap(삽입 정렬)
def insertion_sort(arr, size, n = 0, h = 1):
    for i in range(n + h, size, h):
        j = i
        value = arr[j]
        while j > n:
            if arr[j - h] > value:
                arr[j] = arr[j - h]
            else:
                break
            j -= h
        arr[j] = value

#full swap(삽입 정렬)
def insertion_sort1(arr, size):
    for i in range(1, size):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

# 쉘 정렬
def shell_sort(arr, size):
    h = size // 3 + 1
    while h > 1:
        for x in range(h):
            insertion_sort(arr, size, x, h)
        h = h // 3 + 1
    insertion_sort(arr, size)
            

def sorts(f, arr, size, msg):
    print('{:=^60}'.format(msg))
    print_list(arr, size, '<-- before sort -->')
    t1 = time.time()
    f(arr, size)
    t2 = time.time()
    print_list(arr, size, '<-- after sort -->')
    print('{} time : %.3f'.format(msg) % abs(t2 - t1))

def main():
    size = 5000
    arr, tmp = [], [0] * size
    fill_list(arr, size)
    data_copy(tmp, arr)    
    
    f_list = [bubble_sort, bubble_sort1, selection_sort, minmax_sort,
              insertion_sort, insertion_sort1, shell_sort]
    m_list = ['Bubble sort', 'Bubble sort1', 'Selection sort', 'Minmax sort',
              'Half swap sort', 'Full swap sort', 'Shell sort']

    for x in range(len(f_list)):
        sorts(f_list[x], arr, size, m_list[x])
        data_copy(arr, tmp)
        print()


if __name__ == '__main__':
    main()    
    
