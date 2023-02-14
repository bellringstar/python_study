import sys
sys.stdin = open('1219input.txt', 'r')

def dfs(s, e):
    v = s
    stack = [v]
    visited = [0] * 100

    while stack:
        if stack[-1] == e:
            return 1
        visited[v] = 1
        for w in range(100):
            if not visited[w]:
                if arr[v][w]:
                    stack.append(w)
                    v = w
                    break
        else:
            stack.pop()
            if stack:
                v = stack[-1]
    else:
        return 0





for tc in range(10):
    T, N = map(int, input().split())

    arr = [[0]*100 for _ in range(100)]
    xy = list(map(int, input().split()))
    for i in range(0,len(xy)-1,2):
        x = xy[i]
        y = xy[i+1]
        arr[x][y] = 1

    rst = dfs(0, 99)
    print(f'#{T} {rst}')


