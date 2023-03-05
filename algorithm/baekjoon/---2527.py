'''
공통 부분의 형태
'''

import sys
input = sys.stdin.readline

for _ in range(4):
    lst = list(map(int, input().split()))
    s1 = lst[:4]
    s2 = lst[4:]
    set1 = set()
    set2 = set()
    for i in range(s1[0],s1[2]):
        for j in range(s1[1],s1[3]):
            set1.add((i,j))
    for i in range(s2[0],s2[2]):
        for j in range(s2[1],s2[3]):
            set2.add((i,j))
    print(set1 & set2)