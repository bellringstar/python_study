'''
겹치는 칸 수
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    lst = []
    for _ in range(N):
        r1x,c1y,r2x,c2y,c = list(map(int, input().split()))
        for i in range(r1x, r2x+1):
            for j in range(c1y, c2y+1):
                if [i,j] in lst:
                    cnt +=1
                else:
                    lst.append([i,j])
    print(f'#{tc} {cnt}')