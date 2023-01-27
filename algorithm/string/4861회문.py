#회문 찾기 가로,세로 가능 N * N 사이즈 글자판 길이가 M인 회문
def circular(string): #ABCBA
    i = 0 
    while i<=len(string)//2:
        if string[-1 - i] != string[i]:
            return False
        i += 1
    return True
def print_circular(N, M):
    lst = []
    for i in range(N):
        line = input()
        lst.append(line)
    #1. 문자열 생성 -> 회문 확인 : 모든 문자열에 반복작업
    # print(lst)
    for s in lst:
        k = 0
        while M+k <= len(s):
            if circular(s[k:M+k]):
                return s[k:M+k]
            else:
                k+=1
    j = 0
    while j<=N-1:            
        string = ''
        r = 0
        for idx in range(N):
            string += lst[r][j]
            r += 1
        j += 1
        if circular(string):
            return string

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    print(f'#{test+1} {print_circular(N, M)}')
    

    
        
            



