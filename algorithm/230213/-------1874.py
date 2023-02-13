n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = int(input())


def check(arr, n):
    i = 0
    j = 1
    stack = []
    rst = []
    while i < n-1:
        for k in range(j, arr[i]+1):
            stack.append(k)
            rst.append('+')
        stack.pop()
        rst.append('-')
        j = arr[i] +1
        while i+1 < n:
            if stack and arr[i+1] == stack[-1]:
                stack.pop()
                rst.append('-')
                i += 1
            elif (stack and arr[i+1] > stack[-1]) or not stack:
                i += 1
                break
            else:
                rst = ['NO']
                return rst

    return rst

for i in check(arr, n):
    print(i)

