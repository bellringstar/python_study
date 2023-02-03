'''
최소개수 거스름돈 N = 금액
'''
'''
1. 돈 리스트를 만든다.
2, 사용된 돈의 카운트를 기록할 리스트를 만든다.
3. 큰 것부터 가능한만큼 빼고 뺀 횟수를 리스트에 기록한다.
'''
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    cnts = [0]*8
    for idx in range(len(money)):
        cnt = 0
        while money[idx] <= N:
            cnt += 1
            N -=  money[idx]
        cnts[idx] = cnt

    print(f'#{tc}')
    print(*cnts)