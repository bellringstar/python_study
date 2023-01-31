'''
Bubble Sort 
다음 수와 비교해가며 자기가 다음 것보다 크다면 자리 교체
1.입력 : 어레이 a,인덱스 시작, 인덱스 끝
2.출력 : 정렬이 끝난 어레이
a[0],a[1] 비교
if a[0]>a[1] => 0 <-> 1
a[1] vs a[2] 
else a[0] < a[1]: 변화 x
a[1]과a[2] 비교
한바퀴 종료 : 리스트 마지막만 고정. 
리스트 크기 1 줄여서 다시 반복
[1,2,3] len = 3
'''

def BubbleSort(lst, i, end):
    if end == 0:
        return 
    swap = False 
    while i < len(lst)-1:
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i] #크기 비교 후 교환
            swap =True #정렬이 한번이라도 일어났다.
        i += 1
    if not swap : #정렬이 한번도 일어나지 않았다 = 정렬 종료된 상태
        return
    print(lst)    
    BubbleSort(lst, 0, end-1)
lst = [4,7,1,2,3,4,8,2,11,82,45,63]
BubbleSort(lst, 0, len(lst)-1)
