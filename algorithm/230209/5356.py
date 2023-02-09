import sys
sys.stdin = open('5356input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    maxL = 0
    for s in arr:
        if len(s) > maxL:
            maxL = len(s)

    print(f'#{tc} ', end='')
    for i in range(maxL):
        for j in range(5):
            if i < len(arr[j]):
                print(arr[j][i], end='')
    print()