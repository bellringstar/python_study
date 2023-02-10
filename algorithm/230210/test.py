def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = i
        while tmp>=1 and arr[tmp-1] > arr[tmp]:
            arr[tmp-1],arr[tmp] = arr[tmp],arr[tmp-1]
            tmp -=1

arr = [8, 1, 9, 4, 4, 2, 0]

insertion_sort(arr)

print(arr)