'''
연속한 1의 최대 개수
00110001110
[0,0,1,2,0,0,0,1,2,3,0]
'''

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_string = input()
    cnt_list = [0] * N
    cnt = 0
    for idx in range(N):
        if num_string[idx] == '1':
            cnt +=1
            cnt_list[idx] = cnt
        else:
            cnt = 0

    maxN = cnt_list[0]
    # print(cnt_list)
    for num in cnt_list:
        if num > maxN:
            maxN = num
    print(f'#{test} {maxN}')

