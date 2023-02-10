def stack():
    i = 1 # 첫 원소
    d = 2 # 다음 스택 첫 원소와의 차이
    while True:
        s = [i]
        i += d
        d += 1
        yield s
def pos(t:int):
    s_idx = 1 #좌표가 1부터 시작하니 편의상 1로 시작
    d = 1
    d0 = 1
    idx = 0
    p = t
    s = stack()
    s1 = next(s) #스택 생성
    while True:
        if s1[idx] > p:
            s1 = next(s)
            s_idx += 1
            idx = 0
            d0 += 1
            d = d0
        elif s1[idx] < p:
            s1.append(s1[idx]+d)
            d += 1
            idx += 1
        else:
            return s_idx, idx+1


def find_v(x, y):
    s = stack()
    d = x
    for _ in range(x):
        s1 = next(s)
    for _ in range(y-1):
        s1.append(s1[-1]+d)
        d += 1
    return s1[-1]


T = int(input())

for tc in range(1, T+1):
    p, q = map(int, input().split())
    new_x = pos(p)[0] + pos(q)[0]
    new_y = pos(p)[1] + pos(q)[1]
    rst = find_v(new_x, new_y)
    print(f'#{tc} {rst}')







