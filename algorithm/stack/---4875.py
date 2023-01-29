# T = int(input())

# for test in range(T):
#     N = int(input())
#     labi = []
#     for _ in range(N):
#         labi.append(list(map(int, input())))
        
labi = [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]
#0은 통로 1은 벽, 2는 출발, 3은 도착
'''
현위치, 이동방향 스택에 push
진행하다 이동 불가능한 지점 -> 다른 방향 이동이 가능한 지점까지 pop
다른 방향으로 이동 push
백트래킹
'''
stack = []
#1. 시작위치 파악
for i in range(labi):
    for j in range(i):
        if labi[i][j] == 2: #시작점 인덱스 파악
            stack.append([i,j]) #[4,3]