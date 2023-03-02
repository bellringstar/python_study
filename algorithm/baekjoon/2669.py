arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    lx,ly,rx,ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            arr[i][j] = 1

rst = 0
for row in arr:
    rst += sum(row)

print(rst)