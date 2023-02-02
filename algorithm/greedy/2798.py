'''
블랙잭
카드에 양의 정수, 딜러는 N장의 카드를 모두 숫자가 보이도록 놓는다
그 후 딜러는 M이라고 외친다
제한시간 안에 N장 중 3 장을 고르른다.
그 3장의 합이 M을 넘지 않고 M에 최대한 가깝게
출력 = 3장의 합
'''
'''
N장의 카드중 3장을 고른 수들의합= S 가운데 M-S가 0에 가깝다.
'''

N, M = map(int, input().split())
M_list = list(map(int,input().split()))

sum_list = []
for num1 in M_list:
    for num2 in M_list:
        if num1 != num2:
            for num3 in M_list:
                if num2 != num3 and num1 != num3:
                    sum = num1 + num2 +num3
                    sum_list.append(sum)

sum_list.sort(key=lambda x:M-x)
for num in sum_list:
    if num <= M:
        print(num)
        break