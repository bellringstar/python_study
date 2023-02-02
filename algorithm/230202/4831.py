'''
전기버스
0번출발 N번까지 이동
1회 충전 최대 K 이동
충전기는 M개 설치, 위치리스트
종점(N)번 도착 가능 = 충전횟수 불가능 = 0
장소인덱스 0 -> cnt = K
시작점을 늘려가면서 cnt 감소
cnt = 0일때 정거장 있나 확인
정거장 있다면 정거장cnt 1증가 정거장 없는cnt 초기화
없다면 정거장 없는 cnt 1 증가
없다면 장소 인덱스 - 1 후 다시 판정
만약 정거장 없는 cnt == k : return 0

'''
def on_charge(n):
    return n in M_list
    # return n in [1, 3, 5, 7, 9]
T = int(input())
for test in range(1, T+1):
    K, N, M = map(int,input().split())
    M_list = list(map(int,input().split()))

    cnt = K
    i = 1
    charge = 0
    uncharge = 0
    while i < N:
        if uncharge == K:
            charge = 0
            break
        cnt -= 1
        if cnt <= 0:
            if on_charge(i):
                charge += 1
                cnt = K
                uncharge = 0
            else:
                uncharge += 1
                i -= 1
                continue

        i += 1
    print(f'#{test} {charge}')


