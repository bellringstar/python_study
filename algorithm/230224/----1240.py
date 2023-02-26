import sys
sys.stdin = open('1240input.txt', 'r')


T = int(input())
decode = {'0001101':'0', '0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
code_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N:세로 M:가로
    for _ in range(N):
        lst = list(input())
        if '1' in lst:
            for i in range(len(lst)-1,-1,-1):
                if lst[i] == '1':
                    idx= i
                    password = ''.join(lst[idx - 55:idx + 1])
                    break

    s = ''
    for i in range(0,56,7):
        s += decode[password[i:i+7]]
    check_sum = 0
    for idx in range(0,8,2):
        check_sum += 3*(int(s[idx])) + int(s[idx+1])
    if check_sum%10:
        print(f'#{tc} 0')
    else:
        answer = 0
        for num in s:
            answer += int(num)
        print(f'#{tc} {answer}')