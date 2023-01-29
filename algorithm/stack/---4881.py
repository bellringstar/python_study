'''
백트래킹
한줄에 한 개씩 N개의 숫자를 골라 합이 최소 단 세로가 같은 줄에서 하나의 숫자만
212
585
722   -> 1+5+2 최소 8
'''

N = 3
lst = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]

'''
1. 첫째줄에서 하나 선택 # 작은 것 우선선택
2. 둘째줄에서 그 선택한 줄을 제외하고 다른 것 선택 
3. 셋째줄에서 나머지 한 줄에서 선택
4. 합을 기록. 만약 모든 선택이 각 줄의 최소다? = 정답
5. 전부 반복해서 가장 작은 합 출력

'''
test = [False] * N
sumL = 0
answer_list = []
# def minimum(lst,test,row,answer):
#     if row  == 0:
#         return answer_list.append(answer)
#     for idx in range(N):
#         if not test[idx]:
#             test[idx] = True
#             answer += lst[N-row][idx]
#             minimum(lst,test,row+1,answer)
    


        
