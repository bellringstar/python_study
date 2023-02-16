'''
NxN
한줄에 하나씩 N개의 숫자를 골라 합이 최소가 되도록
1 열마다 1개만 선택
'''
'''
#순열
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k): #i부터 시작 = 중복상황 방지
            p[i], p[j] = p[j], p[i]
            #p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = len(p)
f(0, N)
'''
'''
1행에서 N개중에 1개 선택
2행에서 N개중에 1개 선턱 단 1행의 것과 열이 다른것으로
3행에서 N개중에 1개 선택 단 1,2행의 것과 열이 다른 것으로 ....
열이 다르다.visited를 만들어 열 위치 idx True로 변경
'''
def partial(h, k, s=0):
    global s_min
    if s_min < s:
        return
    elif h == k :
        s_min = s
        return s_min
        #N번째줄까지 합
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            s += arr[h][i]
            partial(h+1, k, s)
            s -= arr[h][i]
            visited[i] = False





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    s_min = float('inf')
    partial(0, N)
    print(f'#{tc} {s_min}')

