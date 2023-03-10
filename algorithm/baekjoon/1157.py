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
dictS = {}
for s in set(S):
    dictS[s] = S.count(s)
cnt = sorted(dictS.items(), key=lambda x: x[1])

if len(cnt) > 1 and cnt[-1][1] == cnt[-2][1]:
    print('?')
else:
    print(cnt[-1][0].upper())