import sys, collections
input = sys.stdin.readline
q = collections.deque()

N, M = map(int, input().split()) #N = 세로 = 행, M = 가로 = 열
arr = [list(map(int, input().split())) for _ in range(N)]

