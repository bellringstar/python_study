N = int(input())

lst = [0]*N
for idx in range(N):
    lst[idx] = int(input())

lst.sort()
for num in lst:
    print(num)