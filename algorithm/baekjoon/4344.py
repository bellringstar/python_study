import sys
input = sys.stdin.readline

C = int(input())
for i in range(C):
    count_N = 0
    N_score = list(map(int, input().split()))
    N = N_score[0]
    scores = N_score[1:]
    avg = sum(scores) / N
    for score in scores:
        if score > avg:
            count_N += 1
    print(f'{count_N/N * 100:.3f}%')

