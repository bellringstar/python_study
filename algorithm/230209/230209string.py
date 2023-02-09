'''
"==" 와 "is"의 차이
"=="는 값이 동일하냐, is는 주소가 동일하냐
파이썬에서는 내부적으로 특수 메서드 __eq__()를 호출
'''
# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
# 
# print(s1,s5, s1==s5, s1 is s5) #abc abc True False
# print(s1, s4, s1 == s4, s1 is s4, id(s1), id(s4)) #abc abc True True
# print(s1, s2, s1 == s2, s1 is s2, id(s1), id(s2)) #abc abc True True id 동일

#int()와 같은 atoi()함수 만들기
# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x) - ord('0')
#     return i

#str()과 같은 itoa()함수 만들기

'''
패턴 매칭
1. 고지식한 패턴 검색 알고리즘(Brute Force)
문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교
O(MN)
2. 카프-라빈 알고리즘
3. KMP 알고리즘
O(M+N)
불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분은 다시 비교하지 않는다.
패턴을 전처리 next[M]을 구해 잘못된 시작을 최소화함
next[M] : 불일치가 발생했을 경우 이동할 다음 위치
4. 보이어-무어 알고리즘
오른쪽에서 왼쪽으로 비교
오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 패턴의 길이만큼 이동
패턴 내에 존재하는 글자라면 패턴의 그 글자의 위치를 찾아 점프
'''

#1 Brute Force
p = 'is' #찾을 패턴
t = 'This is a book!' #전체 패턴
M = len(p)
N = len(t)

def BruteForce(p, t, N, M):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    while j < M and i < N : #비교할 문장이 남아있고, 패턴을 찾기 전
        if t[i] != p[j] : #철자마다 비교
            i = i - j #비교 시작점으로 복귀
            j = -1 #처음 비교 위치로 복귀
        i += 1 #다음칸으로 이동
        j += 1
    if j == M : return i - M #패턴을 찾은 경우 시작 위치 리턴
    else: return -1

#2 KMP 알고리즘