import sys
input = sys.stdin.readline

N = int(input())
cnt_list = [0] * N #[0, 0, 0, 0, 0] N = 5
for i in range(N):
    a = int(input())
    cnt_list[i] = a

cnt_list.sort()
for num in cnt_list:
    print(num)

