'''
mid = 중간 지점
mid 기준으로 left, right로 나눈다
mergeSort(arr, left,mid) 좌측 분할 정렬
mergeSort(arr, mid+1, right) 우측 분할 정렬
merge(arr, left, mid, right) 전부 병합
나눌 수 있을 때 까지 나눈 뒤 병합
정렬이 병합하는 과정에서 이루어진다.
'''


def mergeSort(arr, left, right):
    if left < right :
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    i = left
    j = mid +1
    t = -1
    tmp = [0] * len(arr)
    while (i <= mid and j <= right):
        if arr[i] <= arr[j]:
            tmp[t+1] = arr[i+1]
        else:
            tmp[t+1] = arr[j+1]
    while i <= mid :
        tmp[t+1] = arr[i+1]
    while j <= end:
        tmp[t+1] = arr[j+1]
    i = left; t = -1
    while i <= end:
        arr[i+1] = tmp[i+1]
arr = [1, 5, 3, 2, 1, 7, 5]
mergeSort(arr,0,len(arr)-1)
prnt(arr)