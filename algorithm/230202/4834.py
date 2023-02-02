'''
0~9까지 적힌 N장의 카드
가장 많은 카드에 적힌 숫자와 카드가 몇장인가. 장수가 같을 때는 숫자가 큰쪽
ex) N = 5 number = 49679
card_list = [4, 9, 6, 7, 9]
1. 각 카드의 개수를 세야한다.
count_list를 만들어 해당인덱스에 1씩 증가시킨다.
2. 최대값의 인덱스 출력
2-1. 최대값이 겹친다 -> 인덱스가 큰 쪽 출력
'''

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    card_list = list(map(int,input()))
    count_list = [0] * 10 # 0~9까지
    for num in card_list:
        count_list[num] += 1 #해당 번호에 1 추가 [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    maxN = count_list[0]
    max_card = 0
    for card in range(10): #count_list에서 최대로 나온 수를 찾아 반환
        if count_list[card] > maxN:
            maxN = count_list[card]

    for i in range(9, -1, -1): #겹치는 경우를 대비해 숫자가 큰것부터 일치하는 순간 출력
        if count_list[i] == maxN:
            max_card = i
            break
    print(f'#{test} {max_card} {maxN}')


