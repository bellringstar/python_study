# import sys
# input = sys.stdin.readline


# S = input().lower()

# def max_alp(s):
#     max_s = ""  
#     max_count = 0
#     for i in s:
#         if max_s == i:
#             continue
#         if max_count < s.count(i):
#             max_s = i
#             max_count = s.count(i)
#         elif max_count == s.count(i):
#             return "?"
#     return max_s.upper()


# print(max_alp(S)) 
#----------------------------시간초과----------------------------
import sys
input = sys.stdin.readline


S = input().rstrip().lower()
