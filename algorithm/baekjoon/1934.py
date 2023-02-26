T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    p = A * B
    if A<B:
        A, B = B, A
    rst = 0
    while True:
        r = A%B
        if not r:
            rst = B
            break
        A = B
        B = r

    print(p//rst)




