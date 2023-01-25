def check(position, n):
    global counter, recursion_num
    if n >= N:
        return counter
    if recursion_num > K:
        counter = 1
        return counter
    
    if charger_pos[n] == 1:
        counter += 1
        recursion_num += 1
        return check(position, n + K)
        
    else:
        recursion_num += 1
        return check(position, n - 1)


T = int(input()) #노선 수
for test in range(T):
    counter = 0
    recursion_num = 0
    K, N, M = map(int, input().split()) #0번 출발 N번 종착점, 한번 충전으로 K 이동, 충전기 M개 설치 3/ 10/ 5
    charger = list(map(int, input().split())); charger.insert(0, 0) # 충전기 위치 # [0, 1, 3, 5, 7, 9]
    charger_pos = [0] * (N+1) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in charger:
        charger_pos[num] = 1 #[1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    check(charger_pos, 0)
    print(counter-1)

