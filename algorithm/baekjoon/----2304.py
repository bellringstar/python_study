'''
자기자신보다 큰 것 or 큰 것이 없다면 작은것중에 최대 = 다음위치
'''
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
p1 = arr[0]
i = idx = 1
s = 0

#[(2, 4), (4, 6), (5, 3), (8, 10), (11, 4), (13, 6), (15, 8)]
while i < N :
    if arr[i][1] > p1[1]:
        s += (arr[i][0] - p1[0]) * p1[1]
        p1 = arr[i]
        idx = i
    i += 1

s += arr[idx][1]
#idx 가장 큰 기둥 이 이후에 더 큰 기둥 없다.
'''
최대값 기둥 이후 중 최대값 찾아 넓이계산. 그 값을 최대값 기둥으로 삼아 반복
'''
while idx+1 < N:
    h = 0
    x1 = arr[idx][0]+1
    x2 = 0
    for j in range(idx+1,N):
        if arr[j][1] >= h:
            h = arr[j][1]
            x2 = arr[j][0]+1 #최대값 위치 찾기
            idx = j
    s += (x2 - x1) * h

print(s)




