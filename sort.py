
# 插入排序 insert 插入  时间复杂度：O(n²) 空间复杂度：O(1)
# 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中
def insert_sort(arr):

    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

# 希尔排序 https://blog.csdn.net/qq_39207948/article/details/80006224 时间复杂度：O(n) 空间复杂度：O(n√n)
def shell_sort1(arr):
    gap = len(arr)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(arr)):
            for j in range(i % gap, i, gap):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

    return arr

def shell_sort(arr):
    gap = len(arr)

    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(arr)):
            for j in range(i%gap, i, gap):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr



# 冒泡排序 相邻位置比较 时间复杂度：O(n²) 空间复杂度：O(1)
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 快速排序 分成两部分 一部分的所有值大于另一部分 时间复杂度：O(nlog₂n) 空间复杂度：O(nlog₂n)
def qucick_s(arr):

    def quick_sort(arr, start, end):
        if start > end:
            return
        init = arr[end]
        mid_index = start
        for i in range(start, end):
            if arr[i] < init:
                if i != mid_index:
                    arr[i], arr[mid_index] = arr[mid_index], arr[i]
                mid_index += 1
        arr[mid_index], arr[end] = arr[end], arr[mid_index]
        quick_sort(arr, mid_index+1, end)
        quick_sort(arr, start, mid_index-1)

    quick_sort(arr, 0, len(arr)-1)
    return arr



# 简单选择排序 时间复杂度：O(n²) 空间复杂度：O(1)
def simple_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

from collections import deque

def heap_sort(arr):
    pass


# 归并排序
# 采用分治法（Divide and Conquer）的一个非常典型的应用。
# 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，
# 再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并
# 时间复杂度：O(nlog₂n) 空间复杂度：O(1)
def merge_sort(arr):
    def merge_arr(arr_l, arr_r):
        arr_new = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                arr_new.append(arr_l.pop(0))
            else:
                arr_new.append(arr_r.pop(0))

        if len(arr_l) != 0:
            arr_new.extend(arr_l)
        if len(arr_r) != 0:
            arr_new.extend(arr_r)
        return arr_new
    def recursive(arr):

        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        arr_l = recursive(arr[:mid])
        arr_r = recursive(arr[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(arr)


def merge(arr, l, m, r):
    L = arr[l: m+1]
    R = arr[m+1: r+1]
    i, j, k = 0, 0, l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def recursive(arr, l, r):
    if l < r:
        mid = int((l+r)/2)

        recursive(arr, l, mid)
        recursive(arr, mid+1, r)
        merge(arr, l, mid, r)





# 基数排序
# 透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用 时间复杂度：O(d(r+n)) 空间复杂度：O(rd+n)
def radix_sort(arr):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(arr):
        bucket = [[],[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(arr)):
            num = (arr[i]//10**digit) % 10
            bucket[num].append(arr[i])
        arr.clear()
        for j in range(len(bucket)):
            arr.extend(bucket[j])
        digit += 1
    return arr




if __name__ == '__main__':
    arr = [6, 5,2, 34,5, 33, 5, 34, 8, 3, 78, 25]
    #print(insert_sort(arr))
    #print(shell_sort(arr))
    #print(bubble_sort(arr))
    #quick_sort(arr, 0, len(arr)-1)
    #print(arr)
    #print(simple_sort(arr))
    #print(merge_sort(arr))
    print(recursive(arr, 0, len(arr)-1))
    print(arr)
    print(arr[0:2])

