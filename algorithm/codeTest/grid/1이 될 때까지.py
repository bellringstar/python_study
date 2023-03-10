'''
N에서 1을 뺸다 or N을 K로 나눈다.
최소 횟수만에 N을 1로 만들어야한다.
대부분의 경우 나머지가 유리
나눠진다 -> 나눈다 안나눠진다 -> 1을 뺸다 반복
'''
N, K = map(int, input().split())

cnt = 0
while N!=1:
    if N%K == 0:
        N //=K
    else:
        N -= 1
    cnt += 1

print(cnt)