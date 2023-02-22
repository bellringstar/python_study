def findD(a):
    global cnt
    while queue:
        a = queue.pop()
        cnt += 1
        for i in range(len(parent)):
            if parent[i] == a:
                queue.append(i)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) #간선의 개수 E, 노드 N을 루트로 하는 서트브리에 속하는 노드의 개수 = 조상노드 N인것
    lst = list(map(int, input().split()))
    parent = [0] * (E+2)
    cnt = 1
    for idx in range(0, len(lst), 2):
        p = lst[idx]
        c = lst[idx + 1]
        parent[c] = p
    queue = []
    for i in range(E+2):
        if parent[i] == N:
            queue.append(i)
    findD(N)
    print(f'#{tc} {cnt}')
