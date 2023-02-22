def inorder(root):
    global num,N
    if root < N+1:
        inorder(root*2)
        node[root] = num
        num += 1
        inorder(root*2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 1
    node = [0] * (N + 1)
    inorder(1)
    print(f'#{tc} {node[1]} {node[N//2]}')