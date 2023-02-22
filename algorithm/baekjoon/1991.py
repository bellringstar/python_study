import string,sys
input = sys.stdin.readline


def preorder(v):
    if v:
        print(c_dic[v],end='')
        preorder(lc[v])
        preorder(rc[v])

def inorder(v):
    if v:
        inorder(lc[v])
        print(c_dic[v], end='')
        inorder(rc[v])

def postorder(v):
    if v:
        postorder(lc[v])
        postorder(rc[v])
        print(c_dic[v], end='')



N = int(input())
lc = [0] * (N+1)
rc = [0] * (N+1)

c_dic = {num+1:word for num,word in enumerate(string.ascii_uppercase)}
n_dic = {word:num+1 for num,word in enumerate(string.ascii_uppercase)}

for _ in range(N):
    arr = list(input().split())
    if arr[1] != '.':
        lc[n_dic[arr[0]]] = n_dic[arr[1]]
    if arr[2] != '.':
        rc[n_dic[arr[0]]] = n_dic[arr[2]]

preorder(1)
print()
inorder(1)
print()
postorder(1)