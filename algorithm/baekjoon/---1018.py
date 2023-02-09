#브루트 포스
pattern = ['BW'*4 , 'WB'*4]

N, M = map(int, input().split())

arr = [input() for _ in range(N)]

for i in range(M-7):
    for j in range(N-7): #시작점 i,j
        for k in range(i, i+8):
            for l in range(j, j+8):
                if arr[k][l] == 'B' #B로 시작시 pattern[0]
                    pass
                else: #A로 시작시 pattern[1]
                    pass
