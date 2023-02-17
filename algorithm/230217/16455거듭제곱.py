def power(b, q):
    if q == 1:
        return b
    elif q%2:
        return power(b, q//2) * power(b, q//2 +1)
    else:
        return power(b, q//2) * power(b, q//2)




for tc in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    rst = power(N, M)
    print(f'#{T} {rst}')



