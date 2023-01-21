import sys
input = sys.stdin.readline

def O_counter(n,score = 1):
    if len(n) == 1:
        return score
    if n[-2] == 'X':
       return score
    return O_counter(n[:-1],score+1) 

T = int(input())
for i in range(T):
    score = 0
    rst = input()
    for idx in range(len(rst)):#OOXXOXXOOO
        if rst[idx] == 'O':
            score += O_counter(rst[:idx+1])
    print(score)


#OOO
#XOO



