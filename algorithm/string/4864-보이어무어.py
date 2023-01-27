# T = int(input())

# for test in range(T):
#     str1 = input(); N = len(str1)
#     str2 = input(); M = len(str2)
#     if str1 in str2:
#         print(1)
#     else:
#         print(0)
#--------------------------------------------------------------------------

def boyer_moore(pattern, text):
    M = len(pattern) #XYPV M = 4
    N = len(text) #EOGGXYPVSY N =10
    i = 0

    while i <= N - M: # i <= 10 - 6 = 4
        j = M - 1 #j = 4 - 1 = 3 마지막 인덱스
        while j >= 0:
            if pattern[j] != text[i+j]: #if V != text[3] = G
                move = find(pattern, text[i+M-1]) #스킵리스트에서 이동량 생성 i+M-1 = 0 + 4 -1 = 3
                break
            j -= 1 # 일치할 시 그 다음  문자 비교
        if j == -1: #j == -1이다? while 조건이 만족해 끝났다. = 전부 일치
            return True
        else:
            i += move #반복이 끝났는데 -1이 아니면 글자가 없다. 스킵리스트 이동

def find(pattern, char):
    for i in range(len(pattern)-2, -1, -1): #ex)pattern = XYPV 4-2=2, -1, -1 : 2,1,0
        #len(pattern) - 2부터 시작하는 이유는 len(pattern) - 1은 이미 다르다고 결과가 나옴
        if pattern[i] == char: 
            return len(pattern) - i - 1 
    return len(pattern)
    

T = int(input())
for test in range(T):
    str1 = input(); N = len(str1) #XYPV N = 4
    str2 = input(); M = len(str2) #EOGGXYPVSY M =10
    if boyer_moore(str1, str2):
        print(1)
    else:
        print(0)








        


        


