import sys
sys.stdin = open('input중위순회.txt', 'r')
def inorder(root):
    global N,s
    if root < N+1:
        inorder(root*2)
        s += words_dict[root]
        inorder(root*2+1)


for tc in range(1, 11):
    N = int(input())
    arr = [[] for _ in range(N+1)]
    words_dict = {}
    for _ in range(N):
        lst = input().split()
        words_dict[int(lst[0])] = lst[1]
    s = ''
    inorder(1)
    print(f'#{tc} {s}')



