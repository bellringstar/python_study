def move():
    arr.append(arr.pop(0))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N개의 숫자 M번
    arr = list(map(int, input().split()))
    for _ in range(M):
        move()

    print(f'#{tc} {arr[0]}')
