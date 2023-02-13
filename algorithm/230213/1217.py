import sys
sys.stdin = open('1217input.txt', 'r')


for tc in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    def power(N, M):
        if M == 1:
            return N
        return N * power(N,M-1)
    rst = power(N, M)
    print(f'#{T} {rst}')
