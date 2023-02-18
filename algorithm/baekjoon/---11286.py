import sys, collections
input = sys.stdin.readline

dq = collections.deque

N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        pass # 절대값이 가장 작거나 같을때는 최소값을 pop하는 작업

    else:

