'''
MN개의 단위 정사각형 MxN 크기 -> 8x8 추출
변을 공유하는 두 개의 사각형은 다른 색으로
다시 칠해야 하는 정사각형의 최소 개수
'''
'''
8<= N,M <= 50 
'''
N, M = map(int, input().split())
Carray = []
for i in range(M):
    Carray.append(input())

start_point = []
if N >= M:
    for i in range(M-7):
        for j in range(M-7):
           start_point.append([i,j])
else:
    for i in range(N-7):
        for j in range(N-7):
           start_point.append([i,j])

cnts = []
for point in start_point:
    cnt = 0
    for i in range(point[0], 8):
        for j in range(point[1], 8):
            if i + 1 < 8 and j+1 < 8:
                if Carray[i][j] == Carray[i+1][j] or Carray[i][j] == Carray[i][j+1]:
                    cnt += 1
    cnts.append(cnt)

print(cnts)

