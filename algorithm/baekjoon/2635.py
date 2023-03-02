'''
f(n-2) = f(n) - f(n-1)
if f(n-2) < 0 => break
'''
import sys
input = sys.stdin.readline

N = int(input())
rst_lst = []
for i in range(1,N+1):
    arr = []
    arr.append(N)
    arr.append(i)
    while True:
        new_num = arr[-2] - arr[-1]
        if new_num < 0:
            break
        arr.append(new_num)

    if len(rst_lst) < len(arr):
        rst_lst = arr

print(len(rst_lst))
for i in rst_lst:
    print(i, end=' ')


