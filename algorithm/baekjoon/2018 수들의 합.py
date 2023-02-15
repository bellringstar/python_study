import sys
input = sys.stdin.readline

N = int(input())

rst = 1
start = end = 1
sum = 1

while end != N:
    if sum == N:
        rst += 1
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(rst)




