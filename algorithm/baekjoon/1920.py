import sys
input = sys.stdin.readline

def bS(target,s,e):
    global ans
    if A[0] > target:
        return
    if A[-1] < target:
        return
    while s<=e:
        mid = (s + e) // 2
        if A[mid] < target:
            s = mid+1
        elif A[mid] > target:
            e = mid -1
        else:
            ans = 1
            return



N = int(input())
A = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
A.sort()
for t in target:
    ans = 0
    bS(t,0,N-1)
    print(ans)

