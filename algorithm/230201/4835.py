import sys
sys.stdin = open('sample_input4835.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int,input().split()))
    '''
    N개의 정수, 이웃한 M개의 합/ output = M개의 합이 가장 큰경우 - 가장 작은 경우
    ex) N = 5, M = 3 num_list = [1, 2, 3, 4, 5]
    마지막에 더하는 수의 인덱스가 N-1보다 작은동안
    '''
    sumList = [0] * (N-M+1)
    for i in range(N-M+1):
        sumN = 0
        for j in range(i,i+M):
            sumN += num_list[j]
        sumList[i] = sumN

    minNum = sumList[0]
    maxNum = sumList[0]
    for num in sumList:
        if num < minNum:
            minNum = num
        if num > maxNum:
            maxNum = num

    print(f'#{test} {maxNum - minNum}')