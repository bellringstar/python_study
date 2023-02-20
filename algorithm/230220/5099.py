T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    arr = []
    for i in range(M):
        arr.append([i+1, C[i]]) #피자 번호, 치즈양

    check = []
    for _ in range(N):
        check.append(arr.pop(0)) #화덕에 들어간 것들


    while check:
        no, c = check.pop(0)
        no, c = no, c//2
        if c > 0:
            check.append([no, c])
        elif arr:
            check.append(arr.pop(0))

    print(f'#{tc} {no}')




