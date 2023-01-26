'''
10x10 0,0 -> 9,9 N개 왼쪽 위와 오른쪽 아래 모서리 인덱스 -> 겹치는 부분의 칸수
ex)2개
2 2 4 4 1 ([2, 2]부터 [4, 4]까지 color 1(빨강))
3 3 6 6 2 ([3, 3]부터 [6, 6]까지 color 2(파랑))
겹치는 부분 = [3, 3]부터 [4, 4] 까지 총 4칸
'''

import sys
input = sys.stdin.readline
T = int(input())
for test in range(T):
    N = int(input())
    color_list = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(N):
        r1,c1,r2,c2,color = map(int, input().split())
        for i in range(c1, c2+1): # 2,3,4
            for j in range(r1, r2+1): #2,3,4
                color_list[i][j] += 1
    cnt = 0
    for listC in color_list:
        cnt += listC.count(2)
    print(f'#{test+1} {cnt}')




