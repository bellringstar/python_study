'''
연속으로 증가한 수의 길이의 최대
[1,2,3,4,5] = 5
[4,5,1,2,3] = 3
cnt_lst = [1,1,1,1,1]
이전것과 차이가 1일때 이전 cnt + 1
[1,2,3,4,5
[1,2,1,2,3]
'''
T = int(input())
for test in range(1,T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    cnt_lst = [1] * N
    for idx in range(1, N):
        if carrot_list[idx] - carrot_list[idx - 1] == 1:
            cnt_lst[idx] += cnt_lst[idx-1]
    maxN = cnt_lst[0]
    for num in cnt_lst:
        if num > maxN:
            maxN = num
    print(f'#{test} {maxN}')


