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
    if parent[a] == a:
        return a
    else:
        return find(parent[a])

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a



N, M = map(int, input().split()) #N:사람수, M 파티수
known = list(map(int, input().split())) #아는 사람 수
if known[0] == 0:
    rst = M
else:
    known = known[1:]
    rst = 0 #결과값
    cnt = 0
    parent = [i for i in range(N+1)] #idx = 번호
    for idx in range(1, len(known)):
        union(known[0],known[idx])
    arr = [list(map(int, input().split()))[1:] for _ in range(M)]
    for lst in arr:
        for people in known:
            if people in lst:
                for i in range(len(lst)):
                    union(people, lst[i])
                    known.append(lst[i])
                break
    for lst in arr:
        for num in lst:
            if num in known:
                break
        else:
            cnt += 1

    rst = cnt

print(rst)





