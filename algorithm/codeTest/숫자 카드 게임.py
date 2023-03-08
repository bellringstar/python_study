'''
여러개 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장
1.NXM (N행,M열)
2.뽑으려는 카드가 있는 행 선택
3. 그 행에서 가장 작은 숫자 카드
'''
N, M = map(int, input().split()) #N: 행 M: 열
arr = [list(map(int, input().split())) for _ in range(N)]

