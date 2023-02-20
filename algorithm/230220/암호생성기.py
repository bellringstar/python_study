import sys
sys.stdin = open('input암호.txt','r')

for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))

    i = 0
    while True:
        arr.append(arr.pop(0) -(i%5 +1))
        if arr[-1] <= 0:
            arr[-1] = 0
            break
        i += 1

    print(f'#{tc}', end=' ')
    print(*arr)