'''
거리가 2 이상 확보 = 조망권
조망권 확보된 세대 수 반환

'''
import sys
sys.stdin = open('input1206.txt', 'r')

for test in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    '''
    ex)[0,0,3,5,2,4,9,0,6,4,0,6,0,0]
    1. 해당 idx 양 옆의 수보다 커야함
    2. 그리고 idx-2, idx+2의 수보다 커야함
    3. lst[idx] - (idx-2/idx-1/idx+1/idx+2) 중 최대 값
    '''
    sum_num = 0
    for i in range(1, N-1):
        # i = 1 혹은 N-2 위치 -> 왼쪽으로는 i-1만 확인 혹은 우측으로는 i +1만 확인
        check_lst = []
        if lst[i] != 0 and lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            if lst[i] > lst[i-2] and lst[i] > lst[i+2]:
                check_lst.append(lst[i - 1])
                check_lst.append(lst[i + 1])
                check_lst.append(lst[i-2])
                check_lst.append(lst[i+2])
        if check_lst:
            check_max = check_lst[0]
            for num in check_lst:
                if num > check_max:
                    check_max = num
            sum_num += lst[i] - check_max
    print(f'#{test} {sum_num}')
