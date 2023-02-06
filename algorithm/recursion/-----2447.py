'''
재귀적 패턴으로 별을 찍어보자
N = 3의 거듭제곱 NxN정사각
ex) 크기 3의 패턴
***
* *
*** 가운데에 공백
N > 3: 공백으로 채워진 가운데의 (N/3)x(N/3) 정사각형을 N/3의 패턴으로 둘러 싼 형태
'''

'''
pattern 1 을 3X3으로 나온게 pattern 2
pattern 2 를 3X3으로 나온게 pattern 3
pattern을 찍는 작업
blank를 찍는 작업
'''

def depth(lst):
    if lst:
        print(1)
    for i in lst:
        depth(i)

lst = [[[1,2,3], [1,5,2]]]
# depth(lst)
