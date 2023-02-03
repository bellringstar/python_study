'''
xkg, ycm (x,y) 둘 다 크다 = 덩치가 크다
등수 = 자신보다 더 큰 덩치의 사람 수
자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 수는 k+1 같은 등수 가능
'''
'''
입력 N = 사람 수, 그 후 x, y
출력: 나열된 사람의 등수
2<=N<=50
10<=x,y<=200
'''

N = int(input())
alst = []
for case in range(N):
    x, y = map(int,input().split())
    alst.append([x,y])

cnts = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j:
           if alst[i][0] < alst[j][0] and alst[i][1] < alst[j][1]:
               cnt += 1
    cnts[i] = cnt + 1

print(*cnts)