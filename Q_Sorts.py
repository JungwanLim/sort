import random
import time

def data_copy(dst, src):
    for x in range(len(src)):
        dst[x] = src[x]

def fill_list(arr, size):
    print('Sort {} integer Data'.format(size))
    for x in range(size):
        arr.append(random.randrange(1, size * 2))

def print_list(arr, size, msg):
    print(msg)
    if size <= 25:
        print(arr)
    else:
        print(arr[:10])
        print(arr[size-10:])

def merge(arr, first, middle, last):
    tmp = []
    i, j = first, middle + 1

    while i <= middle and j <= last:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= middle:
        tmp.append(arr[i])
        i += 1
    while j <= last:
        tmp.append(arr[j])
        j += 1

    for x in tmp:
        arr[first] = x;
        first += 1

def merge_sort(arr, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort(arr, first, middle)
        merge_sort(arr, middle + 1, last)
        merge(arr, first, middle, last)

def m_sort(arr, size):
    merge_sort(arr, 0, size - 1)
    return arr

def merge_sorted(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge1(l, r)
    else:
        return arr
        
def merge1(left, right):
    i = 0
    j = 0
    arr = []
    
    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1

    while (i<len(left)):
        arr.append(left[i])
        i+=1
    while (j<len(right)):
        arr.append(right[j])
        j+=1
        
    return arr

def m_sorted(arr, size):
    return merge_sorted(arr)

def partition(arr, first, last):
    left = first
    right = last - 1
    pivot = arr[last]

    while True:
        while arr[left] <= pivot and left <= right:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[last] = arr[last], arr[left]

    return left

def quick_sort(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quick_sort(arr, first, pivot - 1)
        quick_sort(arr, pivot + 1, last)

def q_sort(arr, size):
    quick_sort(arr, 0, size - 1)
    return arr

def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr

def q_sort1(arr, size):
    return quick_sorted(arr)

def max_heapify(arr, size, root):
    child = root * 2
    while child <= size:
        if child < size and arr[child - 1] < arr[child]:
            child += 1
        if arr[root - 1] < arr[child - 1]:
            arr[root - 1], arr[child - 1] = arr[child - 1], arr[root - 1]
        root = child
        child = root * 2

def heap_sort(arr, size):
    # Make heap
    for i in range(size//2, 0, -1):
        max_heapify(arr, size, i)

    # 정렬 과정
    for i in range(size, 1, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        max_heapify(arr, i - 1, 1)

    return arr
            
# half swap(삽입 정렬)
def insertion_sort(arr, size, n = 0, h = 1):
    j = 0
    for i in range(n + h, size, h):
        value = arr[i]
        for j in range(i, n - h, -h):
            if arr[j - h] > value:
                arr[j] = arr[j - h]
            else:
                break
        arr[j] = value

# 쉘 정렬
def shell_sort(arr, size):
    h = size // 3 + 1
    while h > 2:
        for x in range(h):
            insertion_sort(arr, size, x, h)
        h = h // 3 + 1
    insertion_sort(arr, size)

    return arr


def sys_sort(arr, size):
    arr.sort()
    return arr
    

def sorts(f, arr, size, msg):
    print('{:=^30}'.format(msg))
    #print_list(arr, size, '<-- before sort -->')
    t1 = time.time()
    arr = f(arr, size)
    t2 = time.time()
    #print_list(arr, size, '<-- after sort -->')
    print('Time to sort : %.3fsec' % abs(t2 - t1))

def main():
    size = 200000
    arr, tmp = [], [0] * size
    fill_list(arr, size)
    data_copy(tmp, arr)    
    
    f_list = [shell_sort, heap_sort, m_sort, m_sorted, q_sort, q_sort1, sys_sort]
    m_list = ['Shell sort', 'Heap sort', 'Merge sort', 'Merge sored', 'quick_sort', 
			  'quick_sort1', 'System sort']

    for x in range(len(f_list)):
        sorts(f_list[x], arr, size, m_list[x])
        data_copy(arr, tmp)
        print()


if __name__ == '__main__':
    main()    
