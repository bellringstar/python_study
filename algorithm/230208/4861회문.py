def check(word,length):
    i = 0
    while i < length//2:
        if word[i] != word[length - 1 - i]:
            return False
        i += 1
    return True

def row_check(arr,N,M):
    for i in range(N):
        for j in range(N-M+1):
            if check(arr[i][j:j+M], M):
                rst = arr[i][j:j+M]
                return rst

def col_check(arr, N, M):
    for start in range(N - M + 1):
        for j in range(N):  # 열
            word = ''
            for i in range(start, M + start):
                word += arr[i][j]
            if check(word, M):
                return word


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [0] * N
    for i in range(N):
        words[i] = input()
    if row_check(words, N, M):
        answer = row_check(words, N, M)
    else:
        answer = col_check(words, N, M)
        pass

    print(f'#{tc} {answer}')




