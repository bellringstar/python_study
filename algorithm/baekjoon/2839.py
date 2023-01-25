#봉지를 최소한으로 봉지 = 3kg/5kg
# import sys
# input = sys.stdin.readline

# N = int(input())
# sol_list = []
# for i in range(N):
#     for j in range(N):
#         if N == 5* i + 3* j:
#             sol_list.append([i, j])
# sol_list.sort(key=sum)
# if sol_list == []:
#     print(-1)
# else:
#     print(sum(sol_list[0]))

#------------시간초과--------------------------

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

while N>=0:
    if N%5==0:
        cnt += N//5
        print(cnt)
        break
    else:
        N -= 3
        cnt += 1
else:
    print(-1)