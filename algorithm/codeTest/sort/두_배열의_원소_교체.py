N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)



for i in range(N):
    if A[i] < B[i]:
        A[i] = B[i]
        K -= 1
        if K == 0:
            break

print(sum(A))

