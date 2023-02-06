'''
100X100의 2차원 배열, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최대
'''

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    max_lst = []
    sumD1 = 0
    sumD2 = 0
    for i in range(100):
        sumR = 0 #행우선
        sumC = 0 #열우선
        for j in range(100):
            sumR += lst[i][j]
            sumC += lst[j][i]
            if i == j:
                sumD1 += lst[i][j]
            if i+j == 99:
                sumD2 += lst[i][j]
        if sumR > sumC:
            max_lst.append(sumR)
        else:
            max_lst.append(sumC)
    max_lst.extend([sumD1,sumD2])

    maxV = max_lst[0]
    for num in max_lst:
        if num > maxV:
            maxV = num
    print(f'#{T} {maxV}')



