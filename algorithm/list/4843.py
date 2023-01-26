'''
큰수 작은수 번갈아 정렬 
ex)10개 1~10까지 10 1 9 2 8 3 7 4 6 5
'''
T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    #일단 오름차순 정렬 1,2,3,4,5,6,7,8,9,10
    #뒤에서 하나 앞에서 하나 번갈아가며 추가
    num_list.sort()
    sorted_list = []
    i = 0
    j = -1
    while len(sorted_list) != len(num_list):
        sorted_list.append(num_list[j])
        sorted_list.append(num_list[i])
        i += 1
        j -= 1
    print(f'#{test+1}',end=' ')
    for num in sorted_list:
        print(num, end=' ')
