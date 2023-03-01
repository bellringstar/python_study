'''
진실을 아는 사람이 온다 = 진실을 이야기한다
안온다 = 거짓을 이야기한다.
아는 사람이 껴있는 파티 = 전부 아는사람으로 -> 해당 파티 모든 번호가 같은 집합
파티에 아는 사람이 포함돼있다
-> 같은 집합으로 묶고 아는 사람에 추가한다.
그 다음 파티에 아는 사람이 포함돼있다
-> 반복
포함 안돼있다 -> cnt ++
'''


import sys
input = sys.stdin.readline

def find(a):
    if people[a] == a:
        return a
    else:
        return find(people[a])

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        people[b] = a



N, M = map(int, input().split()) # N:사람수, M:파티수
know = list(map(int, input().split()))
party = [[] for _ in range(M+1)]
for idx in range(1, M+1):
    party[idx] = list(map(int, input().split()))
people = [0] * (N+1)
for i in range(1, N+1):
    people[i] = i






