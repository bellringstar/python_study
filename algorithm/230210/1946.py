T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        Ci, Ki = input().split()
        arr.append(Ci * int(Ki))
    word = ''
    for s in arr:
        word += s
    print(f'#{tc}')
    for i in range(0, len(word), 10):
        print(word[i:i+10])

