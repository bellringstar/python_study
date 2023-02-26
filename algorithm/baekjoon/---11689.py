import sys,math
input = sys.stdin.readline

n = int(input())
rst = n


for p in range(2,int(math.sqrt(n))+1):#시작 인덱스
    if n%p == 0: #p가 n의 소인수인가?
        rst -= rst/p #소인수라며 결과값을 업데이트한다.
        while n%p == 0: #ex) 2^7 * 11 이라면 2^7을 없애고 11만 남김
            n /= p

if n > 1: #제곱근까지만 탐색 -> 1개의 소인수가 누락되는 케이스 처리
    rst -= rst/n

print(int(rst))
