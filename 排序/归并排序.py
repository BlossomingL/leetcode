def merge(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    res = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i < n1:
        res.extend(arr1[i:])
    if j < n2:
        res.extend(arr2[j:])
    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)


def main():
    arr = [1, 3, 2, 5, 4]
    print(merge_sort(arr))


if __name__ == '__main__':
    main()