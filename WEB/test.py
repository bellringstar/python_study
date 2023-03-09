A = [300, 60, 10]

T = int(input())
rst = []
k = 0
while T:
    if T >= A[k]:
        cnt = T//A[k]
        T %= A[k]
        A[k] = cnt
    else:
        A[k] = 0
    k+= 1
    if k >= 3:
        A = [-1]
        break

print(*A)