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
#[1,5,2,4,2,5,7,9,5] 
def Quick_Sort(lst,left,right):
    p = lst[right] #right = 마지막 인덱스
    #left부터 p보다 작은 값들을 찾는다.
    #right부터 p보다 큰 값들을 찬느다 
    while left != right:
        print(left, right)
        if lst[left]<=p and lst[right-1]>=p:
            left +=1 ; right -=1
        else:
            lst[left],lst[right] = lst[right],lst[left]
            left +=1; right -=1
    print(lst)
    #큰값은 있지만 작은값은 없는 상황 : 교환은 못하고 큰 값을 오른쪽으로 옮겨야함 
    i = 0; j = len(lst)-1       
        
    Quick_Sort(lst, left, p)
    Quick_Sort(lst, p+1, right)

lst = [1,5,2,4,2,5,7,9,5]
Quick_Sort(lst,0,len(lst)-1)
