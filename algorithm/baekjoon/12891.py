'''
경우의 수
'''
# import collections, sys
# input = sys.stdin.readline
#
# S, P = map(int, input().split())
# DNA = input()
# keys = ['A', 'C', 'G', 'T']
# values = list(map(int, input().split()))
# ACGT = zip(keys, values)
# ACGT_dic = {key:value for key,value in ACGT}
# cnt = 0
#
# for i in range(S-P+1):
#     check = DNA[i:i+P]
#     c = collections.Counter(check)
#     for key in ACGT_dic.keys():
#         if c[key] < ACGT_dic[key]:
#             break
#     else:
#         cnt += 1
#
# print(cnt)
#----------시간초과
'''
정답
checkList = [0] * 4 #A,C,G,T 가 몇개 필요한가
myList = [0] * 4 # 현재 윈도우에 A,C,G,T가 몇개인가
checkSecret = 0 # 조건에 만족한 문자 개수

def myadd(c): #해당 문자열의 개수 증가
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): #비교해서 개수 제거
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    if c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    if c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    if c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
rst = 0
A = list(input()) #문자열
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1
for i in range(P):
    myadd(A[i])
if checkSecret == 4:
    rst += 1
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        rst += 1

print(rst)
'''



