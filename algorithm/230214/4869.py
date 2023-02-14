T = int(input())


def paper(N):
    if N > 2 and len(rst) < N:
        rst.append(paper(N - 1) + 2 * paper(N - 2))
    return rst[N - 1]

for tc in range(1, T+1):
    rst = [1, 3]
    N = int(input())
    answer = paper(N//10)
    print(f'#{tc} {answer}')

