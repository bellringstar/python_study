def is_possible(start, goal, lst):
    stack = [start]
    while stack:
        top = stack.pop()
        for t in edge:
            if top == t[0]:
                stack.append(t[1])
        if goal in stack:
            return 1
    return 0



T = int(input())

for test in range(T):
    edge = []
    V, E = map(int, input().split()) #V 이내 노드, E개의 간선 뱡향성 그래프
    for e in range(E):
        start, end = map(int, input().split()) #경로 start -> end   #[(1, 4), (1, 3), (2, 3), (2, 5), (4, 6)]
        edge.append((start, end))
    S, G = map(int, input().split()) #시작점, 도착점
    print(f'#{test+1} {is_possible(S, G, edge)}')






    
