'''
가능한 경로인가
ex) A-B, B-C, A-D, B-D, E-A 경로 존재
계획 ECBCD -> E->A->B->C->B->C->B->D 가능
'''
import sys
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    else:
        return find(parent[a])

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N = int(input())
M = int(input())

arr= [[] for _ in range(N+1)]
parent = [0] * (N+1)
for i in range(1,N+1):
    parent[i] = i

for j in range(1,N+1):
    lst = [0] + list(map(int, input().split()))
    for idx in range(1, N+1):
        if lst[idx] == 1:
            union(j,idx)

route = list(map(int, input().split()))

node = find(route[0])

for i in range(1, M):
    if node != find(route[i]):
        print('NO')
        break
else:
    print('YES')
