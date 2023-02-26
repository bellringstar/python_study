'''
수열의 합
수열의 두 수를 묶는다. 위치에 관계없다.
묶은 후 수열의 합을 구할 때 묶은 수는 서로 곱한 후 더한다
묶거나, 묶지 않거나, 합이 최대
'''
N = int(input())
s = []
for _ in range(N):
    s.append(int(input()))

s.sort()


