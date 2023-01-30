#원형큐
'''
N개의 숫자로 이루어진 수열 맨 앞의 숫자를 맨 뒤로 보내는 작업 M번 했을 때 맨 처음 수
1. [0]을 pop 해 [len(num_list)]로 보낸다.
2. M번 반복
'''

N,M = map(int, input().split())
num_list = list(map(int, input().split()))

# for _ in range(M):
#     num_list.append(num_list.pop(0))

# print(num_list[0])

#원형 큐 사용
