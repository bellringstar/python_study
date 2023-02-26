def inorder(root):
    global i,N
    if root<=N:
        inorder(root*2)
        tree[root] = i
        i += 1
        inorder(root*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    i = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')