'''
연속합
연속일에 따른 합
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N = 날짜수 = 수열길이, K = 연속 날짜 수
arr = list(map(int, input().split()))

s = 0
e = K
ans = maxV = sum(arr[s:e])
while e<N:
    new = maxV - arr[s] + arr[e]
    if new>ans:
        ans = new
    s += 1
    e += 1
    maxV = new

print(ans)