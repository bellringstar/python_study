'''
자연수 N의 분해합
어떤 자연수 M의 분해합 = N -> M은 N의 생성자
ex)245 = 2+4+5+245 = 256 : 245는 256의 생성자
가장 작은 생성자
'''
'''
주어진 N 보다 작은 수에 대해 전부 상성자가 맞는지 계산
그중 처음 나오는 애 리턴
'''
N = int(input())
rst = 0
for num in range(N):
    sum = num
    for i in str(num):
        sum += int(i)
    if sum == N:
        rst = num
        break
print(rst)