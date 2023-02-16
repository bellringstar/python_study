N = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0
if N<=2:
    cnt = 0
else:
    for i in range(2, len(A)):
        s = 0
        e = i-1
        while True:
            if A[s] + A[e] < A[i]:
                s += 1
            elif A[s] + A[e] > A[i]:
                s -= 1
            else:
                cnt += 1
                break
            if s == e:
                break

print(cnt)
