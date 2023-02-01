'''
알고리즘: 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
슈도코드를 사용해 표현하는 법을 연습
좋은 알고리즘
1. 정확성
2. 작업량
3. 메모리 사용량
4. 단순성
5. 최적성

반복해서 풀어보자

배열
메모리에 같은이름으로 연속성있게 저장하는것
하나의 변수명으로 다양한 자료를 관리

입출력을 제외한 내장함수 사용금지

가능하면 배열은 크기를 정해놓고 생성한 뒤 풀자. append는 최소화

1. 버블정렬
인접한 두 값을 비교해 교환해가며 맨 마지막 자리까지 이동
그럼 마지막 자리는 고정, 한 사이즈 작은 배열에 다시 정렬을 반복
'''


# blocks = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# N = len(blocks)

# for i in range(0, N):
#     cnt = 0
#     for j in range(i+1, N):
#         if blocks[i] > blocks[j]:
#             cnt += 1
#     print(cnt)

# curMaxV = 0
# res = [0] * N
# for i in range(0, N):
#     cnt = 0
#     for j in range(i+1, N):
#         if blocks[i] > blocks[j]:
#             cnt +=1
#
#     if curMaxV < cnt:
#         curMaxV = cnt
#
# print(curMaxV)


