n = 10**6
arr = [True] * n
arr[0] = False
arr[1] = False

for i in range(2, n):
    if arr[i] == True:
        #arr[i]의 배수들 전부 False 처리
        k = 2
        while i* k < n:
            arr[i*k] = False
            k +=1
for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')

