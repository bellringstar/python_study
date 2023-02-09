import sys
sys.stdin = open('회문2_input.txt', 'r')

# def palindrome(word):
#     i = 0
#     n = len(word)
#     while i <= n // 2:
#         if word[i] != word[-1 - i]:
#             return False
#         i += 1
#     return True
#
# for tc in range(10):
#     arr = []
#     T = int(input())
    # maxV = 0
    # for i in range(100):
    #     arr.append((input()))
    # for i in range(100,0,-1): #길이가 i인 회문 처음으로 나오면 break
    #     for j in range(100): #각 행마다
    #         for k in range(101-i):
    #             word = arr[j][k:k+i]
    #             if palindrome(word):
    #                 if i>maxV:
    #                     maxV = i
    #                     break
    #
    # for i in range(100, 0, -1):
    #     word =''
    #     for start in range(101-i):
    #         for j in range(100):
    #             for k in range(start, start+i):
    #                 word += arr[k][j]
    #             if palindrome(word):
    #                 if i>maxV:
    #                     maxV = i
    #                     break
    #
    # print(f'#{T} {maxV}')

def palindrome(word):
    i = 0
    n = len(word)
    while i <= n // 2:
        if word[i] != word[-1 - i]:
            return False
        i += 1
    return True


def palindrome_row(arr):
    for i in range(100,0,-1): #길이가 i인 회문 처음으로 나오면 break
        for j in range(100): #각 행마다
            for k in range(101-i):
                word = arr[j][k:k+i]
                if palindrome(word):
                    return len(word)

def palindrome_col(arr):
    for i in range(100, 0, -1):
        for start in range(101-i):
            for j in range(100):
                word = ''
                for k in range(start, start+i):
                    word += arr[k][j]
                if palindrome(word):
                    return len(word)



for tc in range(10):
    arr = []
    T = int(input())
    maxV = 0
    for i in range(100):
        arr.append((input()))

    row_V = palindrome_row(arr)
    col_V = palindrome_col(arr)
    if row_V >= col_V :
        answer = row_V
    else:
        answer = col_V
    print(f'#{T} {answer}')

