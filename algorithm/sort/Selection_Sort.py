'''
선택정렬
고정된 위치에 어떤 원소를 넣을지 선택
자리를 선택 한 뒤 그 자리에 오는 값을 찾자
ex)고정된 위치 = 처음과 끝
1. 리스트에서 가장 작은 값을 찾는다.
2. 처음 인덱스의 값과 교환한다
3. 시작 인덱스를 1늘려 끝까지 반복.
-> 반복문 / 재귀

1.입력: 정렬할 list
'''
#[3,5,2,1,7]
def Selection_Sort(lst):
    for i in range(len(lst)):
        min = lst[i]
        min_idx = i   
        for j in range(i,len(lst)-1): #0,1,2,3,4,
            if min > lst[j]:
                min = lst[j]
                min_idx = j
        lst[i],lst[min_idx] = lst[min_idx],lst[i]
        print(lst)
lst =[3,5,2,1,7]
Selection_Sort(lst)
print(lst)        