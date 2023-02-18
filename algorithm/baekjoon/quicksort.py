def partition(arr, s, e):
    # pivot의 idx 리턴
    x = arr[e]
    i = s - 1 #i: 1구역의 끝 지점
    for j in range(s, e): #j: 3구역의 끝 지점
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[e] = arr[e], arr[i+1]
    return i+1


def quickSort(arr, s, e):
    if s < e:
        p = partition(arr, s, e)
        quickSort(arr,s,p-1)
        quickSort(arr,p+1,e)


arr = [1,8,17,6,5,6,2,9]

quickSort(arr, 0, len(arr)-1)

print(arr)