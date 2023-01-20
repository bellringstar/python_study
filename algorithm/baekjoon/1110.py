import sys
input = sys.stdin.readline

N = int(input())
original_N = N
cycle = 0
while True:
    ln = N // 10
    rn = N % 10
    new_num = rn * 10 + (ln + rn) % 10
    N = new_num
    cycle += 1
    if original_N == new_num:
        break
print(cycle)
