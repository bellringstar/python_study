'''
출력 = P개의 버즈 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는가
'''
T = int(input())
for test in range(1, T+1):
    N = int(input())
    AB_lst = [0] * N
    for i in range(N):
        A, B = map(int, input().split())
        AB_lst[i] = [A,B] #[[1, 3], [2, 5]] #[1이상,3이하 정류장만], [2이상, 5이하 정류장]
    P = int(input())
    C_list = [0] * P
    for j in range(P):
        C_list[j] = int(input()) #[13 22, 8, 1, 3] 정류장 번호
    '''
    C_list[0] = 13
    A,B 사이에 13이 있다면 cnt + 1
    '''
    cnt_list = [0] * P
    for idx in range(P):
        for AB in AB_lst:
            if C_list[idx] >= AB[0] and C_list[idx] <= AB[1]:
                cnt_list[idx] += 1
    print(f'#{test}', end=' ')
    print(*cnt_list)


