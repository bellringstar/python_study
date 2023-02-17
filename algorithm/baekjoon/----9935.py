import sys
input = sys.stdin.readline

string = input().rstrip()
ex = input().rstrip()
N = len(ex)
cnt = 0
stack = [string[0]]
i = 0
while i<len(string):
    if stack[-1] == ex[cnt]:
        cnt += 1
    else:
        cnt = 0
    stack.append(string[i])
    if cnt == N:
        for _ in range(N):
            stack.pop()
        cnt = 0
    i += 1
