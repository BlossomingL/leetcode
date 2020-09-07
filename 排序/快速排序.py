def get_pivot(arr, i, j):
    tmp = arr[i]

    while i < j:

        while i < j and arr[j] >= tmp:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        while i < j and arr[i] <= tmp:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1

    arr[i] = tmp
    return i


def quicksort(arr, left, right):
    if left < right:
        pivot = get_pivot(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


def main():
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == '__main__':
    main()