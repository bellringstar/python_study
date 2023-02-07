T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, N):
        if i % 2:
            minIdx = i
            minV = arr[i]
            for j in range(i+1,N):
                if minV > arr[j]:
                    minV = arr[j]
                    minIdx = j
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

        else:
            maxIdx = i
            maxV = arr[i]
            for j in range(i+1,N):
                if maxV < arr[j]:
                    maxV = arr[j]
                    maxIdx = j
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

    print(f'#{tc}',end=' ')
    print(*arr[:10])