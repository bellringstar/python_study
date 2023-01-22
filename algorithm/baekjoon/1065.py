import sys
input = sys.stdin.readline
#1<=X<=N 한수의 개수. 어떤 수의 자리수 끼리 등차수열 
#한수 ex)111 = 한수 123=한수 135 =한수 109 =한수X


def arithmetic(n):
    if n <100:
        return True
    N = str(n)
    d = int(N[1]) - int(N[0])
    for i in range(2, len(N)):
        if d == int(N[i]) - int(N[i-1]):
            continue
        return False
    else:
        return True

N = int(input().rstrip())
rst = 0 #1~99는 무조건 한수.

if N < 100:
    rst = N
else:
    rst = 99
    for i in range(100,N+1):
        if arithmetic(i):
            rst +=1

print(rst)

    
