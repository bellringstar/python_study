'''
quick_sort(arr, start, end)
1. pivot을 정한다.
2. pivot보다 작은것들과 큰 것들로 나눈다.
3. 작은것 pivot 큰것 으로 정렬한다. -> pivot의 위치가 고정됨
4. 작은것/큰것에서 똑같은 행동을 반복
5. 정렬이 완료된다. 완료조건은? start == end : 어레이의 원소가 하나만 있는 상태 -> 정렬할게 없다.
'''

def quickSort(arr, start, end):    #start = 0 , end = 마지막 인덱스
    if start >= end: #종료조건
        return
    pivot = arr[end]
    left = start
    right = end - 1
    while left < right:
        for i in range(left, right + 1):
            if arr[i] > pivot:
                left = i
                break
        for j in range(right, left, -1):
            if arr[j] < pivot:
                right = j
                break
        arr[left],arr[right] = arr[right],arr[left]
    if left == right:
        arr[left],arr[end] = arr[end],arr[left]
    p = left
    quickSort(arr, start, p-1);
    quickSort(arr, p+1, end) #p+1부터 큰것들이 모여있는것 정렬, p는 현재 위치가 고정된 상태




lst = [1, 4, 7, 6, 3, 2, 8, 5]
quickSort(lst, 0, 7)

print(lst)