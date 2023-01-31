'''
삽입정렬
자기 인덱스 전의 것들과 비교해서 삽입될 위치를 찾아 인덱스 결정.
삽입을 위해 나머지 자료들 하칸씩 이동
=> 저음 key 값이 2부터 시작 (index = 1)
1. index1과 index0 비교
만약 index1이 더 작다 -> index0을 오른쪽으로 한칸 이동 index1을 0 자리에 삽입
2. index2와 index 0,1비교
크기비교 이전것보다 작다 -> 우측으로 이동 크다 이동X
index = len(lst) -1 까지 반복
'''


def Insertion_Sort(lst,key=1):
    if key == len(lst):
        return
    tmp = key
    for i in range(key-1,-1,-1):
        if lst[tmp] >= lst[i]:
            break
        if lst[tmp] < lst[i]:
            lst[tmp],lst[i] = lst[i],lst[tmp]
            tmp = i
    print(lst)
    Insertion_Sort(lst,key+1)

lst = [7,3,6,3,1,1,2]
Insertion_Sort(lst)
print(lst)

'''
key = 4
i = 3,2,1,0

'''
#최적화
def insertion_sort(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert