'''
연산의 기준 1초 = 2천만번
데이터의 크기가 가장 클 때를 기준으로 대략적으로 계산

시간복잡도를 도출할 때
1. 상수는 시간 복잡도 계산에서 제외한다.
2. 가장 많이 중첩된 반복문의 수행 횟수가 시간 복잡도의 기준이 된다.

구간합
기존의 리스트 데이터를 전처리한 배열
A = [15, 13, 10, 7, 3, 12]
S = [15, 28, 38, 45, 48, 60] 누적 합 배열
이를 통해 일정 범위의 합을 구하는 시간복잡도가 O(N)에서 O(1)로 감소
S[i] = S[i-1] + A[i]
'''
