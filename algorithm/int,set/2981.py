N = int(input())
lst = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            lst[i][j] = 1

rst = 0
for k in range(100):
    rst += lst[k].count(1)

print(rst)