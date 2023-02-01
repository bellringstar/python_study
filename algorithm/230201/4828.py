T = int(input())

for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    minN = num_list[0]
    maxN = num_list[0]
    for num in num_list:
        if num < minN:
            minN = num
        if num > maxN:
            maxN = num

    print(f'#{test+1} {maxN - minN}')