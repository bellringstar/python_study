N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()


start = 0
end = arr[-1]

while start <= end:
    h = (start + end) //2
    sumV = 0
    for num in arr:
        if num > h:
            sumV += (num-h)

    if sumV >= M:
        rst = h
        start = h + 1

    else:
        end = h - 1


print(rst)

