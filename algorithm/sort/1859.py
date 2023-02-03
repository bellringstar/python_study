'''
사재기 최대한 이득
1. 연속N일 동안의 물건 매매가를 안다.
2. 하루에 최대 1만큼 구입
3. 판매는 얼마든지
'''
'''
날짜순 언제 사고 언제 파는게 중요
가격 리스트의 순위를 정하는 lst를 만든다
정렬된 가격 리스트 price [1,5,87, 99]
원래 lst [1, 87, 5, 5, 99, 1, 5, 23, 85]
원래 리스트의 최대값을 찾고 price에서 그 값의 인덱스를 찾는다. 최대값 99 , idx = 3
최대값 이전의 것들에서 cnt+1, buy += cnt*값 반복
최대값을 만나면 최대값*cnt - buy -> profit 기록
최대값 이후의 리스트에서 위 작업 반복

 '''
import sys
sys.stdin = open('input1859.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    def max_price(lst,start):
        max_idx = start
        maxP = lst[start]
        for i in range(start, len(lst)):
            if lst[i] > maxP:
                maxP = lst[i]
                max_idx = i
        return max_idx


    i = 0
    money = 0
    while True:
        if i >= len(lst):
            break
        cnt = 0
        buy = 0
        max_idx = max_price(lst,i)
        for j in range(i, max_idx):
            cnt += 1
            buy += lst[j]
        money += lst[max_idx] * cnt - buy
        i = max_idx + 1
    print(f'#{tc} {money}')










