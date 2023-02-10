T = int(input())
for tc in range(1, T+1):
    words = input()
    n = len(words)
    pattern = list(zip('#' * n, '.' * n, words, '.' * n))
    arr = [[0]*(4*n+1) for _ in range(5)]



