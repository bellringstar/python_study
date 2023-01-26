A = list(range(1, 13))
#부분집합 N개의 원소, 원소의 합 = K인 개수 없다면 0

T = int(input())
partial_list =[]

n = len(A)
for i in range(1<<n):
    p_list = []
    for j in range(n):
        if i&(1<<j):
            p_list.append(A[j])
    partial_list.append(p_list)
for test in range(T):
    cnt = 0
    N, K = map(int, input().split())
    partial_list3 = []
    for lst in partial_list:
        if len(lst) == N:
            partial_list3.append(lst)
    for lst_3 in partial_list3:
        if sum(lst_3) == K:
            cnt += 1
    print(f'#{test+1} {cnt}')


