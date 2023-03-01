import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# def find(a):
#     stack = []
#     if arr[a] == a:
#         return a
#     else:
#         stack.append(arr[a])
#         while True:
#             v = stack.pop()
#             if arr[v] == v:
#                 return v
#             else:
#                 stack.append(arr[v])

def find(a):
    if arr[a] == a:
        return a
    else:
        return find(arr[a])

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        arr[b] = a
        return

n, m = map(int, input().split())
arr = []

for i in range(n+1):
    arr.append(i)
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')



'''
import sys
input = sys.stdin.readline

def root(a):
    while a != tree[a]:
        tree[a] = tree[tree[a]]
        a = tree[a]
    return a

n, m = map(int, input().split())
tree = [i for i in range(n+1)]
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        tree[root(b)] = root(a)
    else:
        if root(a)==root(b):
            print("YES")
        else:
            print("NO")
'''


