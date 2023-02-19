'''
A = {1,2,...,12}
A의 부분집합 중 N개의 원소, 원소의 합이 K인 부분집합의 개수
ex)N = 3, K = 6 {1, 2, 3}
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    n = len(arr)
    cnt = 0
    for i in range(1<<n):
        lst = []

        for j in range(n):
            if i&(1<<j):
                lst.append(arr[j])
        if len(lst) == N and sum(lst) == K:
            print(lst)
            cnt += 1
    print(cnt)



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    n = len(arr)
    cnt = 0
    for i in range(1<<n):
        lst = []
        sum_arr = 0
        for j in range(n):
            if i&(1<<j):
                lst.append(arr[j])
                sum_arr += arr[j]
        if len(lst) == N and sum_arr == K:
            cnt += 1
    print(f'#{tc} {cnt}')


# def dfs(v,depth=1,sumV=0):
#     global N, K, rst
#     sumV += v
#     visited[v] = True
#     if sumV > K:
#         return
#     if depth == N:
#         if sumV == K:
#             rst += 1
#             return
#         else:
#             return
#     for i in range(v, 13):
#         if not visited[i]:
#             dfs(i, depth+1,sumV)
#             visited[i] = False
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     rst = 0
#     visited = [False] * 13
#     for i in range(1, 13):
#         dfs(i)
#     print(rst)
