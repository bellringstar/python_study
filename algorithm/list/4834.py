T = int(input())
for i in range(T):
    N = int(input())
    card = input()
    count_list = [0] * 9 #[0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_list = []
    for num in card:
        num_list.append(int(num)) #[4, 9, 6, 7, 9]
    for num in num_list:
        count_list[num-1] += 1
    max_count = max(count_list)
    max_num = count_list.index(max(count_list)) + 1
    if max_count == 1:
        max_num = max(num_list)

    print(f'#{i + 1} {max_num} {max_count}')
    
