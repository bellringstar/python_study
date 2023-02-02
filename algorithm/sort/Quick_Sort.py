'''
quick_sort(arr, start, end)
1. pivot을 정한다.
2. pivot보다 작은것들과 큰 것들로 나눈다.
3. 작은것 pivot 큰것 으로 정렬한다. -> pivot의 위치가 고정됨
4. 작은것/큰것에서 똑같은 행동을 반복
5. 정렬이 완료된다. 완료조건은? start == end : 어레이의 원소가 하나만 있는 상태 -> 정렬할게 없다.
'''
<<<<<<< HEAD
=======

# def quickSort(arr, start, end):    #start = 0 , end = 마지막 인덱스
#     if start >= end: #종료조건
#         return
#     pivot = arr[end]
#     left = start
#     right = end - 1
#     while left < right:
#         for i in range(left, right + 1):
#             if arr[i] > pivot:
#                 left = i
#                 break
#         for j in range(right, left, -1):
#             if arr[j] < pivot:
#                 right = j
#                 break
#         arr[left],arr[right] = arr[right],arr[left]
#     if left == right:
#         arr[left],arr[end] = arr[end],arr[left]
#     p = left
#     quickSort(arr, start, p-1);
#     quickSort(arr, p+1, end) #p+1부터 큰것들이 모여있는것 정렬, p는 현재 위치가 고정된 상태
>>>>>>> 75603c6221a87a6ac2e3b3678fdbea87ebfa82de

def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end) # arr을 피벗을 기준으로 분할
        quickSort(arr, start, p-1) # 피벗의 왼쪽에서 작업을 반복
        quickSort(arr, p+1, end) # 피벗의 오른쪽에서 작업을 반복

def partition(arr, start, end):
    pivot = arr[end] #임의로 정한 pivot
    i = start - 1 #작은영역 시작점
    for j in range(start, end): #시작부터 끝까지
        if arr[j] < pivot: #만약 그 값이 pivot보다 작다면
            i += 1 #작은 영역 증가
            arr[i], arr[j] = arr[j], arr[i] # 큰영역에 존재하는 작은값과 작은영역에 있는 큰 값 교환
    arr[i+1], arr[end] = arr[end], arr[i+1] #pivot과 작은영역의 끝 다음위치 = 큰 영역의 시작 값과 교환
    return i + 1 #교환 후 pivot의 위치 반환

lst = [5,2,1,5,7,2,4]
quickSort(lst, 0, len(lst)-1)
print(lst)

<<<<<<< HEAD
=======


lst = [1, 4, 7, 6, 3, 2, 8, 5]
quickSort(lst, 0, 7)

print(lst)
>>>>>>> 75603c6221a87a6ac2e3b3678fdbea87ebfa82de
