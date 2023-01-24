T = int(input())
for test in range(T):
    N, M = map(int, input().split()) #10 3 10개의 수, 3개의 연속된 수 합
    a = list(map(int, input().split())) # [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
    max_sum = sum(a[0:0 + M])
    min_sum = sum(a[0:0 + M])
    for i in range(N - M + 1):
        if sum(a[i:i+M]) > max_sum:
            max_sum = sum(a[i:i+M])
        if sum(a[i:i+M]) < min_sum:
            min_sum = sum(a[i:i+M])
    print(f'#{test + 1} {max_sum - min_sum}')    

