def inorder(root):
    global N, rst
    if root <= N:
        inorder(root*2)
        rst += node[root]
        inorder(root*2+1)



for tc in range(1, 11):
    N = int(input())
    node = [0] * (N+1)
    arr = [[] for _ in range(N+1)]
    for _ in range(1,N+1):
        lst = input().split()
        node[int(lst[0])] = lst[1]
    rst = ''
    inorder(1)

    print(f'#{tc} {rst}')
