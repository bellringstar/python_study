'''
NxM
캐릭터가 향하는 방향 동서남북
(A,B) = A:북쪽으로부터 떨어진 칸의 개수, B: 서쪽으로부터 떨어진 칸의 개수 = 행,열
현재 방향 기준 왼쪽부터 반시계 90도로 갈 방향을 정한다.
바로 왼쪽에 가지 않은 곳 -> 왼쪽방향으로 회전한 다음 왼쪽칸 이동
바로 왼쪽에 가지 않은곳이 없다 -> 왼쪽방향으로 회전 후 다시 반시계 90도
4방향이 전부 방문 or 바다 -> 방향 유지한채 1칸 뒤로 후 90도, 만약 뒤가 바다다? 중지
'''

N, M = map(int, input().split())
A, B, d = map(int, input().split()) # d : 0/1/2/3 = 북/동/남/서
arr = [list(map(int, input().split())) for _ in range(M)] # 1바다 0 육지
visited = [[False] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            visited[i][j] = True

move = ((-1,0),(0,1),(1,0),(0,-1)) #북 서 남 동

direction = {0:3, 1:0, 2:1, 3:2}

cnt = 0
while True:
    visited[A][B] = True
    new_r = A + move[d][0]
    new_c = B + move[d][1]
    if arr[A][B-1] != 1 and not visited[A][B-1]:
        d = direction[d]
        B -= 1
        cnt += 1

    elif arr[new_r][new_c] == 0 and not visited[new_r][new_c]:
        A = new_r
        B = new_c
        cnt += 1


    elif visited[A-1][B] and visited[A+1][B] and visited[A][B-1] and visited[A][B+1]:
        if d==0:
            A += 1
            if arr[A][B] == 1:
                break
        elif d==1:
            B -= 1
            if arr[A][B] == 1:
                break
        elif d==2:
            A -= 1
            if arr[A][B] == 1:
                break
        else:
            B += 1
            if arr[A][B] == 1:
                break

    else:
        d = direction[d]



print(cnt)






