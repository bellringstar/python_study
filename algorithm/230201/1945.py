'''
숫자 N을 소인수분해 해 소인수들을 출력
입력 : 숫자 N
출력 : 소인수 분해의 승수
1. 소인수 리스트 [2,3,5,7,11]
소인수 리스트로 안나눠 질때까지
'''

T = int(input())
num_list = [2, 3, 5, 7, 11]
for test in range(1, T+1):
    cnt_lst = [0] * 5
    N = int(input())
    i = 0
    for num in num_list:
        cnt = 0
        while N % num == 0:
            cnt += 1
            N //= num
            cnt_lst[i] = cnt
        i += 1
    print(f'#{test}', end=' ')
    print(*cnt_lst)

