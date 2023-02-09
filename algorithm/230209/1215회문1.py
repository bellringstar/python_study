import sys
sys.stdin = open('1215input.txt', 'r')

def palindrome(word,length):
    i = 0
    while i < length//2:
        if word[i] != word[length - 1 - i]:
            return False
        i += 1
    return True


for tc in range(1, 11):
    cnt = 0 #회문의 개수
    N = int(input())
    arr = [input() for _ in range(8)] #바꿀 일 없으니 리스트로 받지 않고 문자열 그대로 받는다.


    #행 우선 판단
    for i in range(8):
        for j in range(8-N+1):
            word = arr[i][j:j+N]
            if palindrome(word, N):
                cnt += 1
    #열 우선 판단
    for start in range(8-N+1):
        for j in range(8):
            word = ''
            for k in range(start, N+start):
                word += arr[k][j]
            if palindrome(word, N):
                cnt += 1
    print(f'#{tc} {cnt}')


