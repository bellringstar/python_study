'''
쌓여있는 노란상자 높은곳 -> 낮은곳 평탄화작업
평탄화 작업을 모두 한 후 최고 - 최저 <= 1
작업횟수의 제한. -> 제한 횟수 후 최고점,최저점 차이 출력
dump = 가낭 높은곳 -> 가장 낮은곳
상자의 높이 1~100
제한횟수 이전에 평탄화 끝 = 최고-최저 <= 1 : 종료 후 리턴

1. 가장 크기가 큰 값과 가장 작은 값을 찾는다.
2. 큰 값에서 -1, 작은 값에서 +1을 한다. cnt를 1 늘린다
3. 위의 과정을 반복. 도중에 cnt가 제한 값에 도달한다 반복 종료
'''

import sys
sys.stdin = open('Flatten_input.txt', 'r')

def dump(arr): #n = 덤프 횟수, arr = 각 상자의 높이값
    max_idx = find_max(arr)[0] #최대/최소값과 그 위치 찾기
    maxH = find_max(arr)[1]
    min_idx = find_min(arr)[0]
    minH =  find_min(arr)[1] 
    arr[max_idx] -= 1 #평탄화 작업
    arr[min_idx] += 1

def find_max(arr): #최대값과 인덱스 찾기
    maxH = arr[0]
    max_idx = 0
    for idx in range(len(arr)):
        if arr[idx] > maxH:
            maxH = arr[idx]
            max_idx = idx
    return max_idx, maxH

def find_min(arr): #최소값과 그 인덱스 찾기
    minH = arr[0]
    min_idx = 0
    for idx in range(len(arr)):
        if arr[idx] < minH:
            minH = arr[idx]
            min_idx = idx
    return min_idx, minH


T = 10
for test in range(1, T+1):
    cnt = 0 #dump 횟수
    gap = 0 #최대값과 최소값의 차이
    N = int(input())
    arr = list(map(int,input().split()))
    while cnt<N:
        dump(arr) #dump 1회 실행
        cnt += 1 #1행 횟수 증가
        gap =  find_max(arr)[1] - find_min(arr)[1] #실행 후 최대 - 최소
        if gap <= 1: #평탄화가 완료됐다면
            break

    print(f'#{test} {gap}')




