T = int(input())
#완전이진트리
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) #N:노드개수, M:리프노드개수, L:출력할 노드 번호
    tree = [0] * (N+1)
    for _ in range(M):
        a,b = map(int, input().split())
        tree[a] = b

    if N%2:
        for i in range(N-1,1,-1):
            tree[i//2] = tree[i] + tree[i+1]
    else:
        tree[N//2] = tree[N]
        for i in range(N-2,1,-1):
            tree[i // 2] = tree[i] + tree[i+1]

    print(f'#{tc} {tree[L]}')