'''
주어진 수들을 M번 더해 가장 큰 수
특정 인덱스의 수가 연속해서 K번 초과하여 더해질 수 없다.
정렬 -> [-1] K개 더하고 [-2]한번 ... M번

'''

N, M, K = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

cnt = 0
cnt0 = 0
ans = 0

while cnt<M:
    ans += lst[-1] #가장 큰 수를 더한다
    cnt += 1
    cnt0 += 1
    if cnt0 == K: #가장 큰 수를 K번 더했다면
        ans += lst[-2] #두번째로 큰 수를 더하고 K 카운트 초기화
        cnt += 1
        cnt0 = 0

print(ans)