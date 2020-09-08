def heapify(arr, n, i):
    tmp = arr[i]
    max_idx = i
    if 2 * i + 1 < n and arr[2 * i + 1] > tmp:
        max_idx = 2 * i + 1
    if 2 * i + 2 < n and arr[2 * i + 2] > arr[max_idx]:
        max_idx = 2 * i + 2
    if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        heapify(arr, n, max_idx)


def heap_sort(arr):
    n = len(arr)
    # 建立大顶堆
    for i in range((n - 2) // 2, -1, -1):
        heapify(arr, n, i)
    # 逐次交换第一个元素和最后一个元素,然后重新heapify
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def main():
    arr = [1, 3, 2, 5, 4]
    heap_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()