'''
idx => 0:5 /1:3/2:4 마주보는 상태
각 주사위 아래/위 를 제외한 최대 수의 합
1. 1번 쥐사위에서 아래가 될 녀석을 정한다.
2. 쌓아가며 맞춤 수를 제외한 최대값을 더해간다.
'''
import sys
input = sys.stdin.readline

idx_dict = {0:5,1:3,2:4,3:1,4:2,5:0}
N = int(input())
ans = 0
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for tmp2 in range(1, 7):
    rst = 0
    for row in arr:
        idx = row.index(tmp2)
        idx1 = idx
        tmp1 = row[idx1]
        row[idx1] = 0
        idx2 = idx_dict[idx1]
        tmp2 = row[idx2]
        row[idx2] = 0
        rst += max(row)
        row[idx1] = tmp1
        row[idx2] = tmp2

    ans = max(ans, rst)
print(ans)



