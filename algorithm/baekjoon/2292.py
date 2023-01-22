# import sys
# input = sys.stdin.readline()

# A, B, V = map(int, input().split())

# def day(A, B, V):
#     h = 0
#     count = 0
#     while h < V:
#         h += A
#         count +=1
#         if h >=V :
#             break
#         h -= B
#     return count

# print(day(A, B, V))


#--------------------시간초과
import math

A, B, V = map(int, input().split())

if A>=V:
    print(1)
else:
    print(math.ceil((V - A)/(A - B) + 1))
