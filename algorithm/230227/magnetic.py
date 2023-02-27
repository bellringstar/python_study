import sys
sys.stdin = open('input_magnetic.txt', 'r')
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #2는 위로 1은 아래로
    arr = list(zip(*arr))
    rst = 0
    for row in arr:
        idx_lst = []
        for idx in range(100):
            if row[idx] == 1:
                idx_lst.append(1)
            elif row[idx] == 2:
                idx_lst.append(2)
        stack = []
        cnt = 0
        for num in idx_lst:
            if num == 1:
                stack.append(num)
            else:
                if stack:
                    while stack:
                        stack.pop()
                    cnt += 1
                else:
                    pass
        rst += cnt
    print(f'#{tc} {rst}')