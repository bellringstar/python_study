import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# arr.sort()
#
# S = [arr[0]] * N
#
# for i in range(1, N):
#     S[i] = S[i-1] + arr[i]
#
# print(sum(S))

# for i in range(1,N):
#     for j in range(i,0,-1):
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1],arr[j]
#         else:
#             break
#
# S = [arr[0]] * N
#
# for i in range(1, N):
#     S[i] = S[i-1] + arr[i]
#
# print(sum(S))


S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        arr[j] = arr[j-1] #한칸씩 미룬다
    arr[insert_point] = insert_value

