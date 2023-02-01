'''
pivot을 기준으로 그보다 작은 리스트/ 큰 리스트로 분할
작은 리스트에 위의 과정을 반복
큰 리스트에도 위의 과정을 반복
pivot은 고정된 위치. 
재귀호출마다 고정된 위치의 pivot이 1개씩 증가

1. pivot을 정하고 분할한다.
2. 분할된 left를 다시 분할
3. 분할된 right를 다시 분할
'''

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

