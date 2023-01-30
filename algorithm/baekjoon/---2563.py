import sys
input = sys.stdin.readline

'''
1.검정 도화지 모서리 좌표 저장 넓이는 항상 100
2.좌표 범위가 겸치는 곳의 넓이 뺴기
'''
paper_list = []
N = int(input()) #3
for _ in range(N):
    x,y = map(int, input.split()) #왼쪽 아래 좌표
    