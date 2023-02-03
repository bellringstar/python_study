'''
1~M번 위원
종목 N개
A =[0, 1, 2 ..]  0 = A1을 개최하는데 드는비용
B = J번 위원은 개최비용이 B를 넘지 않는 종목중에 가장 재미있는 경기
ex) N = 4
A = [5, 3, 1, 4]
B = [4, 3, 2]
B1: 비용이 4이하이면서 가장 앞에 있는 종목 A2 = 3
B2: 비용이 3이하이면서 가장 앞에 있는 종목 A2 = 3
B3: 비용이 2이하이면서 가장 앞에 있는 종목 A3 = 1
-> 최종적으로 A2 선정정

1. 종목 N큼 count list를 만든다
2. B의 1번 기준. A의 1부터 값을 비교해가며 해당하는 경우를 만나면 count에 1 추가하고 종료
3. B의 끝까지 반복
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnts = [0] * N
    for i in range(M):
        for j in range(N):
            if A[j] <= B[i]:
                cnts[j] += 1
                break

    maxV = cnts[0]
    max_idx = 0
    for i in range(len(cnts)):
        if maxV < cnts[i]:
            maxV = cnts[i]
            max_idx = i
    print(f'#{tc} {max_idx+1}')