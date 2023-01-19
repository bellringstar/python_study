#입력 5 45321 -> 12345
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 수가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.
'''
# N = int(input())
# array = []
# while len(array) < N:
#     array.append(int(input()))

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end ='\n')
#=========================================시간초과
# N = int(input())
# array = []
# while len(array) < N:
#     array.append(int(input()))

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for idx in range(len(count)):
#     if count[idx] > 0:
#         print(idx)
#=========================================시간초과