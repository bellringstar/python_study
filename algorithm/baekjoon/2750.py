N = int(input())
arr = []
for _ in range(5):
    arr.append(int(input()))

for i in range(N, -1, -1):
    for j in range(i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr:
    print(i)