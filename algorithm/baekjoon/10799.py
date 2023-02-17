import sys
input = sys.stdin.readline

S = input()
rst = 0
cnt = 0 #레이저 카운트
for idx in range(len(S)):
    if S[idx] == '(':
        cnt += 1
    else:
        if S[idx] == ')':
            if S[idx-1] == '(': #레이저
                cnt-=1
                rst += cnt
            else: #막대 끝
                rst += 1
                cnt -= 1

print(rst)
