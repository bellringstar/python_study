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
#[1,2,7,3,4,8,5] 
#[0,i,,j,0,0,0]
def Quick_Sort(lst,left,right):
    p = partition() #마지막 원소 5   left=0 right=len(lst)-1 = 8
    '''
    pivot보다 작냐, pivot보다 크냐, 아직안봤냐
    작은영역과 큰영역을 어떻게 나눌것인가
    작은영역/큰영역 pivot과 큰영역의 1번째랑 교환
    작은영역 0부터 비교 큰 영역 right - 1 부터
    '''    
    Quick_Sort(lst,left,pivot_index)
    Quick_Sort(lst,pivot_index+1,right)
            
def partition(lst, left, right):
    pivot = lst[right]


lst = [1,5,2,4,2,5,7,9,5]
Quick_Sort(lst,0,len(lst)-1)
