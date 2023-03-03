'''
1~25
가로,세로,대각 5개의 수 -> 선 1개
선이 3개 이상 - 빙고 : 가장 먼저가 우승
철수가 언제 빙고를 외치는가
'''
'''
1. 사회자가 수를 부를 때 마다 빙고판에서 숫자를 찾아 0으로 변경한다.
2. cnt가 15회일 때 부터 빙고 여부를 판단한다.
3. 빙고 여부 = 가로,세로,대각선으로 0이 연속으로 5개인가?
4. 빙고 카운터가 3이면 cnt를 출력하고 종료
'''
def bingo():
    global bingo_cnt
    for row in arr:
        if row.count(0) == 5:
            bingo_cnt += 1
    for row in list(zip(*arr)):
        if row.count(0) == 5:
            bingo_cnt += 1
    cnt1 = 0
    for i in range(5):
        if arr[i][i] != 0:
            break
        else:
            cnt1 += 1
    if cnt1 == 5:
        bingo_cnt += 1
    cnt2 = 0
    for i in range(5):
        if arr[i][4-i] != 0:
            break
        else:
            cnt2 += 1
    if cnt2 == 5:
        bingo_cnt += 1


arr = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
bingo_cnt = 0
for _ in range(5):
    lst = list(map(int, input().split())) #사회자가 부르는 수
    for num in lst:
        for row in arr:
            if num in row:
                row[row.index(num)] = 0
                cnt += 1
    if cnt >= 5:
        bingo()
        if bingo_cnt >= 3:
            print(cnt)
            break

